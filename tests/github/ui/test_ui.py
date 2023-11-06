from selenium import webdriver 
import time
from selenium.webdriver.common.by import By


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
    
