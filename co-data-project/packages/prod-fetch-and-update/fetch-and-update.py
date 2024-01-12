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

def fetch_data_from_api(endpoint: str) -> list:
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()

def upsert_data_to_supabase(data: list, table: str) -> None:
    # Upsert data to Supabase table
    response = supabase.table(table).upsert(data, on_conflict='entityid')
    if response.get('error'):
        raise Exception(response['error'])

def handler():
    # Endpoint for the Colorado data source
    api_endpoint = os.getenv('API_ENDPOINT')
    
    # Name of the table in Supabase
    table_name = os.getenv('TABLE_NAME')

    try:
        # Fetch data from the API
        dataset = fetch_data_from_api(api_endpoint)

        # Upsert data to Supabase
        upsert_data_to_supabase(dataset, table_name)
        print("Data has been successfully upserted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'your_function_name' with the actual name you want to use
# This is the entry point for the serverless function
if __name__ == 'fetch-and-update':
    handler()
