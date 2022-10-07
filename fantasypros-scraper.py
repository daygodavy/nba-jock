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
teamFps = []

# creating csv to write player data into
with open('nba-jock-matchups.csv', 'w', encoding='utf8', newline='') as f:
  thewriter = writer(f)
  # header = ['PG', 'SG', 'Stage 2']
  # thewriter.writerow(header)

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

  fps = 0
  for team in teamVsPos:
    # fps = team[1]
    # print(team[1][0])
    currTeam = team[1]
    fps = currTeam[0] + (currTeam[1] * 1.25) + (currTeam[2] * 1.5) + (currTeam[3] * 0.5) + (currTeam[4] * 2) + (currTeam[5] * 2) + (currTeam[6] * -0.5)
    print(fps)
    teamFps.append(fps)
    # fps = team[1]


  print(list(zip(teamNames, teamFps)))
  # TEAM VS SG
  # rows = lists.find_all('tr', class_="GC-0 SG")







  # FPS =
  # PTS + (1.25*REB) + (1.5*AST) + (0.5*3PM) + (2*STL) + (2*BLK) + (-0.5*TO)