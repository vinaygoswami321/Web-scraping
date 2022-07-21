from types import NoneType
from ordered_set import OrderedSet
from time import time
# import dbConnection

import mysql.connector
# from ElectionData import data


def dbconnectionprocess():
        # database connection established
    global db
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="indianelection"
    )

    # to execute multiple query in one go we need to set buffered to true
    global my_cursor
    my_cursor = db.cursor(buffered=True)

# RESPONSE DATA
# data = [{
#     'Id':44,
#     'Name': 'PATTAN MANUSOOR KHAN',
#     'Party': 'GIRI AND SISTERS',
#     'Status': 'REJECTED',
#     'State': 'MADHYA PRADESH',
#     'Constituency': 'ATMAKUR',
#     'Election': 'ELECTION-JUNE-2022',
#     'ElectionType': 'AC - BYE',
# }]


global cache
cache = set()

# get one id from table
def getDataFromDB(id,table,col_name,match_col_name):
    my_cursor.execute(f"select {id} from {table} where {col_name} = '{match_col_name}';")
    if table == 'constituency' and my_cursor.fetchone() == None:
        my_cursor.execute(f"select count(*) from constituency;")
        print("going")
        count = int(my_cursor.fetchone()[0])
        count+=1
        cache.add(f"Insert into constituency (constituency_id, constituency_name, state_id) values({count}, '{match_col_name}','{state_id}');")
        my_cursor.execute(f"Insert into constituency (constituency_id, constituency_name, state_id) values({count}, '{match_col_name}','{state_id}');")
        return int(count)
    if table == 'constituency':
        my_cursor.execute(f"select {id} from {table} where {col_name} = '{match_col_name}';")
    if table == 'party' and my_cursor.fetchone() == None:
        my_cursor.execute(f"select count(*) from party;")
        print("coming")
        count = int(my_cursor.fetchone()[0])
        count+=1
        cache.add(f"Insert into party (party_id, party_name) values({count}, '{match_col_name}');")
        my_cursor.execute(f"Insert into party (party_id, party_name) values({count}, '{match_col_name}');")
        return int(count)
    if table == 'party':
        my_cursor.execute(f"select {id} from {table} where {col_name} = '{match_col_name}';")
    return int(my_cursor.fetchone()[0])

# get all id's from table
def getIdFromDB(candidate):
    global state_id
    state_id  = getDataFromDB('state_id','states','state_name',candidate['State'])
    constituency_id  = getDataFromDB('constituency_id','constituency','constituency_name',candidate['Constituency'])
    electiontype_id  = getDataFromDB('electiontype_id','electiontype','electiontype_name',candidate['ElectionType'])
    election_id  = getDataFromDB('election_id','election','election_name',candidate['Election'])
    party_id  = getDataFromDB('party_id','party','party_name',candidate['Party'])
    return [state_id, constituency_id, electiontype_id,election_id, party_id]
    
def filterData(data):
    dbconnectionprocess()
    Index = 1
    for candidate in data:
        print("candidate",candidate)
        state_id, constituency_id, electiontype_id,election_id, party_id = getIdFromDB(candidate=candidate)
        cache.add(f"INSERT INTO CANDIDATE (CANDIDATE_ID, CANDIDATE_NAME, CANDIDATE_IMAGE ,CANDIDATE_STATUS, PARTY_ID, CONSTITUENCY_ID) VALUES({Index}, '{candidate['Name']}','{candidate['Image']}','{candidate['Status']}', {party_id},{constituency_id});\n")
        cache.add(f"INSERT INTO ELECTION_ELECTIONTYPE (ELECTION_ID, ELECTIONTYPE_ID) VALUES({election_id},{electiontype_id});\n")
        cache.add(f"INSERT INTO ELECTION_STATES (ELECTION_ID, STATE_ID) VALUES({election_id},{state_id});\n")
        cache.add(f"INSERT INTO ELECTIONTYPE_STATES(ELECTIONTYPE_ID,STATE_ID) VALUES({electiontype_id},{state_id});\n")
        cache.add(f"INSERT INTO ELECTIONTYPE_CONSTITUENCY(ELECTIONTYPE_ID,CONSTITUENCY_ID) VALUES({electiontype_id},{constituency_id});\n")
        Index+=1
    
    db.commit()
    my_cursor.close()
    db.close()

# filterData(data)
    file = open("Database/DynamicData.sql", "w")
    file.writelines(cache)
    file.close()