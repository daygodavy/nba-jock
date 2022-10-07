from bs4 import BeautifulSoup
from numpy import NaN
from csv import writer
import requests
import json

# check if string is a float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# request for team - player matchup stats
url = "https://www.fantasypros.com/daily-fantasy/nba/defense-vs-position.php"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find('tbody')

# TEAM VS PG
rows = lists.find_all('tr', class_="GC-0 PG")

teamVsPos = []
teamNames = []
teamStats = []

for row in rows:
  team = row.find_all('td')
  
  teamName = row.find('td', class_="left team-cell")
  teamNames.append(teamName.text[3:])
  
  temp = []
  for stat in team:
    if is_number(stat.text):
      temp.append(float(stat.text))

  teamStats.append(temp)


teamVsPos = list(zip(teamNames, teamStats))
# print(teamVsPos)










# FPS =
# PTS + (1.25*REB) + (1.5*AST) + (2*BLK) + (2*STL) + (0.5*3PM) + (-0.5*TO)