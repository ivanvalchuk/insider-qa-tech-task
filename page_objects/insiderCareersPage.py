import allure
from playwright.async_api import Page

class CareersPage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def check_locations_exist(self, name: str):
        return self.page.get_by_role("listitem").filter(has_text= name).is_visible()
    
    @allure.step
    def check_teams_exist(self, name: str):
        return self.page.get_by_role("heading", name= name).is_visible()
    
    @allure.step
    def retrieve_life_at_insider_section(self):
        return self.page.get_by_test_id("a8e7b90").is_visible()