from StreamAdder import By, webdriver, WebDriverWait, EC, time, Service, Options, WebElement, Keys, ActionChains, Select, pd
from BulkEditorDefs import *







def editReport(driver):
    editReportButton = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.container.top-margin > div.content.clearfix > div.page-header.clearfix > a:nth-child(1)"))
    )
    # editReportButton.click()
    actionchain = ActionChains(driver=driver)
    actionchain.move_to_element(editReportButton).click().perform()



def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://cntr.al/login")
    try:
        loginPage(driver=driver)
        overview(driver=driver)
        bulk_Editor(driver=driver)
    except:
        driver.quit()
    return










if __name__ == "__main__":

    # PATH = "c:/Users/User/Desktop/File_Loc_For_Replacer/CNTRAL Database Corrections Submission.xlsx"
    # df = pd.read_excel(PATH,"Sheet1") # can also index sheet by name or fetch all sheets
    # Code in the part where it separates each csv into parts of 50
    main()