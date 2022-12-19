from bs4 import BeautifulSoup
from numpy import NaN
from csv import writer
import requests
import json

# nba matchups scraper

stage3FPS = dict()

page = requests.get('https://basketballmonster.com/nbalineups.aspx')
soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('div', class_="container-fluid p-2 m-2 float-left")

for row in lists:
  matchup = row.find('th').text.strip()
  # print(matchup)
  print(matchup[:9])

# def setUrl(link):
#   page = requests.get(link)
#   soup = BeautifulSoup(page.content, 'html.parser')
#   lists = soup.find('tbody')
#   rows = lists.find_all('tr')
#   return rows

# def computeFPS():
#   rank = 1
#   for row in rows:
#     teamName = row.find('td', class_='text-left nowrap').text
#     if teamName not in stage3FPS:
#       stage3FPS[teamName] = 0

#     if rank >= 19:
#       stage3FPS[teamName] += 3
#     elif rank >= 15 and rank < 19:
#       stage3FPS[teamName] += 2
#     elif rank >= 11 and rank  < 15:
#       stage3FPS[teamName] += 1

#     rank += 1


# # ~ OPP TOTAL REB/G
# # url = "https://www.teamrankings.com/nba/stat/opponent-total-rebounds-per-game"
# rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-total-rebounds-per-game")
# computeFPS()


# finalFPS = []
# for key in stage3FPS:
#   stage3FPS[key] = float((stage3FPS[key] / 42) * 100)
#   finalFPS.append([key, stage3FPS[key]])


# with open('stage3.csv', 'w', encoding='utf8', newline='') as f:
#   thewriter = writer(f)
#   header = ['Team', 'Stage 3']
#   thewriter.writerow(header)
#   thewriter.writerows(finalFPS)
  
# # print(finalFPS)




