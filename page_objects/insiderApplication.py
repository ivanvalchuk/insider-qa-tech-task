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
        self.page.wait_for_load_state()
    
    @allure.step
    def redirection_to_lever_application_page(self, idx: int, url_name: str):
        with self.context.expect_page() as new_page_info:
            self.page.locator(f"#jobs-list > div:nth-child({idx+1}) > div > a").click()
        self.new_page = new_page_info.value
        return url_name in self.new_page.url
    
    @allure.step
    def is_menu_button_visible(self, label: str):
        return self.page.get_by_role("link", name= "Toggle navigation").is_visible()
    
    @allure.step
    def is_nav_link_visible(self):
        whyInsiderLink = self.page.get_by_role("link", name = "Why Insider").is_visible()
        platformLink = self.page.locator("#navbarNavDropdown").get_by_role("link", name = "Platform").is_visible()
        solutionsLink = self.page.get_by_role("link", name = "Solutions").is_visible()
        customersLink = self.page.get_by_role("link", name = "Customers", exact = True).is_visible()
        resourcesLink = self.page.locator("#navbarNavDropdown").get_by_role("link", name = "Resources").is_visible()
        companyLink = self.page.get_by_role("link", name = "Company").is_visible()
        companyLink = self.page.get_by_role("link", name = "Explore Insider").is_visible()
        loginButton = self.page.get_by_role("link", name = "Login").is_visible()
        getDemoButton = self.page.locator("#desktop_hero_24").get_by_role("link", name = "Get a Demo").is_visible()
        loginButton = self.page.get_by_role("link", name = "Login").is_visible()
        englishButton = self.page.get_by_role("link", name = "English").is_visible()

        return whyInsiderLink and platformLink and solutionsLink and customersLink and resourcesLink and companyLink and \
                loginButton and getDemoButton and englishButton

    @allure.step
    def redirection_to_login_page(self, url_name: str):
        with self.context.expect_page() as new_page_info:
            self.page.get_by_role("link", name="Login").click()
        self.new_page = new_page_info.value
        return url_name == self.new_page.url
    
    def close(self):
        self.page.close()   
        self.context.close()