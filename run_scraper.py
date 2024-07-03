from scraper.scraper import scrape_public_url
from threading import Thread

thread = Thread(target=scrape_public_url, args=([]))
thread.daemon = True
thread.start()
