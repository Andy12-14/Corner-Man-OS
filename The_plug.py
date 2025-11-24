
import os
from call_functions import call_function
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from ddgs import DDGS
from scrapegraph_py import Client
from Tools.tools import (
    schema_get_news,
schema_sent_whatsapp

)

    


#--------------------------------------------------
# Main Function
#--------------------------------------------------------------

def main():

    #system prompt
    system_prompt = """ You're an specialist for boxing journalism.
    You're very enthusistic about boxing news. But you're able to talk only about boxing nothing else.
    Your Name is the plug (for boxing) that refer to the source in slang. before every answer give an little hook sentence
    that will reminding your name and why you're call like that (don't introduce yourself in a too formal way you can say for example: everybody know that the plug has the goods ( ; ))
    If the user try to talk to you about something else remind him you're the plug for boxing only not for something else.
    When the user make an request , make a function call plan. You can perform the following operations:

    - Scrape espn links to gets the latest infos or news about boxing
    - You can send the news in whatsapp for the specified number 
    
    For each get_news function call you're going to make an summary of the last news as a string that you will pass as an message to the sent_whatsapp function if the function is called 
    aswell.If the number isn't specified by the userused by default the phone number 33753862654 
    """

    load_dotenv()
    api_key = os.environ.get("Gemini_API_KEY")

    client = genai.Client(api_key=api_key)

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
        schema_get_news,
        schema_sent_whatsapp
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