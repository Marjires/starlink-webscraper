# Starlink Daily Data Usage Web Scraper

## Project Description

This project is a web scraping application developed using Python, Selenium, Flask, and Pandas.

The application extracts daily Starlink data usage information from the Starlink dashboard, displays the results in a web interface, and exports the data into a CSV file for further analysis.

---

## Features

- Automated Starlink data scraping
- Daily data usage extraction
- CSV file export
- Flask Web User Interface (WebUI)
- Data displayed in a table format

---

## Technologies Used

- Python
- Selenium
- Flask
- Pandas
- WebDriver Manager
- HTML
- CSS

---

## Project Structure

```
starlink-webscraper/
│
├── app.py
├── scraper.py
├── requirements.txt
├── README.md
├── starlink_usage.csv
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

add templates and static folder then move the html and css file to designated folder.
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

### Step 6: Login to Starlink

When the automated browser opens:

1. Enter your Starlink email address fundamentalssystem@gmail.com
2. Enter your Starlink password      systemfundamentals2026
3. Complete login
4. Wait for the scraper to collect data

---

### Step 7: View Results

The application will display:

- Date
- Data Usage (GB)

inside the web interface.

---

### Step 8: Exported CSV

After scraping is complete, the application automatically creates:

```text
starlink_usage.csv
```

The CSV file contains:

| Date | Data Usage (GB) |
|------|----------------|
| May 17 | 22.83 |
| May 18 | 18.45 |

---

## Output

### Web Interface

Displays daily Starlink data usage in a table.

### CSV Export

Exports daily data usage into:

```text
starlink_usage.csv
```

for analysis in Excel or other spreadsheet software.

---

## Author

Margaret Sanay
