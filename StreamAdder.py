from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys

def main():
    
    try:
        # Setup for selenium and get cntr.al login page
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://cntr.al/login")
        # Type in email, password, and press login
        email = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "user_session_email"))
        )
    
        email.send_keys("eabuzar@nwrpartnership.com")
        password = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "user_session_password"))
        )
        password.send_keys("Swisscheese-11")

        loginButton = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.NAME, "commit"))
        )
        loginButton.click()
    except:
        driver.quit()




if __name__ == "__main__":
    main()

