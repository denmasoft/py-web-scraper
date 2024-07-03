from selenium import webdriver


def get_driver(headless=False):
    options = webdriver.ChromeOptions()
    options.binary_location = '/usr/bin/chromium-browser'
    options.add_experimental_option(
        "excludeSwitches", ["ignore-certificate-errors"])
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--enable-javascript")
    options.add_argument("--enable-cookies")
    if headless:
        options.add_argument('--headless')

    return webdriver.Chrome(options=options)
