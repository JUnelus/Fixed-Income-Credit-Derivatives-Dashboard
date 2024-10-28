import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up PostgreSQL connection details
db_params = {
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

# Risk monitoring based on price thresholds
def monitor_risk():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        query = """
            SELECT index_name, price, date
            FROM fixed_income_data
            WHERE price > (SELECT AVG(price) * 1.05 FROM fixed_income_data);
        """
        cur.execute(query)
        risk_entries = cur.fetchall()

        if risk_entries:
            print("High-risk entries found:")
            for row in risk_entries:
                print(f"Index: {row[0]}, Price: {row[1]}, Date: {row[2]}")
        else:
            print("No high-risk entries found.")

        cur.close()
    except Exception as e:
        print(f"Error during risk monitoring: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    monitor_risk()