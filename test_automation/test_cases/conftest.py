
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
profile=webdriver.FirefoxProfile()
foption=webdriver.FirefoxOptions()
from webdriver_manager.firefox import GeckoDriverManager
#foption.headless=True
profile.accept_untrusted_certs=True
profile.accept_untrusted_certs_issuer=False
profile.set_preference("dom.webnotifications.enabled",False)

@pytest.fixture
def setup(request):
    driver=webdriver.Firefox(profile,executable_path=GeckoDriverManager().install(),options=foption)
    driver.get('https://www.yatra.com/')
    driver.maximize_window()
    sleep(2)
    driver.implicitly_wait(30)
    request.cls.driver=driver
    yield
    driver.close()
