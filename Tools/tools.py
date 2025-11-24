

import os
from dotenv import load_dotenv
import sys
from ddgs import DDGS
from scrapegraph_py import Client
from google.genai import types
from datetime import datetime

from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
import time


#---------------------------------------------------------------------------

# Headhunter Tools test

#---------------------------------------------------------------------------

def boxer_info(boxer_name  ):
    load_dotenv()
    api_key = os.environ.get("SCRAPEGRAPH_API_KEY")
    ddgs = DDGS()
    results = ddgs.text(
            query = f'{boxer_name} Boxrec ', 
            region="us-en",
            max_results=5,
            safesearch="moderate")
    boxrec_url = ""
    for result in results:
        if result.get('href') and "boxrec.com" in result['href']:
            boxrec_url = result['href']
            break
        else:
            boxrec_url = "BoxRec profile not found."
    
    try:
        client = Client(api_key=api_key)
        response = client.smartscraper(
            website_url=boxrec_url,
            user_prompt="""
            GET full boxer profile including birth name, sex, age, nationality, stance,
            division, worldwide rank, USA rank, debuts, career, bouts, rounds, record,
            KOs (percentage of KOs), titles, most recent fight, upcoming fights, and wiki links in 
            formatted JSON format.
            Do not include the prompt in the response.
            """
        )
        return response
    except Exception as e:
        return {"error": f"Error scraping BoxRec: {str(e)}"}

    
def highlights_finder(boxer_name):
    ddgs = DDGS()
    results = ddgs.text(
        query=f'{boxer_name} career highlights on youtube', # 'query' is often 'keywords' in newer versions
        region="us-en",
        max_results=5, # Increased slightly to ensure we find YouTube links
        safesearch="moderate"
    )
    
    # List to store only the links
    youtube_links = []
    
    for i in results:
        url = i.get("href", "")
        # Check if 'youtube' is in the URL
        if "youtube" in url:
            youtube_links.append(url)
            
    return youtube_links

def get_boxer_image(boxer_name):
    ddgs = DDGS()
    results = ddgs.images(
        query=f'{boxer_name} boxing', # 'query' is often 'keywords' in newer versions
        region="us-en",
        max_results=5, # Increased slightly to ensure we find YouTube links
        safesearch="moderate"
    )
    
    # List to store only the links
    images = []
    
    image_results = [r['image'] for r in results]

            
    return image_results[0]

#---------------------------------------------------------------------------

# Smoke Detector Tools test

#---------------------------------------------------------------------------


def get_fights():

    load_dotenv()
    SCRAPEGRAPH_API_KEY = os.environ.get("SCRAPEGRAPH_API_KEY")
    client = Client(api_key=SCRAPEGRAPH_API_KEY)
    response = client.smartscraper(
        website_url="https://box.live/upcoming-fights-schedule/",
        user_prompt= f""" From the indicated websites get the 5 nearest upcoming fight. Make sure to take only 5 upcoming fights the closest  to the {datetime.now()}
        to save token and credits.
        Return it in a json with separate dictionnaries for each fights. Each dictionnary should have has charateristics the name of the fight (for example devin Haney vs brian Norman jr it should be : name: haney-vs-norman-jr),
        the date, the links and the community predictions.
        """
    )

    results =  response["result"]["fights"]
    final = []
    for i in results:
        if (i['community_predictions'] == None) or (i['community_predictions'] == []) or (i['community_predictions'] == 'Not Available'):
            i['community_predictions'] == None
            no_pred = [i['name'],i["links"]]
        else:
            final.append(i)
    return f""" Upcoming fight: {final}
                Fights with no pred: {no_pred} (to get the community predictions clicks the links)
"""



import time
import sys
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
try:
    import pywhatkit
except ImportError:
    pywhatkit = None

# Helper function to send the message
def sent_whatsapp_reminder(phone_number, fight_date_str):
    print(f"\n🥊 Triggering WhatsApp for +{phone_number}...")
    message = f"Reminder: The fight is tomorrow ({fight_date_str})! Don't miss it."
    
    # Ensure phone number has exactly one "+"
    if not phone_number.startswith("+"):
        phone_number = f"+{phone_number}"

    # Docker/Headless Check
    if os.environ.get("ENV") == "docker":
        print(f"🐳 [DOCKER MODE] Mocking WhatsApp send to {phone_number}: {message}")
        print("✅ Message sent successfully (Mocked).")
        return

    try:
        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=20, tab_close=True)
        print("✅ Message sent successfully.")
    except Exception as e:
        print(f"❌ Error sending message: {e}")

# Main reminder function
def set_reminder(fight_date, phone_number, hour, minute):
    try:
        # 1. CLEAN THE INPUT (This fixes your error)
        fight_date = fight_date.strip() 
        
        # 2. Calculate the Date
        fight_dt = datetime.strptime(fight_date, '%Y-%m-%d')
        
        # Calculate reminder time (Day before at 8:00 AM)
        reminder_time = fight_dt - timedelta(days=1)
        reminder_time = reminder_time.replace(hour=hour, minute=minute, second=0)

        # Safety check: Is the reminder time in the past?
        if reminder_time < datetime.now():
            print(f"❌ Error: The reminder time ({reminder_time}) has already passed.")
            return

        print(f"✅ Timer set for: {reminder_time}")
        print("⏳ Script is running... It will close automatically after sending the message.")

        # 3. Setup Scheduler
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            sent_whatsapp_reminder,  # Fixed function name here (was sent_whatsapp)
            'date', 
            run_date=reminder_time, 
            args=[phone_number, fight_date]
        )
        scheduler.start()

        # 4. Watchdog Loop
        while scheduler.get_jobs():
            time.sleep(1)

        print("👋 Job done. Shutting down script.")
        scheduler.shutdown()
        sys.exit()

    except ValueError as e:
        # This prints the REAL error from python so you can debug better
        print(f"❌ Date Error: {e}") 
        print("Please use format YYYY-MM-DD (e.g., 2025-11-23)")



#---------------------------------------------------------------------------

# The Plug Tools test

#---------------------------------------------------------------------------

def get_news():

    try:
        load_dotenv()
        api_key = os.environ.get("SCRAPEGRAPH_API_KEY")
        client = Client(api_key=api_key)
        response = client.smartscraper(
            website_url="https://www.espn.com/boxing/",
            user_prompt="""
            GET the last news about boxing take only the titles and the summauries for each news.
            """
        )
        return response
    except Exception as e:
        return {"error": f"Error scraping espn: {str(e)}"}

def sent_whatsapp(phone_number, message):
    print(f"\n📞 Sending WhatsApp to +{phone_number}...")

    phone_number = f"+{phone_number}"
    
    # Docker/Headless Check
    if os.environ.get("ENV") == "docker":
        print(f"🐳 [DOCKER MODE] Mocking WhatsApp send to {phone_number}: {message}")
        return "✅ Message sent successfully (Mocked)."

    try:
        # wait_time needs to be long enough for WhatsApp Web to load (20s is safe)
        pywhatkit.sendwhatmsg_instantly(
            phone_number, 
            message, 
            wait_time=15, 
            tab_close=True
        )
        return "✅ Message sent successfully." # Return this string so the AI sees it
    except Exception as e:
        return f"❌ Error sending message: {e}"




    



#---------------------------------------------------------------------------

# SCHEMA  FUNCTIONS

#---------------------------------------------------------------------------



#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#   FIRST AGENT

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

schema_boxer_info = types.FunctionDeclaration(
    name="boxer_info",
    description="scrape and return informations about boxer found on their boxrec profile.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "boxer_name": types.Schema(
                type=types.Type.STRING,
                description="The name of the boxer to research info for. It got to be an boxer ",
            ),
        },
    ),
)

schema_highlights_finder = types.FunctionDeclaration(
    name="highlights_finder",
    description="Look for the youtube highlights of the specified boxer",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "boxer_name": types.Schema(
                type=types.Type.STRING,
                description="The name of the boxer to research the highlights for. It got to be an boxer ",
            ),
        },
    ),
)


schema_get_boxer_image = types.FunctionDeclaration(
    name="get_boxer_image",
    description="Function that will get an links of an images for the specified boxer.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "boxer_name": types.Schema(
                type=types.Type.STRING,
                description="The name of the boxer to search the image for. It got to be an boxer ",
            ),
        },
    ),
)


#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#   SECOUND AGENT

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

schema_get_fights = types.FunctionDeclaration(
    name="get_fights",
    description="scrape box-live and give informations about upcoming fights their name, date and community_predictions and links",
    )


schema_sent_whatsapp_reminder = types.FunctionDeclaration(
    name="sent_whatsapp_reminder",
    description="Sent whatsapp reminder about the the fight day. Will be used only in the set_reminder.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "phone_number": types.Schema(
                type=types.Type.STRING,
                description="The phone number composed of the country_code + the actual number of the user. It should be asked",
            ),
            "fight_date": types.Schema(
                type=types.Type.STRING,
                description="The date of the fight we sent an reminder for. It should be asked",
            )
        },
    ),
)


schema_set_reminder = types.FunctionDeclaration(
    name="set_reminder",
    description="Schedules the reminder and KILLS the script once the message is sent. it will use the function sent_whatsapp_reminder ",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "fight_date": types.Schema(
                type=types.Type.STRING,
                description="The date of the fight we sent an reminder for. It should be asked ",
            ),
             "phone_number": types.Schema(
                type=types.Type.STRING,
                description="The complete number including the country code for the delivery of the reminder",
            ),
             "hour": types.Schema(
                type=types.Type.INTEGER,
                description="The hour for the reminder",
            ),
             "minute": types.Schema(
                type=types.Type.INTEGER,
                description="The minutes for the reminder",
            )
        },
    ),
)


#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#   THIRD AGENT

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------


schema_get_news = types.FunctionDeclaration(
    name="get_news",
    description="scrape and return latest informations about boxing. Only the title and the summary",
   
)


schema_sent_whatsapp = types.FunctionDeclaration(
    name="sent_whatsapp",
    description="Send the specified message to whatsapp to the user",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "message": types.Schema(
                type=types.Type.STRING,
                description="The text to send to whatsapp ",
            ),
            "phone_number": types.Schema(
                type=types.Type.STRING,
                description="The number of the user to send the message to"
                ),
        }, 
    ),
)

