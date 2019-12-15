from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
from cloudant.query import Query
from cloudant.index import Index
from dotenv import load_dotenv
import os

load_dotenv()

client = Cloudant.iam(os.environ["USER_NAME"], os.environ["API_KEY"])
client.connect()

db_name = "order_list"
my_database = client.create_database(db_name)
if my_database.exists():
    print(f"'{db_name}' successfully created.")

sample_data = [
   [1, "coffee", 2],
   [2, "cake", 1],
   [3, "sandwich", 1]
 ]

for document in sample_data:
    json_document = {
     "userId": document[0],
     "menu": document[1],
     "value": document[2]
    }
    #
    # Create a document by using the database API.
    new_document = my_database.create_document(json_document)
    #
    # Check that the document exists in the database.
    if new_document.exists():
        print(f"Document '{document[0]}' successfully created.")

# result_collection = Result(my_database.all_docs, include_docs=True)
# Construct a Query
query = Query(my_database, selector={'userId': {'$eq': 2}})

for doc in query(limit=100)['docs']:
    print(doc)
    

try:
    client.delete_database(db_name)
except CloudantException:
    print(f"There was a problem deleting '{db_name}'.\n")
else:
    print(f"'{db_name}' successfully deleted.\n")

client.disconnect()
