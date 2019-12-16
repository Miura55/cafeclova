import requests

params = (
    ('blocking', 'true'),
)

body = {"db_name":"my_db"}

response = requests.post(
            args["URL"], 
            params=params, 
            auth=(args["API_KEY"], 'UVMn2vlj8HqCmPjg3QgCgLOIygYIL7hkfUBIEjoDGXKR100rdUyUsMRPRkeSUDjN'),
            json = body
        )
print(response.text)
