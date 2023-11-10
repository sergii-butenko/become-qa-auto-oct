import os


class ConfigEasy:
    """Config class is responsbiel to storing framework's and env's configuration
    config variables declared:
    1
    2
    3
    ...
    """
    
    request_timeout = 29
    user_name = os.environ.get('USERNAME')  # or get it from elsewhere
    env = os.environ.get('BQA_ENV')
    browser_name = os.environ.get('BROWSER_NAME')

config = ConfigEasy()

print(config.request_timeout)
print(config.user_name)
print(config.env)