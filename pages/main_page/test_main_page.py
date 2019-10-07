from locators.locators import NewsletterLocators


class TestPage:

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        self.driver.get("https://www.housebrand.com/ho/en/")

    def input_mail(self, email):
        newsletter = NewsletterLocators
        self.driver.find_element(*newsletter.newsletter_input).send_keys(email)

    def click_checkbox(self):
        newsletter = NewsletterLocators
        self.driver.find_element(*newsletter.newsletter_checkbox).click()

    def push_signup_button(self):
        newsletter = NewsletterLocators
        self.driver.find_element(*newsletter.sign_newsletter_button).click()

    def get_incorrect_email_massage(self):
        newsletter = NewsletterLocators
        return self.driver.find_element(*newsletter.error_incorrect_email).text

    def get_checkbox_required_field(self):
        newsletter = NewsletterLocators
        return self.driver.find_element(*newsletter.checkbox_unfilled).text
