import traceback
from BulkEditorDefs import *
from StreamAdder import By, webdriver, WebDriverWait, EC, time, Service, Options, WebElement, Keys, ActionChains, Select, pd




def main():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://cntr.al/login")
    try:
        loginPage(driver=driver)
        overview(driver=driver)
        bulk_Editor(driver=driver)
        stream_And_Tags = get_data_Dict()
        
        for stream in stream_And_Tags:
            partitionedListDict, numOfContainers = divideFifty(stream, stream_And_Tags)

            for num in range(0, numOfContainers):
                tags = partitionedListDict[num]
                firstEdit(driver, tags)
                saveEdit(driver)
                selectAll(driver)
                bulkEditComponents(driver)
                pickStream(driver, stream)
                saveFinal(driver)
                if num % 4 == 0 and num != 0:
                    midSave(num, partitionedListDict, stream)
                overview(driver=driver)
                bulk_Editor(driver=driver)
            updateTags(stream, num)
                
                




    except Exception as e:
        print(e)
        print(traceback.format_exc())
        #driver.quit()
    print("Done")
    return










if __name__ == "__main__":

    # PATH = "c:/Users/User/Desktop/File_Loc_For_Replacer/CNTRAL Database Corrections Submission.xlsx"
    # df = pd.read_excel(PATH,"Sheet1") # can also index sheet by name or fetch all sheets
    # Code in the part where it separates each csv into parts of 50
    main()
