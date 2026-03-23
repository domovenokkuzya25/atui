import pytest
from playwright.sync_api import expect, Page
from pages.registration_page import RegistrationPage
from fixtures.pages import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.fill_registration_form(email='username@gmail.com', username='username', password='password')
    registration_page.click_registration_button()
    dashboard_page.check_dashboard_title()
