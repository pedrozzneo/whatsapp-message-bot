from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

def set(profile):
    # Create Chrome options
    chrome_options = Options()
    base_path = r"C:\Users\pedro\seleniumProfiles"

    # Set user data directory (persistent profile)
    selenium_data_dir = os.path.join(base_path, profile)
    chrome_options.add_argument(f'user-data-dir={selenium_data_dir}')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--start-maximized')

    # Automatically download and use the correct ChromeDriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    return driver
