from ElectionData import fetchDataFromWebsite
from Database import dataFiltering 

data = fetchDataFromWebsite()
print(data)
dataFiltering.filterData(data)

# candidate {'Name': 'KAKINADA VENKATA RAMANA', 'Party': 'Andhra Rastra Praja Samithi', 'Status': 'Rejected', 
# 'State': 'Andhra Pradesh', 'Constituency': 'Atmakur',
#  'Election': 'Election-June-2022', 'ElectionType': 'AC - BYE'}