import re, allure
from playwright.async_api import Page


class Location:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def check_locations_exist(self, location_name: str):
        self.page.get_by_role("heading", name="Primary Offices").wait_for()
        return self.page.get_by_text(location_name).first.is_visible()