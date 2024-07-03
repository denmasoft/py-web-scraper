from flask import Flask, request, jsonify
from threading import Thread
import logging
from scraper.scraper import scrape_public_register

app = Flask(__name__)


@app.route('/scrape', methods=['POST'])
def scrape():
    payload = request.json
    page = request.args.get('page')
    if page:
        payload['page'] = page
    thread = Thread(target=scrape_public_register, args=(payload))
    thread.daemon = True
    thread.start()

    return jsonify({"status": "success", "message": "Scraping successfully started"}), 200
