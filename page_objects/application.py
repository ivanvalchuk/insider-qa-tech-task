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
    def click_link(self, label: str):
        self.page.get_by_role("link", name = label).click()

    @allure.step
    def click_link_by_locator(self, locator: str):
        self.page.locator(locator).click()
    
    @allure.step
    def click_textbox(self, locator: str):  
        return self.page.locator(locator).click()
    
    @allure.step
    def check_cookie_banner_not_exists(self):
        return self.page.get_by_role("dialog", name="cookieconsent").is_visible() is False

    @allure.step
    def check_if_page_opened(self, locator: str):
        return self.page.locator(locator).is_visible()
    
    @allure.step
    def hover_over(self, label: str):
        self.page.get_by_role("link", name = label).hover()
    
    @allure.step
    def check_items_exist(self, name: str):
        return self.page.get_by_text(name, exact= True).first.is_visible()
    
    @allure.step
    def check_value(self, name: str, text: str):
        return self.page.locator(name).filter(has_text= text).is_visible()

    @allure.step
    def check_if_redirection_happens(self, url_name: str):
        with self.context.expect_page() as new_page_info:
            self.page.get_by_role("link", name = "View Role").first.click()
        self.new_page = new_page_info.value
        return url_name in self.new_page.url

    @allure.step
    def check_text_in_section(self, name: str):
        return self.page.locator("section").filter(has_text = name).is_visible()
    
    @allure.step
    def choose_from_dropdown(self, locator: str, label: str):
        self.page.locator(locator).select_option(label)
    
    @allure.step
    def wait_for_load_state(self):
        self.page.wait_for_load_state('domcontentloaded')

    def close(self):
        self.page.close()   
        self.context.close()