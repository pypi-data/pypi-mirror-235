from logclshelper import LogClsHelper

import subprocess
import os
import re
from contextlib import contextmanager
from pathlib import Path
import itertools
from collections import deque

class SysHelper(LogClsHelper):
    
    @classmethod
    def run_cmd(cls, cmd):
        cls.logger().debug(f'#beg# ! {cmd}')
        
        p = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, env = os.environ)

        cls.logger().debug(f'#end# ! {cmd}')
        return p

    @classmethod
    def walk_non_recursive(cls, parent_dir = '/'):
        cls.logger().debug(f'#beg# walk_non_recursive {parent_dir}')
        
        for pdir, dirs, files in os.walk(parent_dir):
            dirs = [os.path.join(pdir, dir) for dir in dirs]
            files = [os.path.join(pdir, file) for file in files]
            
            cls.logger().debug(f'#end# walk_non_recursive {parent_dir, len(dirs), len(files)}')
            
            return dirs, files

        cls.logger().debug(f'#end# walk_non_recursive {parent_dir}')

    @classmethod
    def walk(cls, parent_dir = '/'):
        cls.logger().debug(f'#beg# walk {parent_dir}')
        
        fifo = deque()
        fifo.appendleft((parent_dir, 0))
        
        while(any(fifo)):
            pdir, depth = fifo.pop()
            dirs, files = cls.walk_non_recursive(parent_dir = pdir)
            
            for next_dir in dirs:
                fifo.appendleft((next_dir, depth + 1))
    
            yield (pdir, dirs, files, depth, fifo)
            
        cls.logger().debug(f'#end# walk {parent_dir}')
                            
    @classmethod
    def yield_filtered_paths(cls, 
        parent_dir = '.', 
        lambda_filter_path = lambda path : True,
        accept_files = True,
        accept_dirs = True,
        min_depth = None,
        max_depth = None
    ):  
        not_valid = (
            ((min_depth is not None) and (max_depth is not None)) and 
            ((min_depth > max_depth) or (max_depth < 0))
        ) or (
            (not accept_dirs) and (not accept_files)
        )
        
        if(lambda_filter_path is None) :
            lambda_filter_path = lambda path : True
           
        if(not not_valid):
            for pdir, dirs, files, depth, fifo in cls.walk(parent_dir):                
                if((min_depth is not None) and (depth < min_depth)):
                    continue
    
                if((max_depth is not None) and (depth > max_depth)):
                    break
    
                accepted = (
                    itertools.chain(dirs, files) if(accept_dirs and accept_files) 
                    else(
                        dirs if accept_dirs
                        else (
                            files if accept_files 
                            else []
                        )
                    )
                )
    
                for file_or_dir in accepted:
                    if lambda_filter_path(file_or_dir):
                        yield file_or_dir
    
    @classmethod
    @contextmanager
    def chdir_context(cls, path):
        cls.logger().debug(f'#beg# chdir context {path}')
        
        origin = Path().absolute()
        try:
            os.chdir(path)
            yield
        finally:
            os.chdir(origin)
            
            cls.logger().debug(f'#end# chdir context {path}')









