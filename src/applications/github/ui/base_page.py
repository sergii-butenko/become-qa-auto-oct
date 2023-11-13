class BasePage:

    def __init__(self, driver) -> None:
        self.driver = driver
    
    def find_el(self, locator_name, locator_value):
        # add waiters
        # add checks
        return self.driver.find_element(locator_name, locator_value)

    def click_el(self, locator_name, locator_value):
        # add waiters
        # add checks
        return self.driver.find_element(locator_name, locator_value)

    def get_text(self, locator_name, locator_value):
        # add waiters
        # add checks
        return self.driver.find_element(locator_name, locator_value)
