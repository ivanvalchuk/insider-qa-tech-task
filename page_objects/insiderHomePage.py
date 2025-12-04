import allure
from playwright.async_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page

        
    @allure.step
    def is_home_page_visible(self):
        return self.page.locator("#desktop_hero_24").is_visible()