# Fixed-Income-Credit-Derivatives-Dashboard
This project will focus on pulling real-time or recent historical data on trending fixed income indices from a financial API.

## Overview
This project demonstrates operational support for Fixed Income Credit Derivative trading. It includes:
- **Data Ingestion** from RapidAPI into PostgreSQL.
- **Reconciliation** checks to identify discrepancies.
- **Risk Monitoring** to highlight high-risk events.
- A **Dashboard** for reporting.

## Project Structure
- `data_ingestion.py`: Fetches data and loads it into PostgreSQL.
- `reconciliation.py`: Performs data reconciliation checks.
- `risk_monitoring.py`: Monitors risk based on price thresholds.
- `dashboard.ipynb`: Jupyter notebook for data visualization and reporting.

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up a PostgreSQL database and add the credentials to an `.env` file.
4. Run the scripts in order.

## Requirements
- Python 3.x
- PostgreSQL
- RapidAPI account
- Python libraries: requests, psycopg2, pandas, matplotlib

## Usage
- Run `data_ingestion.py` to fetch and store data.
- Run `reconciliation.py` to check for discrepancies.
- Run `risk_monitoring.py` to identify high-risk trades.
- Use `dashboard.ipynb` to view the dashboard and generate reports.