from ElectionData import fetchDataFromWebsite
from Database.dataFiltering import filterData

data = fetchDataFromWebsite()
filterData(data)

