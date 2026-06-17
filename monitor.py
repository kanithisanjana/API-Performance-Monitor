import requests
import time
from database import insert_metric
import sqlite3

def get_apis():

    conn = sqlite3.connect("api_metrics.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT api_name, api_url
    FROM apis
    """)

    data = cursor.fetchall()

    conn.close()

    return data

def monitor_apis():

    apis = get_apis()

    for api_name, api_url in apis:

        try:

            start = time.time()

            response = requests.get(
                api_url,
                timeout=5,
                headers={
                    "User-Agent":"API-Monitor"
                }
            )

            end = time.time()

            response_time = round(
                (end-start)*1000,
                2
            )

            insert_metric(
                api_name,
                api_url,
                response_time,
                response.status_code
            )

        except Exception:

            insert_metric(
                api_name,
                api_url,
                0,
                500
            )