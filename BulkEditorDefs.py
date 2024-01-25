from StreamAdder import By, webdriver, WebDriverWait, EC, time, Service, Options, WebElement, Keys, ActionChains, Select, pd


def overview(driver):
    FacilitiesButton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Reporting"))
    )
    FacilitiesButton.click()


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


    def bulk_Editor(driver):
        bulk = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/table/tbody[2]/tr[1]/td[5]/a[2]/i"))
        )
        bulk.click()