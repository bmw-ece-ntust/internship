import requests
import json
import os

def put_request(policyTypeId, url_base, json_file):
    # Get the path to the JSON file in the same directory
    json_file_path = os.path.join(os.path.dirname(__file__), json_file)
    
    # Read the JSON data from the file
    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    url = f"{url_base}/{policyTypeId}"
    headers = {
        "Content-Type": "application/json"
    }
    
    # Update the policy_type_id in the JSON data
    json_data["policy_type_id"] = policyTypeId
    
    response = requests.put(url, headers=headers, data=json.dumps(json_data))
    
    if response.status_code == 200:
        print("Success!")
        print("Response data:", response.json())
    else:
        print(f"Failed with status code: {response.status_code}")
        print("Response text:", response.text)

# Base URL and policy type ID
url_base = "http://192.168.106.157:8000/a1mediator/A1-P/v2/policytypes"
policyTypeId = input("Enter the policy type ID: ")

# Perform the PUT request
put_request(policyTypeId, url_base, 'payload.json')
