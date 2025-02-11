import os
from dotenv import load_dotenv
from sayari.client import Sayari

load_dotenv()

client = Sayari(
    client_id = os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
)

# Fetch company details
def fetch_company_profile(company):

    try:
        # print(f"Fetching data for {company}")
        response = client.search.search_entity_get(limit=1, q=company)

        if response.data:
            # print(f"response.data[0]: {response.data[0]}")
            print(f"fetch_data passed for {company}")
            return response.data[0]
        else:
            print(f"No Sayari records found for {company}")
            return None

    except Exception as e:
        print(f"Error fetching data for {company}: {e}")
        return None

