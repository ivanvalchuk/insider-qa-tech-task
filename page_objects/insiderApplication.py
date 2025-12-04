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
    def click_button_cookie_layer(self, name):
        self.page.locator(f".cli-bar-btn_container >> text={name}").click()
    
    @allure.step
    def click_button(self, name):
        self.page.locator(f".btn-outline-secondary.rounded >> text={name}").click()
    
    @allure.step
    def hover_over_nav_link(self, name: str):
        self.page.locator(f"#navbarNavDropdown >> text={name}").hover()
    
    @allure.step
    def navigate_to(self, name: str):
        self.page.locator(f".dropdown-sub >> text={name}").click(force=True)
    
    @allure.step
    def redirection_to_lever_application_page(self, idx: int, url_name: str):
        with self.context.expect_page() as new_page_info:
            self.page.locator(f".position-list-item:nth-child({idx+1}) .btn").click()
        self.new_page = new_page_info.value
        return url_name in self.new_page.url
    
    @allure.step
    def is_menu_button_visible(self):
        return self.page.locator("[aria-label='Toggle navigation']").is_visible()
    
    @allure.step
    def click_menu_button(self):
        return self.page.locator("[aria-label='Toggle navigation']").click()
    
    @allure.step
    def is_nav_link_visible(self):
        whyInsiderLink = self.page.locator("#navbarNavDropdown >> text='Why Insider'").is_visible()
        platformLink = self.page.locator("#navbarNavDropdown >> text='Platform'").is_visible()
        solutionsLink = self.page.locator("#navbarNavDropdown >> text='Solutions'").is_visible()
        customersLink = self.page.locator("#navbarNavDropdown >> text='Customers'").is_visible()
        resourcesLink = self.page.locator("#navbarNavDropdown >> text='Resources'").is_visible()
        companyLink = self.page.locator("#navbarNavDropdown >> text='Company'").is_visible()
        return whyInsiderLink and platformLink and solutionsLink and customersLink and resourcesLink and companyLink

    @allure.step
    def redirection_to_login_page(self, url_name: str):
        with self.context.expect_page() as new_page_info:
            self.page.locator("#navbarNavDropdown >> text='Login'").click()
        self.new_page = new_page_info.value
        return url_name == self.new_page.url
    
    def close(self):
        self.page.close()   
        self.context.close()