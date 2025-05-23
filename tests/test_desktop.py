import allure
from pytest import mark


@mark.desktop
@allure.title("1. Visit https://useinsider.com/ and check Insider home page is opened or not.")
def test_check_navigation(desktop_app):
  
  # Accept the use of cookies
  desktop_app.click_button("Accept All")
  # Check if the page is opened or not
  assert desktop_app.check_if_page_opened("#desktop_hero_24")

@mark.desktop
@allure.title("2. Select “Company” menu in navigation bar, select “Careers” and check Career page, its Locations, Teams and Life at Insider blocks are opened or not.")
def test_check_career_page(desktop_app):

  desktop_app.hover_over("Company")
  desktop_app.click_link_by_locator('css=.dropdown-sub >> text="Careers"')
#   desktop_app.click_link("Careers")
  location_names = "New York", "Sao Paulo", "London", "Paris", "Amsterdam", "Helsinki", "Warsaw", "Sydney", "Dubai", "Tokyo", "Seoul", "Singapore", "Bangkok", \
                    "Jakarta", "Taipei", "Manila", "Kuala Lumpur", "Ho Chi Minh City", "Istanbul", "Ankara", "Mexico City", "Lima", "Buenos Aires", "Bogota", "Santiago"
  
  team_names = "Customer Success", "Sales", "Product & Engineering", "Finance & Business Support", "Marketing", "CEO’s Executive Office", "Purchasing & Operations",\
                "People and Culture", "Business Intelligence", "Security Engineering", "Partnership", "Quality Assurance", "Mobile Business Unit", "Partner Support Development",\
                "Product Design"

# check 'Locations' section 
  for location_name in location_names:
    assert desktop_app.check_items_exist(location_name)

# check 'Teams' section
  desktop_app.click_link("See all teams")
  for team_name in team_names:
    assert desktop_app.check_items_exist(team_name)

# check 'Life at Insider' section
  assert desktop_app.check_text_in_section("Life at Insider We’re here to")

@mark.desktop
@allure.title("3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”, filter jobs by Location - Istanbul, Turkey  " \
"and department - Quality Assurance, check presence of jobs list. " \
"4. Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, Location contains “Istanbul, Turkey. " \
"5. Click “View Role” button and check that this action redirects us to Lever Application form page.")
def test_check_quality_assurance_page(desktop_app):
    desktop_app.goto("/careers/quality-assurance")
    desktop_app.click_link("See all QA jobs")

    #This is needed because of the poor hydration of the page. 
    #This means that the data is not yet fetched to be checked in the next steps.
    desktop_app.wait_for_load_state()

    # filter all jobs by location
    desktop_app.choose_from_dropdown(locator= "//select[@name='filter-by-location']", label= "Istanbul, Turkiye")
    
    # filter all jobs by department
    desktop_app.choose_from_dropdown(locator= "//select[@name='filter-by-department']", label= "Quality Assurance")

    # check presence of jobs list
    open_positions = "Senior Software Quality Assurance Engineer", "Software Quality Assurance Engineer"
    for open_position in open_positions:
      assert desktop_app.check_items_exist(open_position)
    
    i = 1
    while i < len(open_positions) +1:

        assert desktop_app.check_value(f"#jobs-list > div:nth-child({i}) > div > p", "Quality Assurance")
        assert desktop_app.check_value(f"#jobs-list > div:nth-child({i}) > div > span", "Quality Assurance")
        assert desktop_app.check_value(f"#jobs-list > div:nth-child({i}) > div > div", "Istanbul, Turkiye")
        i+=1
        
    # "Click “View Role” button and check that this action redirects us to Lever Application form page.")
    assert desktop_app.check_if_redirection_happens("https://jobs.lever.co/useinsider/")