import pytest
import logging
import datetime
import allure
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Browser to run tests (chrome, edge, firefox)",
    )
    parser.addoption(
        "--url", default="https://automationexercise.com/", help="Base OpenCart URL"
    )
    parser.addoption("--log_level", default="INFO")
    parser.addoption("--selenoid_url", default="http://77.244.221.82/wd/hub")
    parser.addoption("--remote", action="store_true", help="Run tests on Selenoid")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "setup":
        browser = item.funcargs.get("browser")
        if browser:
            allure.attach(
                name=browser.session_id,
                body=json.dumps(browser.capabilities, indent=4, ensure_ascii=False),
                attachment_type=allure.attachment_type.JSON,
            )

    if rep.when == "call" and rep.failed:
        browser = item.funcargs.get("browser")
        if browser:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG,
            )

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def logger(request):
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler("example.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info(
        "=====> Test %s started %s" % (request.node.name, datetime.datetime.now())
    )

    yield logger
    logger.info(
        "=====> Browser %s opened at %s" % (request.node.name, datetime.datetime.now())
    )


@pytest.fixture
def browser(request, logger):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    selenoid_url = request.config.getoption("--selenoid_url")
    remote = request.config.getoption("--remote")

    if remote:
        if browser_name == "chrome":
            options = ChromeOptions()
        elif browser_name == "firefox":
            options = FirefoxOptions()
        elif browser_name == "edge":
            options = EdgeOptions()

        options.set_capability("browserName", browser_name)

        driver = webdriver.Remote(command_executor=selenoid_url, options=options)
    else:
        if browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "edge":
            driver = webdriver.Edge()
        elif browser_name == "firefox":
            driver = webdriver.Firefox()

    driver.logger = logger
    driver.test_name = request.node.name
    driver.base_url = base_url
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
