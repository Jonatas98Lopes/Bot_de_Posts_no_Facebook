from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class GoogleChrome:
    def __init__(self):
        self._chrome_options = Options()
        
        self._arguments = [
            '--lang=pt-BR',
            '--window-size=800,600',
            '--incognito',
            '--disable-notifications'
        ]


        for argument in self._arguments:
            self._chrome_options.add_argument(argument)

        self._experimental_options = {
            'download.prompt_for_download': False,
            'profile.default_content_setting_values.notifications': 2

        }

        self._chrome_options.add_experimental_option('prefs', self._experimental_options)

        self._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(version='114.0.5735.90').install()), options=self._chrome_options)

    def get_experimental_options(self):
        return self._experimental_options
    
    def get_arguments(self):
        return self._arguments
    
    def get_driver(self):
        return self._driver
    