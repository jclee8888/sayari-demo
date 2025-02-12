import os
from dotenv import load_dotenv
from sayari.client import Sayari

load_dotenv()

client = Sayari(
    client_id = os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
)

# Fetch company details using Sayari aPI
def fetch_company_profile(company):

    # request to Sayari
    try:
        response = client.search.search_entity_get(limit=1, q=company)

        # extract first result from returned data
        if response.data:
            print(f"fetch_data passed for {company}")
            return response.data[0]

        # if no result, return none
        print(f"No Sayari records found for {company}")
        return None

    # error handling
    except Exception as e:
        print(f"Error fetching data for {company}: {e}")
        return None
