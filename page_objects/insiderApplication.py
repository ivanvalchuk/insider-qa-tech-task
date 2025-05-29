import allure
from playwright.sync_api import Browser
from .insiderHomePage import HomePage
from .insiderQualityAssurancePage import QualityAssurancePage
from .insiderCareersPage import CareersPage

class App:
    def __init__(self, browser: Browser, base_url: str, **kwargs):
        self.browser = browser
        self.context = self.browser.new_context(**kwargs)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.insiderHomePage = HomePage(self.page)
        self.insiderQualityAssurancePage = QualityAssurancePage(self.page)
        self.insiderCareersPage = CareersPage(self.page)


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
    def hover_over(self, link: str):
        self.page.get_by_role("link", name = link).hover()
    
    @allure.step
    def check_if_redirection_happens_to_Lever_application_page(self, idx: int, url_name: str):
        with self.context.expect_page() as new_page_info:
            self.page.locator(f"#jobs-list > div:nth-child({idx+1}) > div > a").click()
        self.new_page = new_page_info.value
        return url_name in self.new_page.url
    
    def close(self):
        self.page.close()   
        self.context.close()