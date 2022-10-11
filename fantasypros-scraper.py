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


# # scrape team names
# def scrapeTeamNames(s):
#   for row in rows:
#     team = row.find_all('td')
    
#     # scraping team names and storing in list
#     teamName = row.find('td', class_="left team-cell")
#     teamNames.append(teamName.text[3:])
    


# # scrape team vs pos stats per team
# def scrapeStats(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False

# # check compute FPS for team vs pos
# def computeFPS(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False



        

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

# creating csv to write player data into
with open('nba-jock-matchups.csv', 'w', encoding='utf8', newline='') as f:
  thewriter = writer(f)
  # header = ['PG', 'SG', 'Stage 2']
  # thewriter.writerow(header)

  # scraping through team stats for each team vs PG
  for row in rows:
    team = row.find_all('td')
    
    # scraping team names and storing in list
    teamName = row.find('td', class_="left team-cell")
    teamNames.append(teamName.text[3:])
    
    # scraping team vs PG stats for each team and storing in list of lists
    temp = []
    for stat in team:
      if is_number(stat.text):
        temp.append(float(stat.text))
    teamStats.append(temp)

  teamVsPos = list(zip(teamNames, teamStats))
  # print(teamVsPos)

  fps = 0
  for team in teamVsPos:
    currTeam = team[1]
    fps = currTeam[0] + (currTeam[1] * 1.25) + (currTeam[2] * 1.5) + (currTeam[3] * 0.5) + (currTeam[4] * 2) + (currTeam[5] * 2) + (currTeam[6] * -0.5)
    # print(fps)
    teamFps.append(fps)
  

  print(list(zip(teamNames, teamFps)))








  # NOTE: COMPUTING TEAM VS SG
  teamVsPos = []
  teamStats = []
  teamFps = []
  
  rows = lists.find_all('tr', class_="GC-0 SG")


# scraping through team stats for each team vs PG
  for row in rows:
    team = row.find_all('td')

    # scraping team vs PG stats for each team and storing in list of lists
    temp = []
    for stat in team:
      if is_number(stat.text):
        temp.append(float(stat.text))
    teamStats.append(temp)
  
  teamVsPos = list(zip(teamNames, teamStats))
  # print(teamVsPos)

  fps = 0
  for team in teamVsPos:
    currTeam = team[1]
    fps = currTeam[0] + (currTeam[1] * 1.25) + (currTeam[2] * 1.5) + (currTeam[3] * 0.5) + (currTeam[4] * 2) + (currTeam[5] * 2) + (currTeam[6] * -0.5)
    # print(fps)
    teamFps.append(fps)

  # print(list(zip(teamNames, teamFps)))









  # NOTE: COMPUTING TEAM VS SF
  teamVsPos = []
  teamStats = []
  teamFps = []
  
  rows = lists.find_all('tr', class_="GC-0 SF")


# scraping through team stats for each team vs PG
  for row in rows:
    team = row.find_all('td')

    # scraping team vs PG stats for each team and storing in list of lists
    temp = []
    for stat in team:
      if is_number(stat.text):
        temp.append(float(stat.text))
    teamStats.append(temp)
  
  teamVsPos = list(zip(teamNames, teamStats))
  # print(teamVsPos)

  fps = 0
  for team in teamVsPos:
    currTeam = team[1]
    fps = currTeam[0] + (currTeam[1] * 1.25) + (currTeam[2] * 1.5) + (currTeam[3] * 0.5) + (currTeam[4] * 2) + (currTeam[5] * 2) + (currTeam[6] * -0.5)
    # print(fps)
    teamFps.append(fps)

  # print(list(zip(teamNames, teamFps)))



  

  # NOTE: COMPUTING TEAM VS PF
  teamVsPos = []
  teamStats = []
  teamFps = []
  
  rows = lists.find_all('tr', class_="GC-0 PF")


# scraping through team stats for each team vs PG
  for row in rows:
    team = row.find_all('td')

    # scraping team vs PG stats for each team and storing in list of lists
    temp = []
    for stat in team:
      if is_number(stat.text):
        temp.append(float(stat.text))
    teamStats.append(temp)
  
  teamVsPos = list(zip(teamNames, teamStats))
  # print(teamVsPos)

  fps = 0
  for team in teamVsPos:
    currTeam = team[1]
    fps = currTeam[0] + (currTeam[1] * 1.25) + (currTeam[2] * 1.5) + (currTeam[3] * 0.5) + (currTeam[4] * 2) + (currTeam[5] * 2) + (currTeam[6] * -0.5)
    # print(fps)
    teamFps.append(fps)

  # print(list(zip(teamNames, teamFps)))



    # NOTE: COMPUTING TEAM VS PF
  teamVsPos = []
  teamStats = []
  teamFps = []
  
  rows = lists.find_all('tr', class_="GC-0 C")


# scraping through team stats for each team vs PG
  for row in rows:
    team = row.find_all('td')

    # scraping team vs PG stats for each team and storing in list of lists
    temp = []
    for stat in team:
      if is_number(stat.text):
        temp.append(float(stat.text))
    teamStats.append(temp)
  
  teamVsPos = list(zip(teamNames, teamStats))
  # print(teamVsPos)

  fps = 0
  for team in teamVsPos:
    currTeam = team[1]
    fps = currTeam[0] + (currTeam[1] * 1.25) + (currTeam[2] * 1.5) + (currTeam[3] * 0.5) + (currTeam[4] * 2) + (currTeam[5] * 2) + (currTeam[6] * -0.5)
    # print(fps)
    teamFps.append(fps)

  # print(list(zip(teamNames, teamFps)))






  # FPS =
  # PTS + (1.25*REB) + (1.5*AST) + (0.5*3PM) + (2*STL) + (2*BLK) + (-0.5*TO)