import allure
from playwright.async_api import Page

class QualityAssurancePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def choose_location_from_dropdown(self, label: str):
        self.page.locator("#filter-by-location").select_option(label)
    
    @allure.step
    def choose_department_from_dropdown(self, label: str):
        self.page.locator("#filter-by-department").select_option(label)

    @allure.step
    def check_job_exists(self, idx: int, open_position: str):
        retreived_value = self.page.locator(f"#jobs-list > div:nth-child({idx+1}) > div > p").inner_text()
        return open_position == retreived_value
    
    @allure.step
    def check_position_contains(self, idx: int, position: str):
        retreived_value = self.page.locator(f"#jobs-list > div:nth-child({idx+1}) > div > p").inner_text()
        return position in retreived_value
    
    @allure.step
    def check_department_equals(self, idx: int, department: str):
        retreived_value = self.page.locator(f"#jobs-list > div:nth-child({idx+1}) > div > span").inner_text()
        return department == retreived_value
    
    @allure.step
    def check_location_equals(self, idx: int, location: str):
        retreived_value = self.page.locator(f"#jobs-list > div:nth-child({idx+1}) > div > div").inner_text()
        return location == retreived_value
