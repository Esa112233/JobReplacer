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
import pandas as pd


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
        add_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[1]/a/span"))
        )
        add_dropdown.click()
        stream_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Stream"))
        )
        stream_tab.click()
        # add_select = Select(add_dropdown)
        # add_select.select_by_visible_text("Stream")


        # add_select.select_by_visible_text("Stream")
        # add_dropdown.click()

    except Exception as e:
        print("exception in add button after save")
        print(f"Error in AddButton: {e}")
        driver.quit()

def AddButtonAfterSave(driver):
    try:
        add_dropdown2 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[1]/a/span"))
        )
        add_dropdown2.click()
        stream_tab = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Stream"))
        )
        stream_tab.click()
        # add_select = Select(add_dropdown)
        # add_select.select_by_visible_text("Stream")


        # add_select.select_by_visible_text("Stream")
        # add_dropdown.click()

    except Exception as e:
        print("exception in add button after save")
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
def InsertStream(driver, mylist):
    num_Streams = len(mylist)
    success_Elements = list()
    unsuccess_Elements = list()


    for name in mylist:
        Name_input = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "stream_name"))
            )
        Name_input.send_keys(name)


        saveButton = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.NAME, "commit"))
        )
        saveButton.click()
        try:
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "alert-heading")))
            unsuccess_Elements.append(name)
            saveButton = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, "stream_name"))
        )
            saveButton.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
        except:
            success_Elements.append(name)
            print("Here success")
            AddButtonAfterSave(driver)
    print("Successfully saved streams: " + success_Elements)
    print("Already existing streams: " + unsuccess_Elements)







def main(mylist):
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
        InsertStream(driver, mylist)
        # addit = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[11]/a")
        # print(addit)
        # actionchain = ActionChains(driver=driver)
        # actionchain.move_to_element(addit).click().perform()
       
       
    except:
        driver.quit()
    print("Done!")








if __name__ == "__main__":
    PATH = "c:/Users/User/Desktop/File_Loc_For_Replacer/CNTRAL Database Corrections Submission.xlsx"
    df = pd.read_excel(PATH,"Sheet1") # can also index sheet by name or fetch all sheets

    mylist = df['TestStream'].dropna().tolist()
    print(mylist)
    main(mylist)





