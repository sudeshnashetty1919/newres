import time
import unittest
from behave import given, when, then
from pages.BasePage import BasePage
from pages.LoginPage import LoginPage


@given("user is on login page")
def step_user_on_login_page(context):
    context.login_page = LoginPage(BasePage.initialize_web_driver())

@when("user enters {username} and clicks on next and {password}")
def step_user_enters_credentials(context, username, password):
    time.sleep(5)
    context.login_page.enter_email(username)
    context.login_page.click_on_next()
    context.login_page.enter_pass(password)

@when("user clicks on login")
def step_user_clicks_login(context):
    context.login_page.click_on_log_in()

@when("user clicks on post")
def step_user_clicks_post(context):
    time.sleep(5)
    context.login_page.click_on_post()

@then("user should get a toast {message}")
def step_user_gets_toast_message(context, message):
    toast_message = context.login_page.toast_message()
    assert toast_message == message

@then("user clicks on logout")
def step_user_clicks_logout(context):
    context.login_page.click_on_user_name()
    context.login_page.log_out()
    context.login_page.click_on_logout_confirm()
    BasePage.quit_driver()

@when("user takes a screenshot")
def step_user_takes_screenshot(context):
    time.sleep(5)
    context.login_page.take_screenshot()

@when("user clicks on reply")
def step_user_clicks_reply(context):
    time.sleep(5)
    context.login_page.click_on_reply()
    time.sleep(5)
    context.login_page.upload_screenshot()
    time.sleep(5)

@when("posts the screenshot")
def step_user_posts_screenshot(context):
    time.sleep(5)
    context.login_page.click_on_reply_post()

@when("user clicks on notifications and opens the account")
def step_user_clicks_notifications_and_opens_account(context):
    time.sleep(5)
    context.login_page.click_on_notifications()  # Use the correct attribute
    time.sleep(5)
    context.login_page.click_on_tagger_name()  # Use the correct method


@when("click back")
def step_click_back(context):
    context.login_page.click_on_back() # Assuming you have defined this method in your LoginPage class

@when("clicks on reply")
def step_clicks_on_reply(context):
    time.sleep(5)
    context.login_page.click_on_reply()  # Assuming you have defined this method in your LoginPage class
    context.login_page.upload_screenshot()  # Assuming you have defined this method in your LoginPage class
    time.sleep(5)  # Wait for 5 seconds (consider using WebDriverWait instead)
@when('user types {content}')
def enter_content_for_post(context, content):
    context.login_page.enter_content(content)