# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright, Page
@pytest.fixture(scope="session")
def initialize_browser_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_button = page.get_by_test_id('registration-page-registration-button')
        email_input = page.locator("//input[@id=':r0:']")
        email_input.fill("user.name@gmail.com")
        username_input = page.locator("//input[@id=':r1:']")
        username_input.fill("username")
        password_input = page.locator("//input[@id=':r2:']")
        password_input.fill("password")

        registration_button.click()


        context.storage_state(path="browser-state.json")
        browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield page
    context.close()
    browser.close()