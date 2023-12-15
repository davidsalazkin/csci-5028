from dotenv import load_dotenv

load_dotenv()

from dataclasses import asdict

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify

from service import article_service

app = Flask(__name__)

sched = BackgroundScheduler(daemon=True)
sched.add_job(article_service.scrape_articles, 'interval', minutes=1)
sched.start()


@app.route('/fetch-articles', methods=['GET'])
def fetch_articles():
    response = article_service.fetch_articles_from_db()
    return jsonify([asdict(x) for x in response])


if __name__ == '__main__':
    app.run()
