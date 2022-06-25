from select import select
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

#----whole data-----
# data = []

#---- contants ----

chromeDriver = "C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver.exe"
rootUrl = "https://affidavit.eci.gov.in/"

#---- xPaths ----

electionXP = '//*[@id="electionType"]'
electionTypeXP = '//*[@id="election"]'
stateXP = '//*[@id="states"]'
filterXP = '//*[@id="CandidateCustomFilter"]/button'
paginationXP = '/html/body/main/section/div/div/div/div/div/div[2]/div/ul/li'
recordsXP = '//*[@id="data-tab"]/tbody/tr/td[2]'
contituencyXP = '//*[@id="constId"]'
name_of_candidateXP = '//*[@id="data-tab"]/tbody/tr/td[2]/div/h4'
name_of_partyXP = '//*[@id="data-tab"]/tbody/tr/td[2]/div/div/div[1]/p[1]/text()'
name_of_stateXP = '//*[@id="data-tab"]/tbody/tr/td[2]/div/div/div[2]/p[1]/text()'
name_of_consistuencyXP = '//*[@id="data-tab"]/tbody/tr/td[2]/div/div/div[2]/p[2]/text()'



#-----getter-------

# note: functions can be divided further

def getElection():
    elections = driver.find_element(by = By.XPATH,value = (electionXP))
    list_of_elections = Select(elections)
    return list_of_elections

def getElectionType():
    electionType = driver.find_element(by = By.XPATH,value = (electionTypeXP))
    list_of_electiontype = Select(electionType)
    return list_of_electiontype

def getStateList():
    states = driver.find_element(by = By.XPATH,value = (stateXP))
    list_of_states = Select(states)
    return list_of_states

def getConstituency():
    constituencies = driver.find_element(by = By.XPATH,value = (contituencyXP))
    list_of_constituency = Select(constituencies)
    return list_of_constituency

def getRecord():
    records = driver.find_elements(by = By.XPATH ,value = (recordsXP))
    return len(records)


def getPaginationCount():
    pagination = driver.find_elements(by = By.XPATH,value = (paginationXP))
    return len(pagination)

#-----buttons-------

def selectFilter():
    driver.find_element(by = By.XPATH,value=(filterXP)).click()

def selectNextPage(index):
    driver.find_element(by = By.XPATH,value=f'{paginationXP}[{index}]').click()


#-----main-------
def fetchDataFromWebsite():
        try:
            # Object that manages the starting and stopping of the ChromeDriver
            global serv
            serv = Service(chromeDriver)


            #chrome driver compatibility
            # options = webdriver.ChromeOptions()
            # options.add_experimental_option('excludeSwitches', ['enable-logging'])

            global driver
            driver = webdriver.Chrome(service=serv)

            # calling the root url for automation
            driver.get(rootUrl)

            # resizing windows to full size
            driver.maximize_window()

            data = []
            cache = set()
            
            list_of_elections = getElection()
            list_of_elections.select_by_index(0)
            name_of_election = list_of_elections.first_selected_option.text
            time.sleep(1)
            list_of_electionType = getElectionType()
            time.sleep(1)
            for indexElectionType in range(1,len(list_of_electionType.options)):
                list_of_electionType = getElectionType()
                time.sleep(1)
                list_of_electionType.select_by_index(indexElectionType)
                time.sleep(1)
                type_of_election = list_of_electionType.first_selected_option.text
                list_of_state = getStateList()
                for indexState in range(1,len(list_of_state.options)):
                    list_of_state = getStateList()
                    time.sleep(2)
                    print("selecting state",indexState)
                    list_of_state.select_by_index(indexState)
                    time.sleep(1)
                    list_of_constituency = getConstituency()
                    time.sleep(1)
                    for indexConstituency in range(1,len(list_of_constituency.options)):
                        list_of_constituency = getConstituency()
                        time.sleep(1)
                        list_of_constituency.select_by_index(indexConstituency)
                        candidates = []
                        time.sleep(1)
                        selectFilter()
                        time.sleep(1)
                        count = getPaginationCount()
                        for index in range(1,count):
                            time.sleep(1)
                            selectNextPage(index)
                            time.sleep(1)
                            list_of_candidates = getRecord()
                            for c in range(1,list_of_candidates):
                                nam = driver.find_element(by=By.XPATH,value=(f'//*[@id="data-tab"]/tbody/tr[{c}]/td[2]/div/h4')).text
                                party = driver.find_element(by=By.XPATH,value=(f'//*[@id="data-tab"]/tbody/tr[{c}]/td[2]/div/div/div[1]/p[1]')).text
                                status = driver.find_element(by=By.XPATH,value=(f'//*[@id="data-tab"]/tbody/tr[{c}]/td[2]/div/div/div[1]/p[2]/strong[2]/font')).text
                                state = driver.find_element(by=By.XPATH,value=(f'//*[@id="data-tab"]/tbody/tr[{c}]/td[2]/div/div/div[2]/p[1]')).text
                                constituency = driver.find_element(by=By.XPATH,value=(f'//*[@id="data-tab"]/tbody/tr[{c}]/td[2]/div/div/div[2]/p[2]')).text
                                candidate = {'Name' : nam , 'Party' : party.split(':')[1].lstrip() , 'Status' : status , 'State' : state.split(':')[1].lstrip() , 'Constituency' : constituency.split(':')[1].lstrip(),'Election': name_of_election,'ElectionType' : type_of_election}
                                cs = ''+candidate
                                if cs not in cache:
                                    cache.add(cs)
                                    data.append(candidate)
                      
            driver.close()
            return data
        except Exception as e: 
            print(e)


