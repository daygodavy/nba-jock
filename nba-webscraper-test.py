from bs4 import BeautifulSoup
import requests
import json


# SCRAPING PPG
url = "https://www.teamrankings.com/nba/player-stat/points"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')


jockDict = dict()

for list in lists:
  name = list.find('td', class_="text-left")
  ppg = list.find('td', class_="text-right")
  if name is not None and ppg is not None:
    nameText = name.text.strip()
    ppgText = float(ppg.text)
    jockDict[nameText] = {"ppg" : ppgText}


# SCRAPING ASSISTS
url = "https://www.teamrankings.com/nba/player-stat/assists"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')

for list in lists:
  name = list.find('td', class_="text-left")
  assists = list.find('td', class_="text-right")
  if name is not None and assists is not None:
    nameText = name.text.strip()
    assistsText = float(assists.text)
    if nameText in jockDict:
      jockDict[nameText]["assists"] = assistsText
    else:  
      jockDict[nameText] = {"assists" : assistsText}



# SCRAPING REBOUNDS
url = "https://www.teamrankings.com/nba/player-stat/rebounds"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')

for list in lists:
  name = list.find('td', class_="text-left")
  rebounds = list.find('td', class_="text-right")
  if name is not None and rebounds is not None:
    nameText = name.text.strip()
    reboundsText = float(rebounds.text)
    if nameText in jockDict:
      jockDict[nameText]["rebounds"] = reboundsText
    else:  
      jockDict[nameText] = {"rebounds" : reboundsText}



# # SCRAPING STEALS
url = "https://www.teamrankings.com/nba/player-stat/steals"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')

for list in lists:
  name = list.find('td', class_="text-left")
  steals = list.find('td', class_="text-right")
  if name is not None and steals is not None:
    nameText = name.text.strip()
    stealsText = float(steals.text)
    if nameText in jockDict:
      jockDict[nameText]["steals"] = stealsText
    else:  
      jockDict[nameText] = {"steals" : stealsText}


# # SCRAPING BLOCKS
url = "https://www.teamrankings.com/nba/player-stat/blocks"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')

for list in lists:
  name = list.find('td', class_="text-left")
  blocks = list.find('td', class_="text-right")
  if name is not None and blocks is not None:
    nameText = name.text.strip()
    blocksText = float(blocks.text)
    if nameText in jockDict:
      jockDict[nameText]["blocks"] = blocksText
    else:  
      jockDict[nameText] = {"blocks" : blocksText}


# # SCRAPING TURNOVERS
url = "https://www.teamrankings.com/nba/player-stat/turnovers"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('tr')

for list in lists:
  name = list.find('td', class_="text-left")
  turnovers = list.find('td', class_="text-right")
  if name is not None and turnovers is not None:
    nameText = name.text.strip()
    turnoversText = float(turnovers.text)
    if nameText in jockDict:
      jockDict[nameText]["turnovers"] = turnoversText
    else:  
      jockDict[nameText] = {"turnovers" : turnoversText}


# for player in jockDict.keys():
#   print(player)




# print(json.dumps(jockDict, sort_keys=False, indent=4))
# print(jockDict)




