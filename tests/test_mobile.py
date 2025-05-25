import allure
from pytest import mark


@mark.mobile
@allure.title("1. Visit https://useinsider.com/ and check Insider home page is opened or not.")
def test_check_navigation(mobile_app):
  
  # Accept the use of cookies
  mobile_app.click_button("Accept All")
  # Check if the page is opened or not
  assert mobile_app.check_if_element_visible(selector= "#desktop_hero_24")

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
    assert mobile_app.check_locations_exist(location_name)

# check 'Teams' section
  mobile_app.click_link("See all teams")
  for team_name in team_names:
    assert mobile_app.check_teams_exist(team_name)

# check 'Life at Insider' section
  assert mobile_app.retrieve_element_by_testid(data_id= "a8e7b90")

@mark.mobile
@allure.title("3. Go to https://useinsider.com/careers/quality-assurance/, click “See all QA jobs”, filter jobs by Location - Istanbul, Turkey  " \
"and department - Quality Assurance, check presence of jobs list. " \
"4. Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, Location contains “Istanbul, Turkey. " \
"5. Click “View Role” button and check that this action redirects us to Lever Application form page.")
def test_check_quality_assurance_page(mobile_app):
    mobile_app.goto("/careers/quality-assurance")
    mobile_app.click_link(link= "See all QA jobs")

    # filter all jobs by location
    mobile_app.click_button("Filter")
    mobile_app.choose_from_dropdown(selector= "//select[@name='filter-by-location']", label= "Istanbul, Turkiye")
    
    # filter all jobs by department
    mobile_app.choose_from_dropdown(selector= "//select[@name='filter-by-department']", label= "Quality Assurance")
    
    # check presence of jobs list
    open_positions = "Senior Software Quality Assurance Engineer", "Software Quality Assurance Engineer"
    
    i = 1
    while i < len(open_positions) +1:
      assert mobile_app.check_value_equals(selector= f"#jobs-list > div:nth-child({i}) > div > p", value= open_positions[i-1])
      i += 1
    
    # Check that all jobs’ Position contains “Quality Assurance”, Department contains “Quality Assurance”, Location contains “Istanbul, Turkey.
    i = 1
    while i < len(open_positions) +1:

        assert mobile_app.check_value_contains(selector= f"#jobs-list > div:nth-child({i}) > div > p", value= "Quality Assurance")
        assert mobile_app.check_value_contains(selector= f"#jobs-list > div:nth-child({i}) > div > span", value= "Quality Assurance")
        assert mobile_app.check_value_contains(selector= f"#jobs-list > div:nth-child({i}) > div > div", value= "Istanbul, Turkiye")
        i += 1
        
    # "Click “View Role” button and check that this action redirects us to Lever Application form page.")
    i = 1
    while i < len(open_positions) +1:
    
      assert mobile_app.check_if_redirection_happens(selector= f"#jobs-list > div:nth-child({i}) > div > a", url_name= "https://jobs.lever.co/useinsider/")
      i += 1