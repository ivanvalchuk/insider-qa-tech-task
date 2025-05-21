import allure
from playwright.async_api import Page

class Leadership:
    def __init__(self, page: Page):
        self.page = page
    
    @allure.step
    def check_founders_exist(self, founder_name: str):
        self.page.get_by_role("heading", name="Our leadership team").wait_for()
        return self.page.get_by_text(founder_name).is_visible()