import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_btn(browser):
    browser.get(link)
    # Wait to see page language
    time.sleep(5)
    try:
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))
        found = True
    except:
        found = False

    assert found, 'Element not found'
