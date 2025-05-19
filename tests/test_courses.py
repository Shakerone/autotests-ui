from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():  # Создаем тестовую функцию
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()  # Создание контекста
        page = context.new_page()  # Создание страницы

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        registration_button = page.get_by_test_id('registration-page-registration-button')
        expect(registration_button).to_be_disabled()

        email_input = page.locator("//input[@id=':r0:']")
        email_input.fill("user.name@gmail.com")
        username_input = page.locator("//input[@id=':r1:']")
        username_input.fill("username")
        password_input = page.locator("//input[@id=':r2:']")
        password_input.fill("password")
        expect(registration_button).to_be_enabled()
        registration_button.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser-state.json')
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses = page.get_by_test_id('courses-list-toolbar-title-text')
        icon = page.get_by_test_id('courses-list-empty-view-icon')
        results_text = page.get_by_test_id('courses-list-empty-view-title-text')
        results_description = page.get_by_test_id('courses-list-empty-view-description-text')

        expect(courses).to_be_visible()
        expect(courses).to_have_text('Courses')
        expect(results_text).to_have_text('There is no results')
        expect(results_description).to_have_text('Results from the load test pipeline will be displayed here')



