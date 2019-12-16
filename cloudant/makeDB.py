import requests
from dotenv import load_dotenv
import os

load_dotenv()

body = {
    "userId":"431",
    "menu":"マカロン",
    "value":5
}

response = requests.post(
            os.environ["URL"]+"/order",
            json = body
        )
print(response.text)
