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


# scrape team names
def scrapeTeamNames(rows):
  teamList = []
  for row in rows:
    team = row.find_all('td')
    
    # scraping team names and storing in list
    teamName = row.find('td', class_="left team-cell")
    teamList.append(teamName.text[3:])
  return teamList
    


# scrape team vs pos stats per team
def scrapeStats(currClass):
  # NOTE: COMPUTING TEAM VS POS
  teamVsPos = []
  teamStats = []
  
  rows = lists.find_all('tr', class_= currClass)


  # scraping through team stats for each team vs pos
  for row in rows:
    team = row.find_all('td')

    # scraping team vs pos stats for each team and storing in list of lists
    temp = []
    for stat in team:
      if is_number(stat.text):
        temp.append(float(stat.text))
    teamStats.append(temp)
  
  # teamVsPos = list(zip(teamNames, teamStats))
  return teamStats


# check compute FPS for team vs pos
def computeFPS(allTeams):
  fps = 0
  teamFps = []
  for team in allTeams:
    fps = team[0] + (team[1] * 1.25) + (team[2] * 1.5) + (team[3] * 0.5) + (team[4] * 2) + (team[5] * 2) + (team[6] * -0.5)
    teamFps.append(fps)
    # print(fps)
  return teamFps



        

# request for team - player matchup stats
url = "https://www.fantasypros.com/daily-fantasy/nba/defense-vs-position.php"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find('tbody')

# NOTE: COMPUTING TEAM VS PG
rows = lists.find_all('tr', class_="GC-0 PG")

teamVsPos = []
teamNames = []
teamStats = []
teamFps = []

teamVsPG = []
teamVsSG = []
teamVsSF = []
teamVsPF = []
teamVsC = []

fpsVsPG = []
fpsVsSG = []
fpsVsSF = []
fpsVsPF = []
fpsVsC = []



teamNames = scrapeTeamNames(rows)

# creating csv to write player data into
with open('nba-jock-matchups.csv', 'w', encoding='utf8', newline='') as f:
  thewriter = writer(f)
  header = ['Team', 'PG', 'SG', 'SF', 'PF', 'C']
  thewriter.writerow(header)

  teamVsPG = scrapeStats("GC-0 PG")
  teamVsSG = scrapeStats("GC-0 SG")
  teamVsSF = scrapeStats("GC-0 SF")
  teamVsPF = scrapeStats("GC-0 PF")
  teamVsC = scrapeStats("GC-0 C")

  fpsVsPG = computeFPS(teamVsPG)
  fpsVsSG = computeFPS(teamVsSG)
  fpsVsSF = computeFPS(teamVsSF)
  fpsVsPF = computeFPS(teamVsPF)
  fpsVsC = computeFPS(teamVsC)

  stage1TeamFps = list(zip(teamNames, fpsVsPG, fpsVsSG, fpsVsSF, fpsVsPF, fpsVsC))
  thewriter.writerows(stage1TeamFps)

  # print(list(zip(teamNames, teamFps)))


  # FPS =
  # PTS + (1.25*REB) + (1.5*AST) + (0.5*3PM) + (2*STL) + (2*BLK) + (-0.5*TO)