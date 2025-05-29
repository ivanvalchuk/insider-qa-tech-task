import allure
from pytest import mark


@mark.mobile
@allure.title("1. Visit https://useinsider.com/ and check Insider home page is opened or not.")
def test_check_navigation(mobile_app):
  
  # Accept the use of cookies
  mobile_app.click_button("Accept All")
  # Check if the page has opened or not
  assert mobile_app.insiderHomePage.check_if_page_visible(), "Insider home page was not opened."

@mark.mobile
@allure.title("2. Select “Company” menu in navigation bar, select “Careers” and check Career page, its Locations, Teams and Life at Insider blocks are opened or not.")
def test_check_career_page(mobile_app):
  mobile_app.click_link("Toggle navigation")
  mobile_app.click_link("Company")
  mobile_app.click_link("Careers")
  location_names = "New York", "Sao Paulo", "London", "Paris", "Amsterdam", "Helsinki", "Warsaw", "Sydney", "Dubai", "Tokyo", "Seoul", "Singapore", "Bangkok", \
                    "Jakarta", "Taipei", "Manila", "Kuala Lumpur", "Ho Chi Minh City", "Istanbul", "Ankara", "Mexico City", "Lima", "Buenos Aires", "Bogota",
  
  team_names = "Customer Success", "Sales", "Product & Engineering", "Finance & Business Support", "Marketing", "CEO’s Executive Office", "Purchasing & Operations",\
                "People and Culture", "Business Intelligence", "Security Engineering", "Partnership", "Quality Assurance", "Mobile Business Unit", "Partner Support Development",\
                "Product Design"

# check 'Locations' section 
  for location_name in location_names:
    assert mobile_app.insiderCareersPage.check_locations_exist(location_name), f"Location {location_name} is missing."

# check 'Teams' section
  mobile_app.click_link("See all teams")
  for team_name in team_names:
    assert mobile_app.insiderCareersPage.check_teams_exist(team_name), f"Team {team_name} is missing."

# check 'Life at Insider' section
    assert mobile_app.insiderCareersPage.retrieve_life_at_insider_section(), "Insider section is missing."

@mark.mobile
@allure.title("3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”, filter jobs by Location - Istanbul, Turkey  " \
"and department - Quality Assurance, check presence of jobs list. " \
"4. Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, Location contains “Istanbul, Turkey. " \
"5. Click “View Role” button and check that this action redirects us to Lever Application form page.")
def test_check_quality_assurance_page(mobile_app):
  mobile_app.goto("/careers/quality-assurance")
  mobile_app.click_link("See all QA jobs")

  # filter all jobs by location
  mobile_app.click_button("Filter")
  mobile_app.insiderQualityAssurancePage.choose_location_from_dropdown("Istanbul, Turkiye")
    
  # filter all jobs by department
  mobile_app.insiderQualityAssurancePage.choose_department_from_dropdown("Quality Assurance")
    
  # check presence of jobs list
  open_positions = "Senior Software Quality Assurance Engineer", "Software Quality Assurance Engineer"
    
  for idx, open_position in enumerate(open_positions):
    assert mobile_app.insiderQualityAssurancePage.check_job_exists(idx, open_position), f"Open position for {open_position} is missing."
    # Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, Location contains “Istanbul, Turkey.
    assert mobile_app.insiderQualityAssurancePage.check_position_contains(idx, "Quality Assurance"), f'Position {open_position} contains no "Quality Asurance"'
    assert mobile_app.insiderQualityAssurancePage.check_department_equals(idx, "Quality Assurance"), f'There is no department "Quality Asurance" under position {open_position}'
    assert mobile_app.insiderQualityAssurancePage.check_location_equals(idx, "Istanbul, Turkiye"), f'There is no location "Istanbul, Turkiye" under position {open_position}'
      # "Click “View Role” button and check that this action redirects us to Lever Application form page.")
    assert mobile_app.check_if_redirection_happens_to_Lever_application_page(idx, "https://jobs.lever.co/useinsider/"), "No redirection happens to Lever application page."