from scraper.scraper import scrape_public_register
from threading import Thread

thread = Thread(target=scrape_public_register, args=([]))
thread.daemon = True
thread.start()
