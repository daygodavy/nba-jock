from bs4 import BeautifulSoup
from numpy import NaN
from csv import writer
import requests
import json

# NOTE!!! STAGE 1 PART 1 - PLAYER PROJECTED POINTS
# NOTE!!! STAGE 2

# request for per game stats
# NOTE: CHANGE LINK FOR NEW/CURRENT SEASON
url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find('tbody')

rows = lists.find_all('tr', class_="full_table")

jockDict1 = dict()
jockDict2 = dict()
playerNames = []
playerTeams = []
playerStage1FPS = []
playerStage2 = []
playerFinal = []



# check if string is a float
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# creating csv to write player data into
with open('stage1-part1-stage2.csv', 'w', encoding='utf8', newline='') as f:
  thewriter = writer(f)
  header = ['Player', 'Player Team', 'Stage 1: FPS', 'Stage 2']
  thewriter.writerow(header)

  # STAGE 1:
  for row in rows:
    fpsPoints = 0
    if row is not None:
      # scrape player name
      playerName = row.find('td', class_="left").text
      playerPPG = row.find('td', {'data-stat' : 'pts_per_g'}).text
      if is_number(playerPPG):
        playerPPG = float(playerPPG)

      playerRPG = row.find('td', {'data-stat' : 'trb_per_g'}).text
      if is_number(playerRPG):
        playerRPG = float(playerRPG) * 1.25

      playerAPG = row.find('td', {'data-stat' : 'ast_per_g'}).text
      if is_number(playerAPG):
        playerAPG = float(playerAPG) * 1.5

      playerBPG = row.find('td', {'data-stat' : 'blk_per_g'}).text
      if is_number(playerBPG):
        playerBPG = float(playerBPG) * 2

      playerSPG = row.find('td', {'data-stat' : 'stl_per_g'}).text
      if is_number(playerSPG):
        playerSPG = float(playerSPG) * 2
      
      player3PMPG = row.find('td', {'data-stat' : 'fg3_per_g'}).text
      if is_number(player3PMPG):
        player3PMPG = float(player3PMPG) * 0.5

      playerTOPG = row.find('td', {'data-stat' : 'tov_per_g'}).text
      if is_number(playerTOPG):
        playerTOPG = float(playerTOPG) * (-0.5)

      playerTeam = row.find('td', {'data-stat' : 'team_id'}).text
      if playerTeam == 'CHO':
        playerTeam = 'CHA'

      fps = playerPPG + playerRPG + playerAPG + playerBPG + playerSPG + player3PMPG + playerTOPG
      stageScore1 = [playerName, fps]
      jockDict1[playerName] = [fps]
      # thewriter.writerow(stageScore1)
      # print(playerName + ": " + playerTeam)
      playerTeams.append(playerTeam)
      playerNames.append(playerName)
      playerStage1FPS.append(fps)
      


  # STAGE 2:
  for row in rows:
    totalPoints = 0
    if row is not None:
      # scrape player name
      playerName = row.find('td', class_="left").text

      # tallying criteria points for FGA per game
      playerFGA = row.find('td', {'data-stat' : 'fga_per_g'}).text
      if is_number(playerFGA):
        playerFGA = float(playerFGA)
        if playerFGA >= 15:
          totalPoints += 3
        elif playerFGA >= 10.5 and playerFGA < 15:
          totalPoints += 2
        elif playerFGA >= 8.5 and playerFGA < 10.5:
          totalPoints += 1

      # tallying criteria points for EFG% per game
      playerEFG = row.find('td', {'data-stat' : 'efg_pct'}).text
      if is_number(playerEFG):
        playerEFG = float(playerEFG)
        if playerEFG >= 0.60:
          totalPoints += 3
        elif playerEFG >= 0.50 and playerEFG < 0.60:
          totalPoints += 2
        elif playerEFG >= 0.40 and playerEFG < 0.50:
          totalPoints += 1
      
      # tallying criteria points for 3PT% per game
      player3PP = row.find('td', {'data-stat' : 'fg3_pct'}).text
      if is_number(player3PP):
        player3PP = float(player3PP)
        if player3PP >= 0.40:
          totalPoints += 2
        elif player3PP >= 0.36 and player3PP < 0.40:
          totalPoints += 1

      # tallying criteria points for FT% per game
      playerFTP = row.find('td', {'data-stat' : 'ft_pct'}).text
      if is_number(playerFTP):
        playerFTP = float(playerFTP)
        if playerFTP >= 0.85:
          totalPoints += 3
        elif playerFTP >= 0.75 and playerFTP < 0.85:
          totalPoints += 2
        elif playerFTP >= 0.70 and playerFTP < 0.75:
          totalPoints += 1

      jockDict2[playerName] = totalPoints

  # print(jockDict2)
  # exit()


  # request for advanced stats
  url = "https://www.basketball-reference.com/leagues/NBA_2023_advanced.html"
  page = requests.get(url)

  soup = BeautifulSoup(page.content, 'html.parser')

  lists = soup.find('tbody')

  rows = lists.find_all('tr', class_="full_table")

  for row in rows:
    totalPoints = 0
    if row is not None:
      # scrape player name
      playerName = row.find('td', class_="left").text

      # tallying criteria points for 3 PT attempt rate
      player3PAR = row.find('td', {'data-stat' : 'fg3a_per_fga_pct'}).text
      if is_number(player3PAR):
        player3PAR = float(player3PAR)
        if player3PAR >= 0.50:
          totalPoints += 2
        elif player3PAR >= 0.35 and player3PAR < 0.50:
          totalPoints += 1

      # tallying criteria points for FT attempt rate
      playerFTAR = row.find('td', {'data-stat' : 'fta_per_fga_pct'}).text
      if is_number(playerFTAR):
        playerFTAR = float(playerFTAR)
        if playerFTAR >= 0.30:
          totalPoints += 2
        elif playerFTAR >= 0.20 and playerFTAR < 0.30:
          totalPoints += 1

      # tallying criteria points for player efficiency rating
      playerER = row.find('td', {'data-stat' : 'per'}).text
      if is_number(playerER):
        playerER = float(playerER)
        if playerER >= 22.5:
          totalPoints += 2
        elif playerER >= 19.2 and playerER < 22.5:
          totalPoints += 1

      # tallying criteria points for total rebound %
      playerTRP = row.find('td', {'data-stat' : 'trb_pct'}).text
      if is_number(playerTRP):
        playerTRP = float(playerTRP)
        if playerTRP >= 17.5:
          totalPoints += 2
        elif playerTRP >= 12.5 and playerTRP < 17.5:
          totalPoints += 1

      # tallying criteria points for assist %
      playerAP = row.find('td', {'data-stat' : 'ast_pct'}).text
      if is_number(playerAP):
        playerAP = float(playerAP)
        if playerAP >= 33:
          totalPoints += 3
        elif playerAP >= 23.5 and playerAP < 33:
          totalPoints += 2
        elif playerAP >= 19 and playerAP < 23.5:
          totalPoints += 1

      # tallying criteria points for steal %
      playerSP = row.find('td', {'data-stat' : 'stl_pct'}).text
      if is_number(playerSP):
        playerSP = float(playerSP)
        if playerSP >= 2.5:
          totalPoints += 2
        elif playerSP >= 1.8 and playerSP < 2.5:
          totalPoints += 1

      # tallying criteria points for block %
      playerBP = row.find('td', {'data-stat' : 'blk_pct'}).text
      if is_number(playerBP):
        playerBP = float(playerBP)
        if playerBP >= 5.8:
          totalPoints += 2
        elif playerBP >= 4.15 and playerBP < 5.8:
          totalPoints += 1

      # tallying criteria points for turnover %
      playerTOP = row.find('td', {'data-stat' : 'tov_pct'}).text
      if is_number(playerTOP):
        playerTOP = float(playerTOP)
        if playerTOP <= 10:
          totalPoints += 2
        elif playerTOP > 10 and playerTOP <= 13.5:
          totalPoints += 1

      # tallying criteria points for usage %
      playerUP = row.find('td', {'data-stat' : 'usg_pct'}).text
      if is_number(playerUP):
        playerUP = float(playerUP)
        if playerUP >= 25:
          totalPoints += 3
        elif playerUP >= 21.5 and playerUP < 25:
          totalPoints += 2
        elif playerUP >= 18.5 and playerUP < 21.5:
          totalPoints += 1


      if playerName in jockDict2:
        jockDict2[playerName] = jockDict2[playerName] + totalPoints
      else:
        jockDict2[playerName] = totalPoints
      
      stageScore2 = (jockDict2[playerName] / 31) * 100

      info = [ stageScore2]
      # thewriter.writerow(info)

      playerStage2.append(stageScore2)


      # print(info)
  playerFinal = list(zip(playerNames, playerTeams, playerStage1FPS, playerStage2))
  
  # print(list(playerFinal))
  # print(playerFinal)

  for player in playerFinal:
    thewriter.writerow(player)
  # print(jockDict)



    





    