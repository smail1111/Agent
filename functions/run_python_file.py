import os
import subprocess
def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_path = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_path, file_path))

        valid_target = os.path.commonpath([working_dir_path, target_path]) == working_dir_path

        if not valid_target:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
    
        if (target_path[-3:]) != ".py":
            return f'Error: "{file_path}" is not a Python file'
    
        command = ["python", target_path]
        if args:
            command.extend(args)
        
        output = subprocess.run(command, stdout=True, stderr=True, timeout=30, text=True)
        
        text = f"STDOUT:\n{output.stdout}\nSTDERR:\n{output.stderr}"

        if output.returncode != 0:
            text = text + f"\nProcess exited with code {output.returncode}"
        
        if not output.stdout and not output.stderr:
            text = text + f"\nNo output produced"

        return text


    except Exception as e:
        return f"Error: {e}"