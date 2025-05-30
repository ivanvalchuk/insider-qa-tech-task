import allure
from pytest import mark


@mark.mobile
@allure.title("Visit https://useinsider.com/ and check if the navigation menu is present for the mobile version")
def test_check_navigation(mobile_app):
  # Check if the navigation menu is present
  assert mobile_app.is_menu_button_visible, "Navigation menu not shown"
 
@mark.mobile
@allure.title("Check that all the navigation links are available in the navigation dropdown menu")
def test_check_nav_links(mobile_app):
  mobile_app.click_link("Toggle navigation")
  assert mobile_app.is_nav_link_visible(), "Navigation link not visible"
  mobile_app.click_link("Toggle navigation")

@mark.mobile
@allure.title("Check if the user gets redirected to the login page after clicking the Login button")
def test_check_redirection_to_login_page(mobile_app):
  # Accept the use of cookies
  mobile_app.click_button("Accept All")
  mobile_app.click_link("Toggle navigation")
  assert mobile_app.redirection_to_login_page("https://inone.useinsider.com/login"), "No redirection happens to Login page."