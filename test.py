from Tools.tools import (
    boxer_info,
    highlights_finder,
    get_boxer_image,
    sent_whatsapp_reminder,
    set_reminder,
    get_fights
)
import requests
from google.genai import types


'https://box.live/fights/clarke-vs-tshikeva/'




#---------------------------------------------------------------------------

# Headhunter Tools test

#---------------------------------------------------------------------------

# message = input("enter a message to send: ")
# date = input("enter a date to the format : YYYY-mm-dd: ")

# # print(boxer_info(boxer_name))

# # print(highlights_finder(boxer_name))

# # print(get_boxer_image(boxer_name))

# set_reminder(date, message)

print(get_fights())