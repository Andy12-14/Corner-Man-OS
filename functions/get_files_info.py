import os
from google.genai import types


# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False

def get_files_info(working_directory: str, directory = "."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
        
    if not abs_directory.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    contents = os.listdir(abs_directory)

    final_response = ""
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        is_dir = os.path.isdir(os.path.join(abs_directory, content))
        size = os.path.getsize(content_path)
        final_response += f'Name: {content} | Type: {"Directory" if is_dir else "File"} | Size: {size} bytes\n'
    return final_response


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)