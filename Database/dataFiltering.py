from ordered_set import OrderedSet
from time import time
from dbConnection import *


# RESPONSE DATA
# data = [{
#     'Id':44,
#     'Name': 'PATTAN MANUSOOR KHAN',
#     'Party': 'INDEPENDENT',
#     'Status': 'REJECTED',
#     'State': 'MADHYA PRADESH',
#     'Constituency': 'ATMAKUR',
#     'Election': 'ELECTION-JUNE-2022',
#     'ElectionType': 'AC-BYE',
# }]


Index = 1
cache = OrderedSet()

# get one id from table
def getDataFromDB(id,table,col_name,match_col_name):
    my_cursor.execute(f"select {id} from {table} where {col_name} = '{match_col_name}';")
    return int(my_cursor.fetchone()[0])

# get all id's from table
def getIdFromDB(candidate):
    state_id  = getDataFromDB('state_id','states','state_name',candidate['State'])
    constituency_id  = getDataFromDB('constituency_id','constituency','constituency_name',candidate['Constituency'])
    electiontype_id  = getDataFromDB('electiontype_id','electiontype','electiontype_name',candidate['ElectionType'])
    election_id  = getDataFromDB('election_id','election','election_name',candidate['Election'])
    party_id  = getDataFromDB('party_id','party','party_name',candidate['Party'])
    return [state_id, constituency_id, electiontype_id,election_id, party_id]
    
def filterData(data):
    for candidate in data:
        state_id, constituency_id, electiontype_id,election_id, party_id = getIdFromDB(candidate=candidate)
        cache.add(f"INSERT INTO CANDIDATE (CANDIDATE_ID, CANDIDATE_NAME, CANDIDATE_STATUS, PARTY_ID, CONSTITUENCY_ID) VALUES({Index}, '{candidate['Name']}','{candidate['Status']}', {party_id},{constituency_id});\n")
        cache.add(f"INSERT INTO ELECTION_ELECTIONTYPE (ELECTION_ID, ELECTIONTYPE_ID) VALUES({election_id},{electiontype_id});\n")
        cache.add(f"INSERT INTO ELECTION_STATES (ELECTION_ID, STATE_ID) VALUES({election_id},{state_id});\n")
        cache.add(f"INSERT INTO ELECTIONTYPE_STATES(ELECTIONTYPE_ID,STATE_ID) VALUES({electiontype_id},{state_id});\n")
        cache.add(f"INSERT INTO ELECTIONTYPE_CONSTITUENCY(ELECTIONTYPE_ID,CONSTITUENCY_ID) VALUES({electiontype_id},{constituency_id});\n")
        Index+=1
    
        db.commit()
        my_cursor.close()
        db.close()

        file = open("DynamicData.sql", "w")
        file.writelines(cache)
        file.close()