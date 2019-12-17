import requests
from dotenv import load_dotenv
import os

load_dotenv()
response = requests.get(
            os.environ["URL"]+"/confilm?userId={}".format(os.environ["ID"])
        )
print(response.json())
