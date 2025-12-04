import allure
from pytest import mark


@mark.desktop
@allure.title("1. Visit https://useinsider.com/ and check Insider home page is opened or not.")
def test_check_navigation(desktop_app):

  # Accept the use of cookies
  desktop_app.click_button_cookie_layer("Accept All")
  # Check if the page has opened or not
  assert desktop_app.insiderHomePage.is_home_page_visible(), "Insider home page was not opened."

@mark.desktop
@allure.title("2. Select “Company” menu in navigation bar, select “Careers” and check Career page, its Locations, Teams and Life at Insider blocks are opened or not.")
def test_check_career_page(desktop_app):

  desktop_app.hover_over_nav_link("Company")
  desktop_app.navigate_to("Careers")

  # Check if the page has opened or not
  assert desktop_app.insiderCareersPage.is_careers_page_visible(), "Careers' page was not opened."

  location_names = "New York", "Sao Paulo", "London", "Paris", "Amsterdam", "Helsinki", "Warsaw", "Sydney", "Dubai", "Tokyo", "Seoul", "Singapore", "Bangkok", \
                    "Jakarta", "Taipei", "Manila", "Kuala Lumpur", "Ho Chi Minh City", "Istanbul", "Ankara", "Mexico City", "Lima", "Buenos Aires", "Bogota", "Santiago"
  
  team_names = "Customer Success", "Sales", "Product & Engineering", "Finance & Business Support", "Marketing", "CEO’s Executive Office", "Purchasing & Operations",\
                "People and Culture", "Business Intelligence", "Security Engineering", "Partnership", "Quality Assurance", "Mobile Business Unit", "Partner Support Development",\
                "Product Design"

# check 'Locations' section 
  for location_name in location_names:
    assert desktop_app.insiderCareersPage.check_locations_exist(location_name), f"Location {location_name} is missing."

# check 'Teams' section
  desktop_app.click_button("See all teams")
  for team_name in team_names:
    assert desktop_app.insiderCareersPage.check_teams_exist(team_name), f"Team {team_name} is missing."

# check 'Life at Insider' section
  assert desktop_app.insiderCareersPage.retrieve_life_at_insider_section(), "Insider section is missing."

@mark.desktop
@allure.title("3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”, filter jobs by Location - Istanbul, Turkey  " \
"and department - Quality Assurance, check presence of jobs list. " \
"4. Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, Location contains “Istanbul, Turkey. " \
"5. Click “View Role” button and check that this action redirects us to Lever Application form page.")
def test_check_quality_assurance_page(desktop_app):
  desktop_app.goto("/careers/quality-assurance")
  desktop_app.click_button("See all QA jobs")
    
  # filter all jobs by location
  desktop_app.insiderQualityAssurancePage.choose_location_from_dropdown("Istanbul, Turkiye")
    
  # filter all jobs by department
  desktop_app.insiderQualityAssurancePage.choose_department_from_dropdown("Quality Assurance")

  # check presence of jobs list
  open_positions = "Software Quality Assurance Engineer (Remote)",
    
  for idx, open_position in enumerate(open_positions):
    assert desktop_app.insiderQualityAssurancePage.check_job_exists(idx, open_position), f"Open position for {open_position} is missing."
    # Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, Location contains “Istanbul, Turkey.
    assert desktop_app.insiderQualityAssurancePage.check_position_contains(idx, "Quality Assurance"), f'Position {open_position} contains no "Quality Asurance"'
    assert desktop_app.insiderQualityAssurancePage.check_department_equals(idx, "Quality Assurance"), f'There is no department "Quality Asurance" under position {open_position}'
    assert desktop_app.insiderQualityAssurancePage.check_location_equals(idx, "Istanbul, Turkiye"), f'There is no location "Istanbul, Turkiye" under position {open_position}'
    # "Click “View Role” button and check that this action redirects us to Lever Application form page.")
    assert desktop_app.redirection_to_lever_application_page(idx, "https://jobs.lever.co/useinsider/"), "No redirection happens to Lever application page."