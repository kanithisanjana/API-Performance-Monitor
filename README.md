# 🚀 API Performance Monitor

A web-based API Performance Monitoring System built using **Flask**, **SQLite**, **Requests**, and **Chart.js**. The application continuously monitors APIs, tracks response times and status codes, stores historical metrics, and provides an interactive dashboard for performance analysis.

---

## 📌 Features

* ✅ Add and Manage APIs
* ✅ Automated API Monitoring
* ✅ Response Time Tracking
* ✅ Success vs Failure Analysis
* ✅ Uptime Percentage Monitoring
* ✅ Top 5 Slowest API Detection
* ✅ Search Monitoring Logs
* ✅ CSV Report Export
* ✅ Interactive Dashboard Charts
* ✅ SQLite Database Integration
* ✅ Real-Time Monitoring Dashboard
* ✅ Responsive and Modern UI

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask
* Requests
* SQLite

### Frontend

* HTML5
* CSS3
* Chart.js

### Data Processing

* Pandas

---

## 📂 Project Structure

```text
api-performance-monitor/
│
├── app.py
├── database.py
├── monitor.py
├── api_metrics.db
│
├── templates/
│   ├── index.html
│   ├── add_api.html
│   ├── report.html
│   └── apis.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/api-performance-monitor.git
cd api-performance-monitor
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### If PowerShell Blocks Activation

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install flask requests pandas schedule
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

```text
http://127.0.0.1:5000
```

---

## 📊 Dashboard Features

### Response Time Trend

Visualizes API response times using an interactive line chart.

### Success vs Failure Analysis

Displays API request success and failure distribution using a pie chart.

### Uptime Monitoring

Calculates API availability percentage based on successful requests.

### Top 5 Slowest API Calls

Identifies APIs with the highest response times.

### Monitoring Logs

Stores and displays historical API performance records.

### CSV Export

Exports collected monitoring data for further analysis.

---

## 🗄️ Database Schema

### APIs Table

| Column   | Type    |
| -------- | ------- |
| id       | INTEGER |
| api_name | TEXT    |
| api_url  | TEXT    |

### API Metrics Table

| Column        | Type     |
| ------------- | -------- |
| id            | INTEGER  |
| api_name      | TEXT     |
| api_url       | TEXT     |
| response_time | REAL     |
| status_code   | INTEGER  |
| timestamp     | DATETIME |

---

## 🔄 Monitoring Workflow

1. User adds APIs through the dashboard.
2. The monitoring engine periodically sends requests to registered APIs.
3. Response times and status codes are collected.
4. Metrics are stored in SQLite.
5. Dashboard visualizes performance insights.
6. Reports can be exported as CSV files.

---

## 📸 Screenshots

### Dashboard

Add a screenshot here:

```text
screenshots/dashboard.png
```

### Response Time Trend

Add a screenshot here:

```text
screenshots/response-time-chart.png
```

### Success vs Failure Chart

Add a screenshot here:

```text
screenshots/pie-chart.png
```

### Reports Page

Add a screenshot here:

```text
screenshots/reports.png
```

---

## 🎯 Learning Outcomes

* Flask Web Development
* REST API Monitoring
* SQLite Database Operations
* Data Visualization with Chart.js
* Scheduled Task Automation
* Dashboard Design
* CSV Report Generation
* Backend-Frontend Integration

---

## 🚀 Future Enhancements

* Email Alerts for API Failures
* User Authentication
* Multi-User Support
* API Response History Analytics
* Advanced Dashboard Filters
* Cloud Deployment (Render/AWS)

---

## 👩‍💻 Author

**Kanithi Sanjana**

Computer Science Engineering Student

---

## ⭐ If you found this project useful, consider giving it a star!
