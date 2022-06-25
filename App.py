from ElectionData import fetchDataFromWebsite
from Database import dataFiltering 

data = fetchDataFromWebsite()
dataFiltering.filterData(data)

