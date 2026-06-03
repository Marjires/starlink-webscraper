from flask import Flask, render_template, jsonify, send_file
from scraper import scrape_starlink
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

TIMESTAMP_FILE = "last_scraped.txt"


def get_last_scraped():
    if os.path.exists(TIMESTAMP_FILE):
        with open(TIMESTAMP_FILE, "r") as f:
            return f.read().strip()
    return None


@app.route("/")
def home():

    records = []

    if os.path.exists("starlink_usage.csv"):

        try:

            df = pd.read_csv("starlink_usage.csv")

            df = df.drop_duplicates(
                subset=["Date"]
            )

            records = df.to_dict(
                orient="records"
            )

        except Exception as e:
            print(e)

    return render_template(
        "index.html",
        records=records,
        last_scraped=get_last_scraped()
    )


@app.route("/last-scraped")
def last_scraped():

    return jsonify({
        "timestamp": get_last_scraped()
    })


@app.route("/collect", methods=["POST"])
def collect():

    try:

        df = scrape_starlink()

        records = df.to_dict(
            orient="records"
        )

        timestamp = datetime.now().strftime(
            "%Y-%m-%dT%H:%M:%S"
        )

        with open(TIMESTAMP_FILE, "w") as f:
            f.write(timestamp)

        return jsonify({
            "status": "success",
            "count": len(records),
            "records": records,
            "timestamp": timestamp
        })

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/download")
def download():

    return send_file(
        "starlink_usage.csv",
        as_attachment=True
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )