import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests (chrome or firefox)")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    yield driver
    driver.quit()
