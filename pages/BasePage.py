import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class BasePage:
    driver = None

    @staticmethod
    def initialize_web_driver():
        if BasePage.driver is None:
            try:
                BasePage.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
                BasePage.driver.maximize_window()
                BasePage.driver.implicitly_wait(60)
                BasePage.driver.get("https://x.com/i/flow/login")
            except Exception as e:
                print(f"Error initializing WebDriver: {e}")
                raise  # Re-raise the exception to fail the test
        return BasePage.driver

    @staticmethod
    def quit_driver():
        if BasePage.driver is not None:
            BasePage.driver.quit()
            BasePage.driver = None

@pytest.fixture(scope='module')
def setup_driver():
    # Setup WebDriver
    driver = BasePage.initialize_web_driver()
    yield driver  # This allows tests to run
    # Teardown WebDriver
    BasePage.quit_driver()

def test_login_page(setup_driver):
    driver = setup_driver
    driver.get("https://x.com/i/flow/login")
    # Add your test logic here
    #assert "Login" in driver.title  # Example assertion
