```Debugging Tips
If the issue persists, try running pytest with the -v or --trace-config option to see how pytest is handling the configuration:
pytest -v --trace-config


Purpose: The pytest_addoption function allows you to add custom command-line options to pytest.
parser.addoption:
parser.addoption Method:

The parser.addoption method is used to add custom options.
You can specify the option's name, its type, default value, help text, and more.

--browser: This defines a new command-line option named --browser.
action="store": This specifies that the option will store the value provided by the user (like chrome or firefox).
default="chrome": If the user does not specify the --browser option, it defaults to chrome.
help: This provides a description of the option, which can be viewed using pytest --help.
@pytest.fixture(scope="function"): This decorator defines a fixture with a scope of "function", meaning a new instance of the fixture is created for each test function.

request: This is a built-in pytest fixture that provides information about the test being run, including command-line options.

browser_name = request.config.getoption("--browser"):

This retrieves the value of the --browser option passed via the command line.


The @pytest.fixture decorator allows you to create fixtures that can be used across your test suite. The scope parameter in the @pytest.fixture(scope="...") decorator determines the lifespan or the duration for which the fixture will be active. Different scopes control how often the fixture is set up and torn down.

Here are the different scopes you can use with @pytest.fixture:

1. Function Scope (scope="function")
Default: If you don't specify a scope, function is the default.
Duration: The fixture is set up once before each test function and torn down after the test function completes.
Use Case: Ideal for fixtures that need to be fresh for each test, such as initializing variables or creating new instances of objects.
python
Copy code
@pytest.fixture(scope="function")
def sample_fixture():
    # Setup code
    yield resource
    # Teardown code
2. Class Scope (scope="class")
Duration: The fixture is set up once per class, before any test methods within the class are executed, and torn down after all test methods in the class have run.
Use Case: Useful when you have multiple test methods in a single test class that can share the same setup, like a shared database connection or browser instance.
python
Copy code
@pytest.fixture(scope="class")
def class_fixture():
    # Setup code
    yield resource
    # Teardown code
3. Module Scope (scope="module")
Duration: The fixture is set up once per module (a file containing multiple test functions or classes) and torn down after all tests in the module have run.
Use Case: Suitable for resources that are expensive to set up and can be shared across all tests in a single module, such as a temporary file or a database connection.
python
Copy code
@pytest.fixture(scope="module")
def module_fixture():
    # Setup code
    yield resource
    # Teardown code
4. Package Scope (scope="package")
Duration: The fixture is set up once per package, which is a directory containing multiple modules, and torn down after all modules in the package have been tested.
Use Case: Rarely used, but can be useful if you have resources that need to be shared across an entire package of tests, such as setting up a large, shared dataset.
python
Copy code
@pytest.fixture(scope="package")
def package_fixture():
    # Setup code
    yield resource
    # Teardown code
5. Session Scope (scope="session")
Duration: The fixture is set up once per test session and torn down after all tests in all modules have completed.
Use Case: Ideal for very expensive setup operations that should only be done once, such as starting a test server or connecting to a remote database.
python
Copy code
@pytest.fixture(scope="session")
def session_fixture():
    # Setup code
    yield resource
    # Teardown code
Examples of Usage
Function Scope Example:

python
Copy code
@pytest.fixture(scope="function")
def db_connection():
    conn = connect_to_db()
    yield conn
    conn.close()
This fixture will open and close a database connection for each test function that uses it.
Class Scope Example:

python
Copy code
@pytest.fixture(scope="class")
def web_driver():
    driver = setup_web_driver()
    yield driver
    driver.quit()
This fixture will set up a web driver once for all test methods in a class and quit it after the class is done.
Module Scope Example:

python
Copy code
@pytest.fixture(scope="module")
def temp_file():
    file = create_temp_file()
    yield file
    delete_temp_file(file)
This fixture creates a temporary file that all test functions in the module can use, and deletes it after the module's tests are done.
Session Scope Example:

python
Copy code
@pytest.fixture(scope="session")
def global_config():
    config = load_global_config()
    yield config
This fixture loads a global configuration file once for the entire test session.
When to Use Each Scope
function: Use when each test needs a clean, isolated instance of the fixture.
class: Use when all tests within a class can share the same fixture instance.
module: Use when all tests within a module can share the same fixture instance.
package: Use when all tests within a package can share the same fixture instance.
session: Use when all tests in the entire session can share the same fixture instance.
By selecting the appropriate scope for your fixtures, you can optimize your tests for both performance and correctness, ensuring that shared resources are handled efficiently.



from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

slider = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, 'XPATH_OF_THE_SLIDER_HANDLE'))
)

actions.drag_and_drop_by_offset(source_element, x_offset, y_offset).perform()









```
