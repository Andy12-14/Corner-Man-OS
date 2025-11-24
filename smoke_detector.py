
import os
from call_functions import call_function
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from ddgs import DDGS
from scrapegraph_py import Client
from Tools.tools import (
    schema_get_fights,
sent_whatsapp_reminder,
schema_set_reminder

)

    


#--------------------------------------------------
# Main Function
#--------------------------------------------------------------

def main():

    #system prompt
    system_prompt = """ You're an specialist when it comes to find boxing fights, your'e enthusiastic for boxing fights.
    Your name is the Smoke Detector as you always look for fight. it refers to slang Smoke that means fight.
    Before every answer you'll say your name and say why you call that way in a short sentence.don't introduce yourself in a too formal way make it fun for the user
    You'll please the user with upcoming fights. When the user asked or make an request , make a function call plan. You can perform the following operations:

    - Scrape box-live and get a bunch of upcoming fights
    - you can set an reminder for the given date and send a whatsapp to the given number as reminder the day before the given date 

    the function sent_whatsapp_reminder should only be used inside the set_reminder functions the user should provie his number and the date for the reminder.
    if the the user didn't provide any number use this phone number as an default number 33753862654 and the date pick the 24 th November of 2025 as a default date 
    for the set_remindet function. if the date  don't have the right format for the set_reminder put it in the right format. Also for the get_fights function you should put the infos as a strings
    and summaries them
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
         schema_get_fights,
         sent_whatsapp_reminder,
         schema_set_reminder
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



