import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        email_input = page.get_by_test_id("registration-form-email-input").locator('input')
        email_input.fill("user.name@gmail.com")

        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        username_input.fill("username")

        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        password_input.fill("password")

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser-state.json')

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        header_coursers = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(header_coursers).to_be_visible()
        expect(header_coursers).to_have_text('Courses')

        result_courses = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(result_courses).to_be_visible()
        expect(result_courses).to_have_text('There is no results')

        icon_block = page.get_by_test_id('courses-list-empty-view-icon')
        # expect(icon_block).not_to_be_hidden()
        expect(icon_block).to_be_attached()
        expect(icon_block).to_be_visible()

        description_block = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(description_block).to_be_visible()
        expect(description_block).to_have_text('Results from the load test pipeline will be displayed here')