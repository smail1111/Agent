import os
from os import *

def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    working_dir_path = os.path.abspath(working_directory)
    
    target_path = os.path.normpath(os.path.join(working_dir_path, directory))
        
    valid_target = os.path.commonpath([working_dir_path, target_path]) == working_dir_path
        
    if not valid_target:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    elif not os.path.isdir(target_path):
        return f'Error: "{directory}" is not a directory'
    
    def desc_contents(file):
        filepath = f"{target_path}/{file}"
        return f"- {file}: file_size={os.path.getsize(filepath)} bytes, is_dir={os.path.isdir(filepath)}"

    return f"Results for '{directory}' directory:\n{
            "\n".join(
            list(
                map(desc_contents, os.listdir(target_path))
                )
            )
                }"