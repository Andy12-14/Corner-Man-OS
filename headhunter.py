
import os
from call_functions import call_function
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from ddgs import DDGS
from scrapegraph_py import Client
from Tools.tools import (
    schema_boxer_info,
schema_highlights_finder,
schema_get_boxer_image

)

    


#--------------------------------------------------
# Main Function
#--------------------------------------------------------------

def run_headhunter(prompt):

    #system prompt
    system_prompt = """ You're an specialist when it comes to find an summarize informations about boxers.
    Your Name is headhunter as you can find infos about every boxer registered. to each answer you will add
    an little hook sentence saying your Name and why you're called that way in an short sentence.don't introduce yourself in a too formal way make it fun for the user.
    There's the list of functions you have to find informations about an asked boxer
    When a user asks about an boxer , make a function call plan. You can perform the following operations:

    - Scrape boxrec links of boxer to gets infos about them
    - You can get youtube highlights links of an boxer
    - You have the ability to get the link to an boxer image
    
    For each prompt that the user gonna make use this three operations for the first one make summaries the infos under
    two sections the first one is going to be the boxer general infos and the secound one are going to be about all the boxing
    aspect. At the end the user got to have an summary as a string of the boxer , his highlights on youtube (only one link) and his image(only one too).
    Make sure that the user gave you only boxer name and no other stuff don't even try to bother if he asked you something else

    IMPORTANT: Format your response using clear Markdown structure:
    ## General Info
    [Details here]
    
    ## Boxing Record
    [Details here]
    
    ## Highlights
    [Link here]
    
    ## Image
    [Link here]
    """

    load_dotenv()
    api_key = os.environ.get("Gemini_API_KEY")

    client = genai.Client(api_key=api_key)

    verbose = False
        
    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]
    available_functions = types.Tool(
    function_declarations=[
        schema_boxer_info,
        schema_highlights_finder,
        schema_get_boxer_image
    ]
)
    config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

    max_iters = 20
    for i in range(0, max_iters + 1):

        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=messages,
                config=config
            )
        except Exception as e:
            return f"Error: The AI service is currently overloaded or unavailable ({str(e)}). Please try again in a moment."

        if response is None or response.usage_metadata is None:
            return "Error: Response is malformed"
        
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

            return response.text
   


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a prompt as a command-line argument.")
        sys.exit(1)
    print(run_headhunter(sys.argv[1]))