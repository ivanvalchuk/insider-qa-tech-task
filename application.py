import allure
from playwright.sync_api import Browser

class App:
    def __init__(self, browser: Browser, base_url: str, **kwargs):
        self.browser = browser
        self.context = self.browser.new_context(**kwargs)
        self.page = self.context.new_page()
        self.base_url = base_url

    @allure.step
    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)
    
    
    @allure.step
    def click_button(self, button: str):
        self.page.get_by_role("button", name = button).click()
    
    @allure.step
    def click_link(self, link: str):
        self.page.get_by_role("link", name = link).click()

    @allure.step
    def check_if_element_visible(self, selector: str):
        return self.page.locator(selector).is_visible()
    
    @allure.step
    def hover_over(self, link: str):
        self.page.get_by_role("link", name = link).hover()
    
    @allure.step
    def check_locations_exist(self, name: str):
        return self.page.get_by_role("listitem").filter(has_text= name).is_visible()
    
    @allure.step
    def check_teams_exist(self, name: str):
        return self.page.get_by_role("heading", name= name).is_visible()
    
    @allure.step
    def check_value_equals(self, selector: str, value: str):
        retreived_value = self.page.locator(selector).inner_text()
        return value == retreived_value
    
    @allure.step
    def check_value_contains(self, selector: str, value: str):
        retreived_value = self.page.locator(selector).inner_text()
        return value in retreived_value
    
    @allure.step
    def check_if_redirection_happens(self, selector: str, url_name: str):
        with self.context.expect_page() as new_page_info:
            self.page.locator(selector).click()
        self.new_page = new_page_info.value
        return url_name in self.new_page.url
    

    @allure.step
    def retrieve_element_by_testid(self, data_id:str):
        return self.page.get_by_test_id(data_id).is_visible()
    
    @allure.step
    def choose_from_dropdown(self, selector: str, label: str):
        self.page.locator(selector).select_option(label= label)

    def close(self):
        self.page.close()   
        self.context.close()