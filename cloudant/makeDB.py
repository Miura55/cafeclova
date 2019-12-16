import requests
from dotenv import load_dotenv
import os

params = (
    ('blocking', 'true'),
)

body = {
    "userId":"431",
    "menu":"マカロン",
    "value":4
}

response = requests.post(
            os.environ("URL")+"/order",
            json = body
        )
print(response.text)
