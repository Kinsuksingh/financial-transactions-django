import requests
import json
import os

# Base URL for the API
BASE_URL = "http://127.0.0.1:8000/api/transactions/"

# Headers to specify the content type
HEADERS = {"Content-Type": "application/json"}

# Create the responses folder if it doesn't exist
if not os.path.exists('responses'):
    os.makedirs('responses')

# Function to save the response to a JSON file inside the 'responses' folder
def save_response_to_file(filename, response_data):
    filepath = os.path.join('responses', filename)
    with open(filepath, "w") as f:
        json.dump(response_data, f, indent=4)
        print(f"Response saved to {filepath}")

# 1. Create Transaction (POST)
def create_transaction():
    data = {
        "amount": 100.00,
        "transaction_type": "WITHDRAWAL",
        "user": 1
    }
    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(data))
    print("Create Transaction Response Code:", response.status_code)
    print("Raw Response Text:", response.text)
    try:
        response_json = response.json()
        save_response_to_file("create_transaction_response.json", response_json)
    except Exception as e:
        print("Error parsing JSON:", e)

# 2. Get All Transactions for User (GET)
def get_all_transactions_for_user():
    params = {"user_id": 1}
    response = requests.get(f"{BASE_URL}all/", headers=HEADERS, params=params)
    print("Get All Transactions Response Code:", response.status_code)
    print("Raw Response Text:", response.text)
    try:
        response_json = response.json()
        save_response_to_file("all_transactions_response.json", response_json)
    except Exception as e:
        print("Error parsing JSON:", e)

# 3. Get Specific Transaction by ID (GET)
def get_transaction_by_id(transaction_id):
    response = requests.get(f"{BASE_URL}{transaction_id}/", headers=HEADERS)
    print(f"Get Transaction {transaction_id} Response Code:", response.status_code)
    print("Raw Response Text:", response.text)
    try:
        response_json = response.json()
        save_response_to_file(f"transaction_{transaction_id}_response.json", response_json)
    except Exception as e:
        print("Error parsing JSON:", e)

# 4. Update Transaction Status (PUT)
def update_transaction_status(transaction_id):
    data = {
        "status": "COMPLETED"
    }
    response = requests.put(f"{BASE_URL}{transaction_id}/update/", headers=HEADERS, data=json.dumps(data))
    print(f"Update Transaction {transaction_id} Response Code:", response.status_code)
    print("Raw Response Text:", response.text)
    try:
        response_json = response.json()
        save_response_to_file(f"update_transaction_{transaction_id}_response.json", response_json)
    except Exception as e:
        print("Error parsing JSON:", e)

# Call the functions to test the API
if __name__ == "__main__":
    create_transaction()
    get_all_transactions_for_user()
    get_transaction_by_id(5)
    update_transaction_status(5)
