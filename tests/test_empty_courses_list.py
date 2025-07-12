import pytest
from playwright.sync_api import expect, Page

from pages.courses_list_page import CoursesListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page_with_state: CoursesListPage):
    courses_list_page_with_state.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page_with_state.sidebar.check_visible()
    courses_list_page_with_state.sidebar.check_visible()
    courses_list_page_with_state.check_visible_courses_title()
    courses_list_page_with_state.check_visible_empty_view()
    courses_list_page_with_state.check_visible_create_course_button()




