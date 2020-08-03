import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help='choose language: --language=es|fr|ru')
    parser.addoption('--browser',
                     action='store',
                     default='chrome',
                     help='choose browser: --browser=chrome|firefox')


@pytest.fixture(scope='function')
def browser(request):
    _language = request.config.getoption('language')
    _browser = request.config.getoption('browser')
    
    if _browser == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': _language})
        browser = webdriver.Chrome(options=options)
    elif _browser == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', _language)
        browser = webdriver.Firefox(firefox_profile=fp)
    
    yield browser
    browser.quit()
