from flask import Flask, render_template, request, redirect, send_file
from database import init_db, add_api, delete_api
from monitor import monitor_apis

import sqlite3
import threading
import schedule
import time
import pandas as pd

app = Flask(__name__)

# Initialize database
init_db()


@app.route('/')
def home():

    conn = sqlite3.connect('api_metrics.db')
    cursor = conn.cursor()

    # Search functionality
    search = request.args.get('search')

    if search:

        cursor.execute("""
        SELECT *
        FROM api_metrics
        WHERE api_name LIKE ?
        ORDER BY timestamp DESC
        """, ('%' + search + '%',))

    else:

        cursor.execute("""
        SELECT *
        FROM api_metrics
        ORDER BY timestamp DESC
        LIMIT 20
        """)

    metrics = cursor.fetchall()

    # Response Time Chart Data
    cursor.execute("""
    SELECT timestamp, response_time
    FROM api_metrics
    ORDER BY id DESC
    LIMIT 10
    """)

    chart_data = cursor.fetchall()

    # Dashboard Statistics
    cursor.execute("SELECT COUNT(*) FROM apis")
    total_apis = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM api_metrics")
    total_checks = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM api_metrics
    WHERE status_code = 200
    """)
    success = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM api_metrics
    WHERE status_code != 200
    """)
    failed = cursor.fetchone()[0]

    # Uptime Percentage
    if total_checks > 0:
        uptime = round((success / total_checks) * 100, 2)
    else:
        uptime = 0

    # Top 5 Slowest API Calls
    cursor.execute("""
    SELECT api_name,
           response_time,
           timestamp
    FROM api_metrics
    ORDER BY response_time DESC
    LIMIT 5
    """)

    slow_apis = cursor.fetchall()

    conn.close()

    chart_data.reverse()

    # Show only HH:MM on graph
    labels = [
        row[0].split(' ')[1][:5]
        for row in chart_data
    ]

    values = [
        row[1]
        for row in chart_data
    ]

    return render_template(
        'index.html',
        metrics=metrics,
        labels=labels,
        values=values,
        total_apis=total_apis,
        total_checks=total_checks,
        success=success,
        failed=failed,
        uptime=uptime,
        success_count=success,
        failed_count=failed,
        slow_apis=slow_apis
    )


@app.route('/add-api', methods=['GET', 'POST'])
def add_api_page():

    if request.method == 'POST':

        api_name = request.form['api_name']
        api_url = request.form['api_url']

        add_api(
            api_name,
            api_url
        )

        return redirect('/')

    return render_template('add_api.html')


@app.route('/report')
def report():

    conn = sqlite3.connect('api_metrics.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        AVG(response_time),
        MAX(response_time),
        MIN(response_time)
    FROM api_metrics
    """)

    stats = cursor.fetchone()

    conn.close()

    return render_template(
        'report.html',
        stats=stats
    )


@app.route('/run-monitor')
def run_monitor():

    monitor_apis()

    return redirect('/')


@app.route('/apis')
def api_list():

    conn = sqlite3.connect('api_metrics.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM apis
    """)

    apis = cursor.fetchall()

    conn.close()

    return render_template(
        'apis.html',
        apis=apis
    )


@app.route('/delete-api/<int:api_id>')
def delete_api_route(api_id):

    delete_api(api_id)

    return redirect('/apis')


@app.route('/export-csv')
def export_csv():

    conn = sqlite3.connect('api_metrics.db')

    query = """
    SELECT *
    FROM api_metrics
    ORDER BY timestamp DESC
    """

    df = pd.read_sql_query(query, conn)

    conn.close()

    csv_file = "metrics_report.csv"

    df.to_csv(
        csv_file,
        index=False
    )

    return send_file(
        csv_file,
        as_attachment=True
    )


# Background Scheduler
def scheduler_thread():

    schedule.every(1).minutes.do(
        monitor_apis
    )

    while True:

        schedule.run_pending()
        time.sleep(1)


threading.Thread(
    target=scheduler_thread,
    daemon=True
).start()


if __name__ == '__main__':
    app.run(debug=True)