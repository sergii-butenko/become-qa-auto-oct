from src.applications.github.ui.base_page import BasePage
from selenium.webdriver.common.by import By


class GitHubUILoginPage(BasePage):
    """Current class contains every UI usage we use in tests"""

    def __init__(self, driver) -> None:
        super().__init__(driver)

    def navigate_to_page(self):
        self.driver.get("https://github.com/login")
        # waiters that some data exists
        
    def try_to_login(self, username, password):
        login_fld = self.find_el(By.ID ,"login_field")
        #waiter to be added

        login_fld.send_keys(username)
        
        if self.get_text(login_fld) != username:
            print("Username is entered incorrectry")
            raise RuntimeError("Username is entered incorrectry")
        
        pass_fld = self.find_el(By.ID ,"password") 
        #waiter to be added
        pass_fld.send_keys(password)

        # click button
        login_fld = self.find_el(By.NAME ,"commit")
        #waiter to be added

        login_fld.click()

    def check_login_error_message(self):
        error_msg = self.find_el(By.ID ,"js-flash-container") # replace with different identifier e.g. Text of error

        return error_msg is not None

    def close_browser(self):
        self.driver.quit()