import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):

    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru/en and other")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})


    if user_language != None:
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.user_language = user_language
    else:
        raise pytest.UsageError("--language must be selected")
    yield browser
    print("\nquit browser..")
    browser.quit()