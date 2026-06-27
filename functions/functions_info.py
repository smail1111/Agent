from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)") },
        required=["directory"]
    ),
)

from google.genai import types


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_contents",
    description="Lists the contents of a specified file relative to the working directory. If the file is over 10000 characters long, the contents will be truncated at 10000 characters",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to list contents from, relative to the working directory",) },
        required=["file_path"],
    ),
)

from google.genai import types


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Will replace the contents of a specified file with the specified content, or create a new file or parent directory if the either does not exist, relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write content into or create, relative to the working directory. If the parent directory of the file path does not exist, it will be created"),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into file",) },
        required=["file_path","content"],
    ),
)


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Will run a specified Python file with optional arguments and return the standard output and standard error",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Python file path to run and return result"),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING
                ),
                description="Optional arguments to input into python file"), },
        required=["file_path"],
    ),
)


available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],
)