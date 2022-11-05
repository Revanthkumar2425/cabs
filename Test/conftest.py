import pytest
from selenium import webdriver
from Library.config import Config


@pytest.fixture(params=["chrome", "edge"])
def init_driver(request):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=Config.CHROME_PATH)

    else:
        driver = webdriver.Edge(executable_path=Config.EDGE_PATH)

    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    driver.close()
