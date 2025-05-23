import pytest
from playwright.sync_api import expect, Page

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses = page.get_by_test_id('courses-list-toolbar-title-text')
    icon = page.get_by_test_id('courses-list-empty-view-icon')
    results_text = page.get_by_test_id('courses-list-empty-view-title-text')
    results_description = page.get_by_test_id('courses-list-empty-view-description-text')

    expect(courses).to_be_visible()
    expect(courses).to_have_text('Courses')
    expect(results_text).to_have_text('There is no results')
    expect(results_description).to_have_text('Results from the load test pipeline will be displayed here')
