
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    button_basket = None #заранее определяем, поскольку при провале поиска через WebDriverWait переменная не будет определена

    try:
        button_basket = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
        
        current_url = browser.current_url
        url_language = current_url.split('/')[3]

        assert browser.user_language in url_language,  f"Expected language in URL: {browser.user_language}, but get: {url_language}"
    except TimeoutException:
        assert button_basket is not None, "Button not defined"

    #pytest --language=es test_items.py