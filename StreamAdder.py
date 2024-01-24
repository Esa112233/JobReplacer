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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

def loginPage(driver):
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

def overview(driver):
    FacilitiesButton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "facilities-nav-item"))
    )
    FacilitiesButton.click()

def Facilities(driver):

    SRP = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/table/tbody/tr/td[2]/strong/a"
))
    )
    actionchain = ActionChains(driver=driver)
    actionchain.move_to_element(SRP).click().perform()
    
def AddButton(driver):
    try:
        add_dropdown = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/a/span"))
        )
        add_dropdown.click()
        # add_select = Select(add_dropdown)
        # add_select.select_by_visible_text("Stream")

        # add_select.select_by_visible_text("Stream")
        # add_dropdown.click()

    except Exception as e:
        print(f"Error in AddButton: {e}")
        driver.quit()

#     add = Select(WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/a"
# ))
#     ))
#     add.select_by_visible_text("Stream")
    
#     add = WebDriverWait(driver, 5).until(
#         EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[11]/a"
# ))
#     )
#     add.click()
    # actionchain = ActionChains(driver=driver)
    # actionchain.move_to_element(add).click().perform()

def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://cntr.al/login")
    try:
        # Setup for selenium and get cntr.al login page
        
        # Type in email, password, and press login
        loginPage(driver)
        overview(driver)
        Facilities(driver)
        AddButton(driver)
        # addit = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[11]/a")
        # print(addit)
        # actionchain = ActionChains(driver=driver)
        # actionchain.move_to_element(addit).click().perform()
        
        
    except:
        driver.quit()




if __name__ == "__main__":
    main()

