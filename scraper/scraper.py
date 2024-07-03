from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import config
from scraper.utils import get_driver
import time
import logging
import requests


def scrape_public_url(payload):
    url = config.SCRAPER_URL
    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f"Failed to access url. Status code: {response.status_code}")

    driver = get_driver(True)

    form_elements = {
        'lastName': config.FORM_INPUT_0,
        'firstName': config.FORM_INPUT_1,
        'city': config.FORM_INPUT_10,
        'postalCode': config.FORM_INPUT_11,
    }
    form_button = config.FORM_SUBMIT_BUTTON
    table_to_read = config.FORM_TABLE
    pagination_html_elem = config.TABLE_PAGINATION
    page = 1
    try:
        driver.get(url)

        for param, value in payload.items():
            if param == 'page':
                page = value
            else:
                input_element = driver.find_element(By.ID, form_elements[param])
                input_element.send_keys(value)

        find_button = driver.find_element(By.ID, form_button)
        find_button.click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, table_to_read))
        )
        if page > 1:
            try:
                pagination = driver.find_element(By.CLASS_NAME, pagination_html_elem)
                page = pagination.find_element(By.XPATH, f".//a[span[text()='{page}']]")
                page.click()
                time.sleep(5)
            except Exception as e:
                logging.info(f"Error while clicking page number {page}: {e}")
                return False

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table')
        headers = [th.text for th in table.find('tr').find_all('th')]
        rows = table.find_all('tr')[1:]

        data = []
        for row in rows:
            cells = row.find_all('td')
            row_data = {headers[i]: cell.text for i, cell in enumerate(cells)}
            data.append(row_data)

        # save data to db
        logging.info(f"Data successfully saved to db")
    finally:
        driver.quit()
