from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.locator("//input[@id=':r0:']")
    email_input.fill("user.name@gmail.com")

    username_input = page.locator("//input[@id=':r1:']")
    username_input.fill("username")

    password_input = page.locator("//input[@id=':r2:']")
    password_input.fill("password")

    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    dashboard_text = page.locator("//h6[@data-testid='dashboard-toolbar-title-text']")
    expect(dashboard_text).to_have_text("Dashboard")

    page.wait_for_timeout(5000)