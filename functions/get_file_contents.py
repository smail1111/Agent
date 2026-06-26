import os

def get_file_contents(working_directory: str, file_path: str) -> str:
    
    try:
        working_dir_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_path, file_path))

        valid_target = os.path.commonpath([working_dir_path, target_path]) == working_dir_path

        if not valid_target:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_path, "r") as file:
            content = file.read(10000)
            
            if file.read(1):
                content = content + f'[...File "{file_path}" truncated at 10000 characters]'
        
        return content
    
    except Exception as e:
        print(f"Error: {e}")