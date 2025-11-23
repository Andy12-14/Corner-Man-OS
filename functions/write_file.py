import os 
from google.genai import types

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    parent_dir = os.path.dirname(abs_file_path)

    if not os.path.isdir(parent_dir):
   
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f'Error creating directories for "{file_path}": {str(e)}'
    
    try:
        with open(abs_file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return f'Success: Content written to "{file_path}" ({len(content)} characters)'
    except Exception as e:
        return f'Error writing to file "{file_path}": {str(e)}'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites to an existing files or write to an new file if it doesn't exist (and create required parent dir safely) , constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the fileas a string.",
            )
        },
    ),
)