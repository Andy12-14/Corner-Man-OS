import os 
import subprocess
import time
from google.genai import types

def run_python_file(working_directory: str, file_path : str, args = []):
     abs_working_dir = os.path.abspath(working_directory)
     abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
     if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
     
     if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a valid file in the current working directory'
     
     if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python (.py) file'
        
     try:
        final_args = ['python', file_path ]
        final_args.extend(args)
        output = subprocess.run(
            final_args,
            cwd=abs_working_dir,
            capture_output=True,
            timeout=30
        )
        final_string = f"""  
       --- Output of "{file_path}" ---
       
        STDOUT:
        {output.stdout}
        
        STDERR:
        {output.stderr}
        ------------------------------
        """
        if output.stdout == "" and output.stderr == "":
            final_string = f"\n[No output from running {file_path}]"
        if output.returncode != 0:
            final_string = f"\n[Error running {file_path}, return code {output.returncode}]\n\n{final_string}"
        return final_string

     except Exception as e:
        return f'Error running file "{file_path}": {str(e)}'
    


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file with the python interpreter. Accepts additional CLI args as an option array. Constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An option array of string to be use as the CLI args for the python file",
                items=types.Schema(
                    type=types.Type.STRING,
                )
            )
        },
    ),
)