create database `INDIANELECTION`;

-- Entity tables
USE `INDIANELECTION`;


-- create table party
CREATE TABLE PARTY(
    PARTY_ID INT NOT NULL,
    PARTY_NAME VARCHAR(255) NOT NULL,
    PRIMARY KEY(PARTY_ID)
);


-- create table candidate
CREATE TABLE CANDIDATE(
    CANDIDATE_ID INT NOT NULL,
    CANDIDATE_NAME VARCHAR(255) NOT NULL,
    CANDIDATE_IMAGE varchar(255) NOT NULL,
    CANDIDATE_STATUS VARCHAR(15) NOT NULL,
    PARTY_ID INT NOT NULL REFERENCES PARTY(PARTY_ID),
    CONSTITUENCY_ID INT NOT NULL REFERENCES CONSTITUENCY(CONSTITUENCY_ID),
    PRIMARY KEY(CANDIDATE_ID)
);

-- create table election

CREATE TABLE ELECTION(
    ELECTION_ID INT NOT NULL,
    ELECTION_NAME VARCHAR(255) NOT NULL,
    PRIMARY KEY(ELECTION_ID)
);


-- create table state

CREATE TABLE STATES(
 STATE_ID INT NOT NULL,
 STATE_NAME VARCHAR(255) NOT NULL,
    PRIMARY KEY (STATE_ID)
);

-- create table consituency
CREATE TABLE CONSTITUENCY(
    CONSTITUENCY_ID INT NOT NULL,
    CONSTITUENCY_NAME VARCHAR(255) NOT NULL,
    STATE_ID INT NOT NULL REFERENCES STATES(STATE_ID),
    PRIMARY KEY(CONSTITUENCY_ID)
);

-- create table electionType

CREATE TABLE ELECTIONTYPE(
 ELECTIONTYPE_ID INT NOT NULL,
 ELECTIONTYPE_NAME VARCHAR(255) NOT NULL,
    PRIMARY KEY (ELECTIONTYPE_ID)
);

-- relationship table

-- create table electionType_constituency
CREATE TABLE ELECTIONTYPE_CONSTITUENCY(
 ELECTIONTYPE_ID INT NOT NULL REFERENCES ELECTIONTYPE(ELECTIONTYPE_ID),
 CONSTITUENCY_ID INT NOT NULL REFERENCES CONSTITUENCY(CONSTITUENCY_ID),
 CONSTRAINT ELECTIONTYPE_CONSTITUENCY_ID PRIMARY KEY (ELECTIONTYPE_ID, CONSTITUENCY_ID)   
);

-- create table electionType_state
CREATE TABLE ELECTIONTYPE_STATES(
 ELECTIONTYPE_ID INT NOT NULL REFERENCES ELECTIONTYPE(ELECTIONTYPE_ID),
 STATE_ID INT NOT NULL REFERENCES STATES(STATE_ID),
 CONSTRAINT ELECTIONTYPE_STATES_ID PRIMARY KEY (STATE_ID, ELECTIONTYPE_ID)   
);

-- create table election_electionType
CREATE TABLE ELECTION_ELECTIONTYPE(
 ELECTION_ID INT NOT NULL REFERENCES ELECITON(ELECTION_ID),
 ELECTIONTYPE_ID INT NOT NULL REFERENCES ELECTIONTYPE(ELECTIONTYPE_ID),
 CONSTRAINT ELECTION_ELECTIONTYPE_ID PRIMARY KEY (ELECTION_ID, ELECTIONTYPE_ID)   
);

-- create table election_state
CREATE TABLE ELECTION_STATES(
 ELECTION_ID INT NOT NULL REFERENCES ELECITON(ELECTION_ID),
 STATE_ID INT NOT NULL REFERENCES STATES(STATE_ID),
 CONSTRAINT ELECTION_STATES_ID PRIMARY KEY (ELECTION_ID, STATE_ID)   
);


-- create table state_constituency
-- CREATE TABLE STATES_CONSTITUENCY(
--  STATE_ID INT NOT NULL REFERENCES STATES(STATE_ID),
--  CONSTITUENCY_ID INT NOT NULL REFERENCES CONSTITUENCY(CONSTITUENCY_ID),
--  CONSTRAINT STATES_CONSTITUENCY_ID PRIMARY KEY (STATE_ID, CONSTITUENCY_ID)   
-- );
-- create table party_candidate
-- CREATE TABLE PARTY_CANDIDATE(
--  PARTY_ID INT NOT NULL REFERENCES PARTY(PARTY_ID),
--  CANDIDATE_ID INT NOT NULL REFERENCES CANDIDATE(CANDIDATE_ID),
--  CONSTRAINT PARTY_CANDIDATE_ID PRIMARY KEY (PARTY_ID, CANDIDATE_ID)   
-- );

-- create table contituency_candidate
-- CREATE TABLE CONSTITUENCY_CANDIDATE(
--  CONSTITUENCY_ID INT NOT NULL REFERENCES CONSTITUENCY(CONSTITUENCY_ID),
--  CANDIDATE_ID INT NOT NULL REFERENCES CANDIDATE(CANDIDATE_ID),
--  CONSTRAINT CONSTITUENCY_CANDIDATE_ID PRIMARY KEY (CONSTITUENCY_ID, CANDIDATE_ID)   
-- );