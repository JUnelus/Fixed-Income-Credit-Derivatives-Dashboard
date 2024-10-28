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

# Reconciliation logic
def reconcile_data():
    try:
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()

        query = """
            SELECT index_name, COUNT(*)
            FROM fixed_income_data
            GROUP BY index_name
            HAVING COUNT(*) > 1;
        """
        cur.execute(query)
        discrepancies = cur.fetchall()

        if discrepancies:
            print("Discrepancies found:")
            for row in discrepancies:
                print(f"Index: {row[0]}, Count: {row[1]}")
        else:
            print("No discrepancies found.")

        cur.close()
    except Exception as e:
        print(f"Error during reconciliation: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    reconcile_data()