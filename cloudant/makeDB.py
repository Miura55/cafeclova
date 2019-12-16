from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.query import Query
from cloudant.index import Index
from dotenv import load_dotenv
import os, time

load_dotenv()

client = Cloudant.iam(os.environ["USER_NAME"], os.environ["API_KEY"])
client.connect()

db_name = "order_list"
my_database = client.create_database(db_name)
while True:
    time.sleep(1)
    if my_database.exists():
        print(f"'{db_name}' successfully created.")
        break

