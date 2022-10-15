from bs4 import BeautifulSoup
from numpy import NaN
from csv import writer
import requests
import json

# NOTE!!! STAGE 2


# Stage 3
# ! ! Opp Total Reb/G 
# ! • Opp Off Reb %
# ! • Block % 
# • Steals per Possession
# • Assists per Possession
# • TO per Possession
# • Defensive Efficiency
# • Opponent Floor %
# • Opponent % Points from 3
# • Opponent EFG %
# • Opp 3P %
# • Opp FGA/G
# • Opp 3P rate
# • Opp FTA per FGA


# ***This is the scoring for the above categories**
# 19 or Lower = 3 Points
# • Between 15-18 = 2 Points
# • Between 11-14 = 1 Point
# • Top 10 = 0 Points

stage3FPS = dict()


def setUrl(link):
  page = requests.get(link)
  soup = BeautifulSoup(page.content, 'html.parser')
  lists = soup.find('tbody')
  rows = lists.find_all('tr')
  return rows

def computeFPS():
  rank = 1
  for row in rows:
    teamName = row.find('td', class_='text-left nowrap').text
    if teamName not in stage3FPS:
      stage3FPS[teamName] = 0

    if rank >= 19:
      stage3FPS[teamName] += 3
    elif rank >= 15 and rank < 19:
      stage3FPS[teamName] += 2
    elif rank >= 11 and rank  < 15:
      stage3FPS[teamName] += 1

    rank += 1

# ~ OPP TOTAL REB/G
# url = "https://www.teamrankings.com/nba/stat/opponent-total-rebounds-per-game"
rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-total-rebounds-per-game")
computeFPS()

print(stage3FPS)
print("\n\n")

# ~ OPP OFF REB %
rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-offensive-rebounding-pct")
computeFPS()

# ~ BLOCK %
rows = setUrl("https://www.teamrankings.com/nba/stat/block-pct")
computeFPS()

# ~ STEALS PER POSSESSION (Steals per defensive play)
rows = setUrl("https://www.teamrankings.com/nba/stat/steal-pct")
computeFPS()

# ~ ASSISTS PER POSSESSION
rows = setUrl("https://www.teamrankings.com/nba/stat/assists-per-possession")
computeFPS()

# ~ TO PER POSSESSION
rows = setUrl("https://www.teamrankings.com/nba/stat/turnovers-per-possession")
computeFPS()

# ~ DEFENSIVE EFFICIENCY
rows = setUrl("https://www.teamrankings.com/nba/stat/defensive-efficiency")
computeFPS()

# ~ OPP FLOOR %
rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-floor-percentage")
computeFPS()

# ~ OPP % PTS FROM 3
rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-percent-of-points-from-3-pointers")
computeFPS()

# ~ OPP EFG %
rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-effective-field-goal-pct")
computeFPS()

# ~ OPP 3 PT %
rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-three-point-pct")
computeFPS()

# ~ OPP FGA/G
rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-field-goals-attempted-per-game")
computeFPS()

# ~ OPP 3 PT RATE
rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-three-point-rate")
computeFPS()

# ~ OPP FTA PER FGA
rows = setUrl("https://www.teamrankings.com/nba/stat/opponent-fta-per-fga")
computeFPS()

print(stage3FPS)




