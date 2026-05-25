from flask import Flask, render_template
from scraper import scrape_starlink

app = Flask(__name__)


@app.route('/')

def home():

    df = scrape_starlink()

    records = df.to_dict(orient='records')

    return render_template(
        'index.html',
        records=records
    )


if __name__ == '__main__':
    app.run(debug=True)