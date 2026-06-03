# Starlink Daily Data Usage Web Scraper

## Project Description

This project is a web-based application that performs web scraping on the Starlink Usage Dashboard. The system extracts daily data usage information from the dashboard, stores the collected data in a CSV file, and presents the results through a user-friendly web interface.

The application was developed as part of a Systems Fundamentals web scraping assignment to demonstrate data extraction, data organization, CSV generation, and frontend presentation.

---

## Features

* Web-based User Interface (WebUI)
* Collect Data button to start scraping
* Automated browser control using Selenium
* Daily data usage extraction
* Data storage in CSV format
* Dashboard displaying usage statistics
* Table view of collected records
* Dark-themed responsive interface

---

## Technologies Used

### Backend

* Python
* Flask
* Selenium
* Pandas

### Frontend

* HTML
* CSS

---

## Project Structure

starlink-webscraper/

├── app.py

├── scraper.py

├── requirements.txt

├── README.md

├── starlink_usage.csv

├── templates/

│ └── index.html

└── static/

└── style.css

---

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/starlink-webscraper.git
```

2. Enter the project folder

```bash
cd starlink-webscraper
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## How to Use

1. Open the dashboard.
2. Click the **Collect Data** button.
3. A Chrome browser window will open.
4. Log in to your Starlink account.
5. Open the Usage Dashboard page.
6. Return to the terminal and press ENTER.
7. The scraper will collect daily data usage information.
8. The data will be saved as:

```text
starlink_usage.csv
```

9. The dashboard will display the collected records.

---

## CSV Output Format

Example:

```csv
Date,Data Usage (GB)
Nov 1,15.2
Nov 2,18.4
Nov 3,12.7
```

---

## Expected Output

The system generates:

* Daily usage records
* Total usage statistics
* Average usage statistics
* Peak usage statistics
* CSV file export

---

