from selenium import webdriver 
from selenium.webdriver.common.by import By


class GitHubUILoginPage:
    """Current class contains every UI usage we use in tests"""

    def __init__(self, browser_name) -> None:
        if browser_name == 'ff':
            self.driver = webdriver.Firefox()
        elif browser_name == 'chrome':
            pass

    def navigate_to_page(self):
        self.driver.get("https://github.com/login")
        # waiters that some data exists


    def try_to_login(self, username, password):
        login_fld = self.driver.find_element(By.ID ,"login_field")
        #waiter to be added

        login_fld.send_keys(username)
        
        pass_fld = self.driver.find_element(By.ID ,"password") 
        #waiter to be added
        pass_fld.send_keys(password)

        # click button
        login_fld = self.driver.find_element(By.NAME ,"commit")
        #waiter to be added

        login_fld.click()

    def check_login_error_message(self):
        error_msg = self.driver.find_element(By.ID ,"js-flash-container") # replace with different identifier e.g. Text of error

        return error_msg is not None

    def close_browser(self):
        self.driver.quit()