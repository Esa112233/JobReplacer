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

def get_Streams():

    PATH = "c:/Users/User/Desktop/File_Loc_For_Replacer/CNTRAL Database Corrections Submission.xlsx"
    df = pd.read_excel(PATH,"Sheet1") # can also index sheet by name or fetch all sheets
    myList = df['NEW STREAMS'].dropna().tolist()

    return myList

def get_Tags():

    PATH = "c:/Users/User/Desktop/File_Loc_For_Replacer/CNTRAL Database Corrections Submission.xlsx"
    df = pd.read_excel(PATH,"Corrections Submission") # can also index sheet by name or fetch all sheets
    myList = df['Tags'].dropna().tolist()

    return myList

def get_DataTest():

    PATH = "c:/Users/User/Desktop/File_Loc_For_Replacer/CNTRAL Database Corrections Submission.xlsx"
    df = pd.read_excel(PATH,"Corrections Submission") # can also index sheet by name or fetch all sheets
    myList = df['Requested Update'].dropna().tolist()
    
    df2 = pd.read_excel(PATH,"Corrections Submission")
    tags = df2['Tags'].dropna().tolist()

    df3 = pd.read_excel(PATH,"Corrections Submission")
    rows = df3.loc[df3['Requested Update1'] == 'FUEL GAS'][['Tags', 'Current', 'Requested Update1']].dropna()
    # rows = df3[['Tags', 'Current', 'Requested Update1']]


    return myList, tags, rows

def get_Data():
     
    PATH = "c:/Users/User/Desktop/File_Loc_For_Replacer/CNTRAL Database Corrections Submission.xlsx"
    df = pd.read_excel(PATH,"Sheet1") # can also index sheet by name or fetch all sheets
    stream_List = df['NEW STREAMS'].dropna().tolist()
    numOfStreams = len(stream_List)
    streamDict = dict()

    countstreams = 0
    for stream in stream_List:
        df2 = pd.read_excel(PATH,"Corrections Submission")
        tagsList = df2.loc[df2['Requested Update1'] == stream,'Tags'].dropna().tolist()
        streamDict[stream] = tagsList
        print(stream)
        countstreams+=1
    count = 0
    print(streamDict)
    print(f"number of streams: {countstreams}")
    for key in streamDict:
        print(f"{key} has {len(streamDict[key])} tags")
        count+= len(streamDict[key])
    print(f"total tags: {count}")




if __name__ == "__main__":

    myList = get_Tags()
    print(len(myList))
    # myListStream, tags, rows = get_DataTest()
    # print(rows)
    #get_Data()






    # for (stream, tag) in zip(myListStream, tags):
    #     print(stream, tag)
    #     num+=1
    # print(num)
    # print(len(myListStream))
    # print(len(tags))
    # print(myListStream[1])
    # print(tags[0])
    

