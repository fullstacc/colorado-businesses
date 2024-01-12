import os
import requests
from supabase import create_client, Client
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# supabase setup
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_SERVICE_ROLE_KEY')
supabase = create_client(url, key)

# Get the app token from the environment variables
app_token = os.getenv('APP_TOKEN')

def connect_to_api(endpoint: str) -> dict:
    headers = {'X-App-Token': app_token}
    # Append the parameter to the endpoint URL
    endpoint += "?entityid=18881009142"
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def handler():
    # Endpoint for the Colorado data source
    api_endpoint = os.getenv('API_ENDPOINT')

    try:
        # Connect to the API
        response = connect_to_api(api_endpoint)
        print("Successfully connected to the API.")
        print("Example response body:")
        print(response)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'your_function_name' with the actual name you want to use
# This is the entry point for the serverless function
if __name__ == 'fetch-and-update':
    handler()
