import os
from ddgs import DDGS
from scrapegraph_py import Client
from dotenv import load_dotenv




boxer_name = input("Enter the boxer's name: ")

def main(boxer_name):

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
            KOs (percentage of KOs), titles, most recent fight, upcoming fights, and wiki links in JSON format.
            """
        )
        return response
    except Exception as e:
        return {"error": f"Error scraping BoxRec: {str(e)}"}


print(main(boxer_name))
