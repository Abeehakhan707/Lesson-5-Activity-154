import pandas as pd
import numpy as np
from datetime import datetime
import sqlite3

database = "database.sqlite"
conn = sqlite3.connect(database)

team = pd.read_sql("""SELECT * FROM Team;""", conn)
print(team)

season = pd.read_sql("""SELECT * FROM Season;""", conn)
print(season)

csk_details = pd.read_sql("""
SELECT 
    Match_ID,
    Team_2 AS away_Team,
    Toss_Winner,
    Match_Winner
FROM Match
WHERE Team_1 = 3 
AND Season_ID = 8
""", conn)

print(csk_details)

match_run = pd.read_sql("""
SELECT 
    Match_ID,
    Runs_Scored AS Total_runs,
    Innings_No
FROM Batsman_Scored
WHERE Runs_Scored > 5
AND Match_ID IN (
    SELECT Match_ID
    FROM Match
    WHERE Team_1 = 3
    AND Season_ID = 8
)
""", conn)

print(match_run)

avg_run = pd.read_sql("""
SELECT 
    Match_ID,
    Runs_Scored AS Total_runs,
    Innings_No
FROM Batsman_Scored
WHERE Innings_No = 1
AND Runs_Scored > (
    SELECT AVG(Runs_Scored)
    FROM Batsman_Scored
)
""", conn)

print(avg_run)

conn.close()