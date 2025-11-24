from Tools.tools import (
    boxer_info,
    highlights_finder,
    get_boxer_image,
    get_news,
    sent_whatsapp,
    set_reminder,
    sent_whatsapp_reminder,
    get_fights
)
from google.genai import types



def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Function Calls:\n{function_call_part.name}({function_call_part.args})\n")
    else:
        print(f"Calling function :\n{function_call_part.name}\n")

    result= ""

    if function_call_part.name == "boxer_info":
        result = boxer_info( **function_call_part.args)

    if function_call_part.name == "highlights_finder":
        result = highlights_finder( **function_call_part.args)

    if function_call_part.name == "get_boxer_image":
        result = get_boxer_image( **function_call_part.args)

    if function_call_part.name == "get_news":
        result = get_news()

    if function_call_part.name == "sent_whatsapp":
        result = sent_whatsapp(**function_call_part.args)
        
    if function_call_part.name == "set_reminder":
        result = set_reminder(**function_call_part.args)

    if function_call_part.name == "sent_whatsapp_reminder":
        result = sent_whatsapp_reminder(**function_call_part.args)

    if function_call_part.name == "get_fights":
        result = get_fights(**function_call_part.args)

    if result =="":
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"error": f"Unknown function: {function_call_part.name}"},
        )
    ],
)
    else:
        return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"result":result},
        )
    ],
)