import re, allure
from playwright.async_api import Page


class Contact:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def validate_contact_form(self, validation_message: str):
        return self.page.locator("div").filter(has_text=re.compile(r'{}'.format(validation_message))).get_by_role("paragraph").is_visible()
    
    @allure.step
    def fill_text(self, controller_name, value: str):
        self.page.get_by_role("textbox", name = controller_name).fill(value)
    
    @allure.step
    def verify_correct_error_message(self, validation_message: str):
        return self.page.locator("form").filter(has_text=validation_message).is_visible()
    
    @allure.step
    def verify_form_was_not_sent(self, controller_name: str):
        return self.page.get_by_role("textbox", name = controller_name).input_value() is not None
   
    
        