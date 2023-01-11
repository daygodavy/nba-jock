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

currDayMatchups = []


for row in lists:
  matchup = row.find('th').text.strip()
  # print(matchup)
  homeTeam = matchup[0:3]
  awayTeam = matchup[6:9]

  if homeTeam == 'NOR':
    homeTeam = 'NOP'
  elif awayTeam == 'NOR':
    awayTeam = 'NOP'
  currDayMatchups.append([homeTeam, awayTeam])
  # print(matchup[:9])
  # print(matchup[0:3])
  # print(matchup[6:9])
  
print(currDayMatchups)
  




# creating csv to write player data into
with open('daily-matchups.csv', 'w', encoding='utf8', newline='') as f:
  thewriter = writer(f)
  header = ['Home Team', 'Away Team']
  thewriter.writerow(header)
  for team in currDayMatchups:
    thewriter.writerow(team)




#! ATL	- Atlanta Hawks
#! BOS	- Boston Celtics
#! CHA	- Charlotte Hornets
#! CHI	- Chicago Bulls
#! CLE	- Cleveland Cavaliers
#! DAL	- Dallas Mavericks
#! DEN	- Denver Nuggets
#! DET	- Detroit Pistons
#! GSW	- Golden State Warriors
#! HOU -	Houston Rockets
#! IND	- Indiana Pacers
#! LAC -	Los Angeles Clippers
#! LAL	- Los Angeles Lakers
#! MEM	- Memphis Grizzlies
#! MIA	- Miami Heat
#! MIL	- Milwaukee Bucks
#! MIN	- Minnesota Timberwolves
#! NOP	- New Orleans Pelicans
#! NYK	- New York Knicks
#! BKN	- Brooklyn Nets
#! OKC	- Oklahoma City Thunder
#! ORL	- Orlando Magic
#! PHI	- Philadelphia 76ers
#! PHO	- Phoenix Suns
#! POR	- Portland Trail Blazers
#! SAC	- Sacramento Kings
#! SAS - San Antonio Spurs
#! TOR	- Toronto Raptors
#! UTH	- Utah Jazz
#! WAS	- Washington Wizards


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




