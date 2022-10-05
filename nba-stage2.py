from bs4 import BeautifulSoup
import requests
import json

# SCRAPING FGA
url = "https://www.teamrankings.com/nba/player-stat/field-goals-attempted"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')


jockDict = dict()

for list in lists:
  name = list.find('td', class_="text-left")
  fga = list.find('td', class_="text-right")
  if name is not None and fga is not None:
    nameText = name.text.strip()
    fgaText = float(fga.text)
    fgaScore = 0
    if fgaText >= 15:
      fgaScore = 3
    elif fgaText >= 10.5 and fgaText < 15:
      fgaScore = 2
    elif fgaText >= 8.5 and fgaText < 10.5:
      fgaScore = 1
    # else:
    #   jockDict[nameText] = 0
    jockDict[nameText] = fgaScore

    # jockDict[nameText] = {"fga" : fgaText}



# SCRAPING EFG %
url = "https://www.teamrankings.com/nba/player-stat/efg-percentage"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')

for list in lists:
  name = list.find('td', class_="text-left")
  efgP = list.find('td', class_="text-right")
  if name is not None and efgP is not None:
    nameText = name.text.strip()
    efgPText = float(efgP.text[:-1])
    efgPScore = 0
    if efgPText >= 60:
      efgPScore = 3
    elif efgPText >= 50 and efgPText < 60:
      efgPScore = 2
    elif efgPText >= 40 and efgPText < 50:
      efgPScore = 1

    if nameText in jockDict:
      jockDict[nameText] = jockDict[nameText] + efgPScore
    else:
      jockDict[nameText] = efgPScore



# SCRAPING 3 PT ATTEMPT RATE







# SCRAPING 3 PT FG %
url = "https://www.teamrankings.com/nba/player-stat/three-point-field-goal-percentage"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')

for list in lists:
  name = list.find('td', class_="text-left")
  threePtFgP = list.find('td', class_="text-right")
  if name is not None and efgP is not None:
    nameText = name.text.strip()
    threePtFgPText = float(threePtFgP.text[:-1])
    threePtFgPScore = 0
    if threePtFgPText >= 40:
      threePtFgPScore = 2
    elif threePtFgPText >= 36 and threePtFgPText < 40:
      threePtFgPScore = 2

    if nameText in jockDict:
      jockDict[nameText] = jockDict[nameText] + threePtFgPScore
    else:
      jockDict[nameText] = threePtFgPScore



# SCRAPING FT ATTEMPT RATE







# SCRAPING FT %
url = "https://www.teamrankings.com/nba/player-stat/free-throw-percentage"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')

for list in lists:
  name = list.find('td', class_="text-left")
  freeThrowP = list.find('td', class_="text-right")
  if name is not None and efgP is not None:
    nameText = name.text.strip()
    freeThrowPText = float(freeThrowP.text[:-1])
    freeThrowPScore = 0
    if freeThrowPText >= 85:
      freeThrowPScore = 3
    elif freeThrowPText >= 75 and freeThrowPText < 85:
      freeThrowPScore = 2
    elif efgPText >= 70 and efgPText < 75:
      freeThrowPScore = 1

    if nameText in jockDict:
      jockDict[nameText] = jockDict[nameText] + freeThrowPScore
    else:
      jockDict[nameText] = freeThrowPScore

print(jockDict)