import pytest

from pages.main_page.test_main_page import TestPage


@pytest.mark.usefixtures('setup')
class TestNewsletter:

    def test_correct_email_input(self):
        test_newsletter = TestPage(self.driver)
        test_newsletter.open_main_page()
        test_newsletter.input_mail("")
        test_newsletter.click_checkbox()
        test_newsletter.push_signup_button()

    def test_incorrect_email_input(self):
        test_newsletter = TestPage(self.driver)
        test_newsletter.open_main_page()
        test_newsletter.input_mail("")
        test_newsletter.click_checkbox()
        test_newsletter.push_signup_button()
        assert "EMAIL ADDRESS IS INCORRECT" in test_newsletter.get_incorrect_email_massage()

    def test_checkbox_off(self):
        test_newsletter = TestPage(self.driver)
        test_newsletter.open_main_page()
        test_newsletter.input_mail("")
        test_newsletter.push_signup_button()
        assert "THIS FIELD IS REQUIRED" in test_newsletter.get_checkbox_required_field()
