import requests
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up PostgreSQL connection details
db_params = {
    'database': os.getenv('POSTGRES_DB_NAME'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT')
}

# RapidAPI configuration
RAPIDAPI_HOST = "apidojo-yahoo-finance-v1.p.rapidapi.com"
querystring = {"symbol":"AMRN","region":"US","lang":"en-US","straddle":"true"}
RAPIDAPI_KEY = os.getenv('RAPIDAPI_KEY')
API_URL = f"https://{RAPIDAPI_HOST}/stock/v3/get-options"

headers = {
    "X-RapidAPI-Host": RAPIDAPI_HOST,
    "X-RapidAPI-Key": RAPIDAPI_KEY
}


# Fetch data from RapidAPI
def fetch_data():
    response = requests.get(API_URL, headers=headers, params=querystring)
    if response.status_code == 204:
        print("No content available from the API.")
        return {}
    elif response.status_code != 200:
        print(f"Error fetching data: {response.status_code}, {response.text}")
        return {}
    try:
        return response.json()
    except ValueError:
        print("Error parsing JSON response")
        return {}


# Store data in PostgreSQL
def store_data(data):
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        # Assuming data contains fixed income indices
        for item in data.get('results', []):
            query = """
                INSERT INTO fixed_income_data (index_name, price, date)
                VALUES (%s, %s, %s)
                ON CONFLICT (index_name, date) DO UPDATE
                SET price = EXCLUDED.price;
            """
            cur.execute(query, (item['index_name'], item['price'], item['date']))

        conn.commit()
        cur.close()
    except Exception as e:
        print(f"Error storing data: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    data = fetch_data()
    if data:
        store_data(data)