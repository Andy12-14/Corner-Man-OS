import os
from  config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a valid file in the current working directory'
    
    try:
        with open(abs_file_path, 'r', encoding='utf-8') as file:
            content = file.read(MAX_CHARS)
            if len(content) >= MAX_CHARS:
                content += f"\n\n[{file_path} Truncated: File content exceeds maximum length]"
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {str(e)}'


schema_get_file_content = types.FunctionDeclaration(
name="get_file_content",
description="Get the content of the given file as a string, constrained to the working directory.",
parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "file_path": types.Schema(
            type=types.Type.STRING,
            description="The path to the file from working directory .",
        ),
    },
),
)