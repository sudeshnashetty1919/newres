import os
import time
from datetime import datetime

from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.js_executor = driver
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.screenshot_name = f"screenshot_{self.timestamp}.png"
        self.img_upload_locator = (By.XPATH, "//input[@type='file']")
        self.toast_message_locator = (By.XPATH, "//span[contains(text(),'Your post was sent.')]")  # Adjust XPath as necessary
        self.post_button = (By.XPATH, "//button[@data-testid='tweetButtonInline' and .//span[text()='Post']]")

    email = (By.XPATH, "//input[@name='text']")
    next_button = (By.XPATH, "//span[contains(text(),'Next')]")
    pass_input = (By.XPATH, "//input[@type='password']")
    log_in = (By.XPATH, "//span[contains(text(),'Log in')]")
    log_out = (By.XPATH, "//span[contains(text(),'Log out @')]")
    toast_message = (By.XPATH, "//span[contains(text(),'Your post was sent.')]")
    post_content = (By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")

    user_name = (By.XPATH, "//div[@class='css-175oi2r r-1adg3ll r-bztko3']")
    logout_confirm = (By.XPATH, "//button[@data-testid='confirmationSheetConfirm']")
    notifications = (By.XPATH, "(//div[@class='css-175oi2r'])[4]")
    tagger_name = (By.XPATH, "//a[contains(@class, 'r-dnmrzs')]/div/span")
    screen_for_shot = (By.XPATH, "(//div[@class='css-175oi2r'])[16]")
    reply_button = (By.XPATH, "//button[@data-testid='reply']")
    img_upload = (By.XPATH, "//input[@type='file']")
    back_from_profile = (By.XPATH, "//button[@aria-label='Back']")
    reply_post = (By.XPATH, "//button[@data-testid='tweetButton']")

    def enter_email(self, email_id):
        email_element = self.driver.find_element(*self.email)
        email_element.send_keys(email_id)

    def enter_pass(self, password):
        pass_element = self.driver.find_element(*self.pass_input)
        pass_element.send_keys(password)

    def click_on_log_in(self):
        log_in_element = self.driver.find_element(*self.log_in)
        log_in_element.click()

    def enter_content(self, content):
        content_element = self.driver.find_element(*self.post_content)
        content_element.send_keys(content)

    def click_on_post(self):
        wait = WebDriverWait(self.driver, 30)
        post_button_element = wait.until(EC.element_to_be_clickable(self.post_button))
        post_button_element.click()

    def click_on_user_name(self):
        wait = WebDriverWait(self.driver, 10)
        user_name_element = wait.until(EC.presence_of_element_located(*self.user_name))
        self.driver.execute_script("arguments[0].scrollIntoView();", user_name_element)
        user_name_element.click()

    def log_out(self):
        log_out_element = self.driver.find_element(*self.log_out)
        log_out_element.click()

    def click_on_logout_confirm(self):
        logout_confirm_element = self.driver.find_element(*self.logout_confirm)
        logout_confirm_element.click()

    def toast_message(self):
        wait = WebDriverWait(self.driver, 10)
        toast_element = wait.until(EC.presence_of_element_located(self.toast_message_locator))
        print(toast_element.text)
        return toast_element.text

    def click_on_next(self):
        next_button_element = self.driver.find_element(*self.next_button)
        next_button_element.click()

    def click_on_notifications(self):
        notifications_element = self.driver.find_element(*self.notifications)
        notifications_element.click()

    def click_on_tagger_name(self):
        tagger_name_element = self.driver.find_element(*self.tagger_name)
        tagger_name_element.click()

    def click_on_back(self):
        back_element = self.driver.find_element(*self.back_from_profile)
        back_element.click()

    def click_on_reply(self):
        reply_element = self.driver.find_element(*self.reply_button)
        reply_element.click()

    def upload_screenshot(self):
        destination_file = os.path.join(os.getcwd(), "twitterBot", "screenshots", self.screenshot_name)
        wait = WebDriverWait(self.driver, 10)
        img_upload_element = wait.until(EC.presence_of_element_located(self.img_upload_locator))

        # Now you can call send_keys on the WebElement
        img_upload_element.send_keys(destination_file)

    def click_on_reply_post(self):
        wait = WebDriverWait(self.driver, 30)
        reply_post_element = wait.until(EC.element_to_be_clickable(self.reply_post))
        reply_post_element.click()

    def take_screenshot(self):
        try:
            # Assuming 'screenForShot' is a WebElement you want to take a screenshot of
            element = self.driver.find_element(*self.screen_for_shot)  # Replace with your actual element locator
            element_screenshot = element.screenshot_as_png  # Take screenshot as PNG

            # Create the destination directory if it doesn't exist
            screenshots_dir = os.path.join(os.getcwd(), "twitterBot", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Define the full path for the screenshot
            destination_file = os.path.join(screenshots_dir, self.screenshot_name)

            # Write the screenshot to the file
            with open(destination_file, 'wb') as file:
                file.write(element_screenshot)

            print(f"Screenshot saved as: {destination_file}")

        except WebDriverException as e:
            print("An error occurred while taking the screenshot:")
            print(e)

