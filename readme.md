## > 3 years experienced candidates:

### 1. Describe the steps for comprehensively testing of a pencil with an eraser on one end. Cases for all types of testing (such as functional, usability, performance, load, stress, security, etc.) are expected here.

### Preconditions: let's assume it's a simple pencil with an eraser and it's made of wood, since no additional information is specified.

### Functional testing:
 - Make sure that the pencil can draw.
 - Make sure the pencil can draw through a carbon paper.
 - Make sure that the pencil writes smoothly, the lines are even and do not leave smudges.
 - The lead does not break or crumble directly during drawing.
 - Make sure that the pencil can draw not only on paper but also on but on alternative materials (cardboard, wood, walls, or floor (relevant for construction work).
 - Check whether the eraser erases notes/sketches and does not smear or make it “dirty”.
 - During and after sharpening, the lead did not break its integrity.
 - During and after sharpening, the pencil does not break or crumble.
 - The sharpened pencil is successfully functioning (you can write, sketch, draw).

### Usability Testing
- Is it comportable to hold a pencil? 
- Does it not slip, nor does it fall out when using it?
- Does it squeak while writing or does it write quietly?
- How useful is the eraser on the end of the pencil?
- The body shape is round, triangular, or hexagonal.
- Pencil sharpens easily with a pencil sharpener.

### Security Testing
 - Can I get hurt with a pencil (scratched, cut when sharpening)?
 - Is it safe to give a pencil to a child? There are “safe” types of pencils (for example, special “children” pencils, often with a triangular body) that can be given to children without fear (of course, depending on age, general development, and characteristics of the child).
 - Is the pencil safe for people with disabilities (eg visually impaired)? E.g. a pencil with a round body can pose a serious problem for a visually impaired person when rolled under a table. For the visually impaired the use of pencils with a hexagonal or triangular barrel is more appropriate.

### Load Testing
- Let’s check the behavior of the pencil when you press the pencil lead on the paper. Make sure the pencil won’t break.
- Pull the pencil lead. It must not come out of the body.
- Tap the pencil on the table several times. The lead should not crumble or break, fall out of the body, or crack.
- After use, the eraser does not leave crumbs, does not fall out; the ferrule does not bend or leave marks or scratches on paper and hands. 

### Stress Testing
- Drop the pencil on the floor a couple of times and check whether the lead breaks or crumbles. The pencil body must not be damaged.
- Try to bend the pencil: will it break or not?
- Chew on a pencil. It’s advisable that the end of the pencil stays not “eaten”. Many manufacturers pay special attention to this point.
- Place the pencil in water, then dry it. It should be possible to use it normally for drawing / writing as before.
- Place the pencil in the freezer for a while to freeze it. It should be possible to use it normally for drawing / writing as before.
- Use the eraser to rigorously to erase notes / sketches. The eraser head should not wear off quickly.

### Performance Testing
- Check that the pencil lead does not wear off, nor does it thin quickly while drawing / writing.
- Check that the eraser head does not wear off quickly while erasing notes / sketches written by the pencil.

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## The test cases have been automated using Playwright and Pytest using the Page Object Model for better maintainability.
## Below are the instructions on how to install the required libraries and run the tests.

### Installation instructions
1. Download the latest Python version from https://www.python.org/downloads and install it (if not installed).
2. Download the latest version of Git from https://git-scm.com/downloads and install it (if not installed).
3. Install the Pytest plugin using pip install "pytest-playwright".
4. Install the Pytest browsers with "playwright install".

### Repository setup
1. Clone the repository from https://github.com/ivanvalchuk/ui-automation-task.git
2. "cd" to the folder "ui-automation-task".
3. The tests are located as follows:
- "./tests/test_desktop.py" contains test cases for running on Desktop.
- "./tests/test_mobile.py" contains test cases for running on Mobile.
4. Page objects can be found under the "./page_objects" folder.
5. Pytest fixtures can be checked under the "./conftest.py" folder.


### Running intstructions
- "pytest" - runs the tests on both Desktop browsers and mobile.
- "pytest -m desktop" - runs the tests on Desktop browsers (e.g. Chromium).
- "pytest -m mobile" - runs the tests on emualated mobile devices (e.g. iPhone 15).
- "pytest -m desktop --lf" / "pytest -m mobile --lf" - re-runs the previous failed tests for Desktop / Mobile.
By default, the tests are run in the 'headless' mode and on Chromium browser on Desktop and iPhone 15. In order to change to the 'headed'  mode, please change this in "./pytest.ini" by setting 'headless' to 'False'. Adding support for other browsers (Firefox, Webkit)
can be done in the "./conftest" file by adding them to the params of the corresponding fixtures, e.g. params = ['firefox', 'webkit', 'Galaxy S9'], params = ['iPhone 14', 'Pixel 7'].

### Automated test scenarios:

1. Founders 
- Hover over “About us” and go to “Leadership”.
- Check Founders' section (check if all 3 founders names are displayed).

2. Contact Form Validation
- Check that required fields trigger validation errors.
- Test invalid inputs (e.g. wrong email format) and verify correct error messages.

Candidate-Defined Scenarios:

1. Consent to use of cookies
- Click on on the "I understand" button on the cookie consent banner to accept the use of cookies.
- Check if the use of cookies can be accepted.

2.  Check if the 'Contact us' form is protected by reCAPTCHA and cannot be submitted by a bot user.
- Navigate to the "Contact us" page.
- Fill out all the required fields.
- Submit the form (check if the form can be submitted).

3. Locations
- Hover over “About us” and go to “Locations”.
- Check Primary offices' section (check if all primary offices are displayed).


### How to set up reporting
1. Install the plugin for Allure reporting using "pip install allure-pytest".
2. Install Allure via "brew install allure" for Mac or check https://allurereport.org/docs/install for other operating systems.
3. "cd" to the folder "ui-automation-task".
4. Run the command for generating the report: "allure serve report" and the report will be opened in a separate tab of the browser.
5. A generated test report can also be found under the "Actions" tab at https://github.com/ivanvalchuk/ui-automation-task 
   Click on a corresponding workflow run to see the details. 

#### ***Please not that html report can also be generated by running the "pytest --html=report.html" command.

### CI
The tests are also run on each push and pull request to the respository in GitHub, which is configured in "playwright.yml" as part of the ".github/workflows" folder. The test report is also generated there.

#### The generated html report can also be viewed by opening the "./report.html" file.
#### The screenshots of the found issues recorded in Allure Report can be found in the "./test_results" folder for reference purposes.
