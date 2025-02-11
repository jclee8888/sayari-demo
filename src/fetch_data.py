import os
from dotenv import load_dotenv
from sayari.client import Sayari

load_dotenv()

client = Sayari(
    client_id = os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
)

resolution = client.resolution.resolution(name="Victoria Beckham")

print(resolution)

# client = sayari(
#     client.id = 
# )