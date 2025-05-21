import allure
from playwright.sync_api import Browser
from .leadership import Leadership
from .contact_us import Contact
from .locations import Location

class App:
    def __init__(self, browser: Browser, base_url: str, **kwargs):
        self.browser = browser
        self.context = self.browser.new_context(**kwargs)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.leadership = Leadership(self.page)
        self.contact_us = Contact(self.page)
        self.locations = Location(self.page)

    @allure.step
    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)
    
    @allure.step
    def hover_over(self, label: str):
        self.page.get_by_label("Header").get_by_role("link", name = label).hover()
       
    @allure.step
    def navigate_to(self, link: str):
        self.page.get_by_role("link", name = link).click()
   
    @allure.step
    def navigate_to_menu(self, menu: str):
        self.page.get_by_label("Header").get_by_role("link", name = menu).click()

    @allure.step
    def navigate_to_footer(self, menu: str):
        self.page.get_by_label("Footer").get_by_role("link", name = menu).click()
    
    @allure.step
    def click_button(self, button: str):
        self.page.get_by_role("button", name = button).click()

    @allure.step
    def wait_for_load_state(self):
        self.page.wait_for_load_state()
    
    @allure.step
    def check_cookie_banner_not_exists(self):
        return self.page.locator('css=.CookieConsent').is_visible() is False
        
    def close(self):
        self.page.close()   
        self.context.close()