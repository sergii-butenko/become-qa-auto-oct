from selenium import webdriver 


class BrowserProvider:
    """
    Return the initialized driver for desired browser
    """

    @staticmethod
    def get_driver(browser_name):        
        if browser_name == 'ff':
            driver = webdriver.Firefox()
            # add options  speed - normal
        elif browser_name == 'ff_slow':
            driver = webdriver.Firefox()
            # add options  speed - reduce

        elif browser_name == 'chrome':
            pass

        return driver