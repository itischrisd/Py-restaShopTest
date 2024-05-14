from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options

from pages.account_page import AccountPage
from utils.screenshot import take_screenshot


def before_all(context):
    context.options = Options()
    context.options.add_argument("--start-maximized")
    context.options.add_argument("--disable-notifications")
    context.options.add_argument("--ignore-certificate-errors")
    context.options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome(options=context.options)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        take_screenshot(context.browser, scenario.name)
    try:
        AccountPage(context.browser).click_logout()
    except NoSuchElementException as e:
        print(f"Error during logout: {e}")
    finally:
        context.browser.quit()
