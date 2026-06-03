from flask import Flask, render_template, redirect
from scraper import scrape_starlink

app = Flask(__name__)

records = []

@app.route('/')
def home():

    total = 0
    avg = 0
    peak = 0

    if len(records) > 0:

        usages = [
            float(row["Data Usage (GB)"])
            for row in records
        ]

        total = round(sum(usages), 2)
        avg = round(total / len(usages), 2)
        peak = max(usages)

    return render_template(
        "index.html",
        records=records,
        total=total,
        avg=avg,
        peak=peak,
        days=len(records)
    )


@app.route('/collect-data', methods=['POST'])
def collect_data():

    global records

    df = scrape_starlink()

    records = df.to_dict(
        orient='records'
    )

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
