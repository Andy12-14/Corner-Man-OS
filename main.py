
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from call_function import call_function

def main():

    load_dotenv()
    api_key = os.environ.get("Gemini_API_KEY")

    client = genai.Client(api_key=api_key)

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Write to a file (create or update)
- Read the content of a file
- Run a Python file with optional arguments

When the user asking about code project they are reffering to the working directory.
So check the project files and figuring out how to run the project and how to run the tests , you'll always want to test the tests and the actual project
to verify that behavior is working

All paths you provide should be relative to the working directory.
You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    if len(sys.argv) < 2:
        print("Please provide a prompt as a command-line argument.")
        sys.exit(1)
    prompt = sys.argv[1]
    verbose = False
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose = True
    
        
    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_write_file,
        schema_get_file_content,
        schema_run_python_file
    ]
)
    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

    max_iters = 20
    for i in range(0, max_iters + 1):

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages,
            config=config

        )

        if response is None or response.usage_metadata is None:
            print("response is malformed")
            return
        
        if verbose:
            print()
            print("Usage Metadata:\n")
            print(f"user prompt: {prompt}")
            print(f"prompt tokens used: {response.usage_metadata.prompt_token_count}")
            print(f"response tokens used: {response.usage_metadata.candidates_token_count}")
            print()


        if response.candidates:
            for candidates in response.candidates:
                if candidates is None or candidates.content is None:
                    continue 
                messages.append(candidates.content)

        if response.function_calls:
            for function_call_part in response.function_calls:
                result = call_function(function_call_part, verbose)
                messages.append(result)
                
        else:

            print(response.text)
            return
   


main()