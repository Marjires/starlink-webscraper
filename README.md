# Starlink Daily Data Usage Web Scraper

## Project Description

This project is a web-based data scraping application developed using **Python, Selenium, Flask, Pandas, HTML, CSS, and JavaScript**.

The application automatically extracts **daily Starlink data usage information** from the Starlink dashboard, stores the collected data in a CSV file, and displays the results through an interactive analytics dashboard.

The system provides usage statistics, insights, and downloadable reports for easier monitoring and analysis of Starlink network consumption.

---

## Features

* Automated Starlink data scraping using Selenium
* Daily data usage extraction
* CSV report generation
* CSV download functionality
* Interactive Flask Web User Interface (WebUI)
* Analytics dashboard
* Usage statistics and insights
* Daily usage table display
* Peak and lowest usage monitoring

---

## Analytics Dashboard

The dashboard automatically calculates and displays:

* Total Data Usage (GB)
* Average Daily Usage (GB)
* Peak Usage (GB)
* Lowest Usage (GB)
* Highest Usage Day
* Lowest Usage Day
* Total Days Tracked
* Usage Pattern Classification (Low, Normal, Heavy)

---

## Technologies Used

### Backend

* Python
* Flask
* Selenium
* Pandas
* WebDriver Manager

### Frontend

* HTML
* CSS
* JavaScript

### Data Storage

* CSV File

---

## Project Structure

```text
starlink-webscraper/
│
├── app.py
├── scraper.py
├── requirements.txt
├── README.md
├── starlink_usage.csv
├── last_scraped.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## Installation Guide

### Step 1: Download the Project

Clone the repository:

```bash
git clone https://github.com/Marjires/starlink-webscraper.git
```

Or download the ZIP file and extract it.

---

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

Ensure the following folders exist:

```text
templates/
static/
```

Place:

```text
index.html
```

inside:

```text
templates/
```

and

```text
style.css
```

inside:

```text
static/
```

---

### Step 3: Install Dependencies

Open Terminal and run:

```bash
pip install -r requirements.txt
```

If the requirements file is unavailable:

```bash
pip install flask selenium pandas webdriver-manager
```

---

### Step 4: Run the Application

Open Terminal and run:

```bash
python app.py
```

---

### Step 5: Open the Web Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

### Step 6: Collect Starlink Data

Click:

```text
Collect Data
```

The Selenium browser will open automatically.

---

### Step 7: Login to Starlink

Use the provided credentials:

**Email**

```text
fundamentalssystem@gmail.com
```

**Password**

```text
systemfundamentals2026
```

After logging in:

1. Complete the authentication process.
2. Wait for the scraper to navigate to the usage dashboard.
3. Allow the scraper to collect all available daily usage records.
4. Wait until the CSV file is generated.

---

### Step 8: View Dashboard Results

The dashboard displays:

* Daily Usage Records
* Total Usage
* Average Usage
* Peak Usage
* Lowest Usage
* Usage Insights
* Number of Days Tracked

---

### Step 9: Download CSV Report

Click:

```text
Download CSV
```

to download the generated report.

The file will be saved as:

```text
starlink_usage.csv
```

---

## CSV Output Format

Example:

| Date   | Data Usage (GB) |
| ------ | --------------- |
| May 17 | 22.83           |
| May 18 | 18.45           |
| May 19 | 9.46            |
| May 20 | 16.38           |

---

## Sample Output

### Web Dashboard

Displays:

* Usage Analytics
* Data Insights
* Daily Usage Breakdown
* Downloadable CSV Report

### CSV Export

Exports collected Starlink data into:

```text
starlink_usage.csv
```

for analysis using:

* Microsoft Excel
* Google Sheets
* LibreOffice Calc
* Data Analytics Tools

---

## Author

**Margaret Sanay**

Bachelor of Science in Information Technology
