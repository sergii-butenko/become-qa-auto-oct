import pytest

from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from src.applications.github.ui.github_ui import GitHubUILoginPage
from src.helpers.browsers_provider import BrowserProvider


def test_github_login_negative():
    # create webdriver object 
    driver = webdriver.Firefox()
  
    # open the browser
    # navigate to login page
    driver.get("https://github.com/login")


    # enter wrong creds
    login_fld = driver.find_element(By.ID ,"login_field")
    login_fld.send_keys("wrong email")
    
    pass_fld = driver.find_element(By.ID ,"password") 
    pass_fld.send_keys("wrong pass")

    # click button
    login_fld = driver.find_element(By.NAME ,"commit")
    login_fld.click()
    
    # check error message
    error_msg = driver.find_element(By.ID ,"js-flash-container") # replace with different identifier e.g. Text of error
    time.sleep(5)
    assert error_msg is not None
    


#### test with tear_up/teardown but whout page object
@pytest.fixture
def github_login():
    # tear_up foreach
    # open the browser
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

    # navigate to login page
    driver.get("https://github.com/login")

    # return login page
    yield driver

    # tear_down foreach
    # close the browser --post set after EACH
    driver.quit()



def test_github_login_negative_fixture(github_login):
    login_fld = github_login.find_element(By.ID ,"login_field")
    login_fld.send_keys("wrong email")
    
    pass_fld = github_login.find_element(By.ID ,"password") 
    pass_fld.send_keys("wrong pass")

    # click button
    login_fld = github_login.find_element(By.NAME ,"commit")
    login_fld.click()
    
    # check error message
    error_msg = github_login.find_element(By.ID ,"js-flash-container") # replace with different identifier e.g. Text of error
    time.sleep(5)

    assert error_msg is not None


@pytest.fixture
def github_login_page_object():
    # tear_up foreach
    BROWSER_NAME = 'ff_slow'
    driver = BrowserProvider.get_driver(BROWSER_NAME)

    gitlab_login_page = GitHubUILoginPage(driver)
    gitlab_login_page.navigate_to_page()
    
    # return login page
    yield gitlab_login_page

    # tear_down foreach
    # close the browser --post set after EACH
    gitlab_login_page.close_browser()


def test_github_login_negative_page_object(github_login_page_object):
    github_login_page_object.try_to_login("kjasbdkjfsa", "ksjhdkjfsdf")

    assert github_login_page_object.check_login_error_message()