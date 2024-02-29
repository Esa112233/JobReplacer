import json
from StreamAdder import By, webdriver, WebDriverWait, EC, time, Service, Options, WebElement, Keys, ActionChains, Select, pd
from math import ceil


def overview(driver):

    FacilitiesButton = WebDriverWait(driver, 25).until(
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
        
        bulk = WebDriverWait(driver, 15).until(
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
    df = pd.read_excel(PATH,"Esa Fixes") # can also index sheet by name or fetch all sheets
    myList = df['Tag'].dropna().tolist()

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

def get_data_Dict():

    with open('C:/Users/User/Desktop/JobReplacer/JobReplacer/dynamicTags.json','r') as f:
        data = json.loads(f.read())
    return data

def updateTags(stream, num):
    with open('C:/Users/User/Desktop/JobReplacer/JobReplacer/dynamicTags.json','r') as f:
        data = json.loads(f.read())
        data.pop(stream)
        newData = json.dumps(data, indent=4)
    with open('C:/Users/User/Desktop/JobReplacer/JobReplacer/dynamicTags.json','w') as f:
        f.write(newData)




def divideFifty(stream, stream_And_Tags):
    partitionedListDict = dict()
    NumOfContainers = ceil(len(stream_And_Tags[stream])/50)
    tags = stream_And_Tags[stream]
    for i in range(NumOfContainers):
        tagsPartitionedTemp = list()
        if len(tags) < 50:
            for n in range(len(tags)):
                tagsPartitionedTemp.append(tags[n])
            for j in range(len(tags)):
                tags.pop(0)
        else:
            for n in range(50):
                tagsPartitionedTemp.append(tags[n])
            for j in range(50):
                tags.pop(0)
        partitionedListDict[i] = tagsPartitionedTemp

    return partitionedListDict, NumOfContainers
    
def firstEdit(driver, tags):
    FieldTagNumbers = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "report_search_params_field_tag_numbers"))
    )
    mystr = ','.join(tags)
    FieldTagNumbers.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
    FieldTagNumbers.send_keys(mystr)
    
    
def saveEdit(driver):
    saveButton = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.NAME, "commit"))
    )
    saveButton.click()

def selectAll(driver):
    select_All = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "select-all"))
    )
    select_All.click()

def bulkEditComponents(driver):
    bulkEditButton = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'bulk-edit'))
    )
    bulkEditButton.click()

def pickStream(driver, stream):
    streamCheck = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'stream_uid_enabled'))
    )
    streamCheck.click()

    dropDown = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, 'emission_component_stream_uid'))
    )

    streamSelect = Select(dropDown)
    streamSelect.select_by_visible_text(stream)

def saveFinal(driver):
    saveButton = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.NAME, "commit"))
    )
    saveButton.click()

def midSave(num, partitionedListDict, stream):

    fullList = list()
    for n in range(len(partitionedListDict)):
        fullList.extend(partitionedListDict[n])

    num = num-5
    if len(fullList) < 250:
        for i in range(len(fullList)):
            fullList.pop(0)
        updateSave(fullList, stream)
    else:
        for i in range(250):
            fullList.pop(0)
        updateSave(fullList, stream)
    
def updateSave(fullList, stream):
    with open('C:/Users/User/Desktop/JobReplacer/JobReplacer/dynamicTags.json','r') as f:
        data = json.loads(f.read())
        #data.pop(stream)
        data[stream] = fullList
        newData = json.dumps(data, indent=4)
    with open('C:/Users/User/Desktop/JobReplacer/JobReplacer/dynamicTags.json','w') as f:
        f.write(newData)
        print("saved!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
def get_Data_test():
     
    PATH = "c:/Users/User/Desktop/File_Loc_For_Replacer/CNTRAL Database Corrections Submission.xlsx"
    df = pd.read_excel(PATH,"Esa Fixes") # can also index sheet by name or fetch all sheets
    stream_List = df['NEW ASSIGNED STREAM FINAL'].dropna().drop_duplicates().tolist()
    numOfStreams = len(stream_List)
    print(f"Number of streams {numOfStreams}")
    streamDict = dict()

    countstreams = 0
    testingTags = list()
    for stream in stream_List:
        df2 = pd.read_excel(PATH,"Esa Fixes")
        tagsList = df2.loc[df2['NEW ASSIGNED STREAM FINAL'] == stream,'Tag'].dropna().tolist()
        streamDict[stream] = tagsList
        testingTags.extend(tagsList)
        print(stream)
        countstreams+=1
    count = 0
    with open("dynamicTags.json", "w") as outfile: 
        json.dump(streamDict, outfile)
    print(streamDict)
    print(f"number of streams: {countstreams}")
    for key in streamDict:
        print(f"{key} has {len(streamDict[key])} tags")
        count+= len(streamDict[key])
    print(f"total tags: {count}")
    totalTags = get_Tags()
    for i in testingTags:
        if i not in totalTags:
            print(f"{i} was not in the list")
    

def jsontest():

    templist = list()
    tempdict = dict()
    seen = set()
    dupes = list()
    fullTags = get_Tags()
    f = open('C:/Users/User/Desktop/JobReplacer/JobReplacer/wrongTags.json','r')
    data = json.loads(f.read())
    count = 0
    # wrongTags = list(data.values())
    wrongTags = [tag for tags in data.values() for tag in tags]
    print(f"{len(wrongTags)} wrongTags")
    print(len(fullTags))
    for i in wrongTags:
        print(i)
        if i not in fullTags:
            print(f"{i} not in full Tags")
    for x in fullTags:
        print(x)
        if x not in wrongTags:
            dupes.append(x)
        else:
            seen.add(x)
    print(len(seen))
    print(dupes)
    print(fullTags[1])
    # for i in fullTags:
    #     if i in templist:
    #         print(f"{i} is a duplicate")
    #     else:
    #         templist.append(i)
    # for i in data:
    #     for n in data[i]:
    #         if n in tempdict:
    #             print(f"{i} is a duplicate")
    return count
    


if __name__ == "__main__":
    # pyautogui.moveTo(170.13, 28)
    # while True:
    #     pos = pyautogui.position()
    #     print(pos)

#     # myList = get_Tags()
#     # print(myList)
#     #print(len(myList))
#     # myListStream, tags, rows = get_DataTest()
#     # print(rows)
#     # get_Data()
#     pass


    # for (stream, tag) in zip(myListStream, tags):
    #     print(stream, tag)
    #     num+=1
    # print(num)
    # print(len(myListStream))
    # print(len(tags))
    # print(myListStream[1])
    # print(tags[0])
    # driver = 1
    # bulkEditComponents(driver)
    pass
