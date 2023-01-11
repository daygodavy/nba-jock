from bs4 import BeautifulSoup
from numpy import NaN
import csv
import requests
import json
import pandas as pd
  

df1 = pd.read_csv("stage1-part3.csv")
df2 = pd.read_csv("stage1-part1-stage2.csv")
df3 = pd.read_csv("stage3.csv")
df4 = pd.read_csv("daily-matchups.csv")


playerName = df2['Player'].tolist()
playerTeam = df2['Player Team'].tolist()
homeTeam = df4['Home Team'].tolist()
awayTeam = df4['Away Team'].tolist()
dailyTeams = homeTeam + awayTeam

homeTeamPlayers = []
awayTeamPlayers = []

playerInfo = list(zip(playerName, playerTeam))
playerMatchups = dict()

for player in playerInfo:
  # print(player)
  # print(player[0])
  # print(player[1])
  if player[1] not in playerMatchups:
    playerMatchups[player[1]] = [player[0]]
  else:
    playerMatchups[player[1]].append(player[0])


dailyMatchup = dict()


for team in homeTeam:
  if team in playerMatchups:
    homeTeamPlayers.append(playerMatchups[team])

  
for team in awayTeam:
  if team in playerMatchups:
    awayTeamPlayers.append(playerMatchups[team])  



for roster in homeTeamPlayers:
  opposingTeam = awayTeam.pop(0)
  dailyMatchup[opposingTeam] = roster

for roster in awayTeamPlayers:
  opposingTeam = homeTeam.pop(0)
  dailyMatchup[opposingTeam] = roster


print(dailyMatchup)


# ! NOW MATCHUP HOMETEAMS VS AWAYTEAMPLAYERS AND AWAYTEAMS VS HOMETEAMPLAYERS

# for i in homeTeamPlayers:
#   print(i)



df_final = df1.join(df2, how='right')

df_final = df_final.join(df3, how='left', lsuffix='_left', rsuffix='_right')

df_final.to_csv('jock-nba-final.csv')




# ~ POSSIBLE SOLUTION 1, STACKS THE COLUMNS
# in_1_name = csv.reader(open("stage1-part3.csv", 'r'))
# in_2_name = csv.reader(open("stage1-part1-stage2.csv", 'r'))
# in_3_name = csv.reader(open("stage3.csv", 'r'))
# out_name = csv.writer(open("jock-nba-final.csv", 'w'))

# for i, row in enumerate(in_1_name):
#   out_name.writerow(row)


# for i, row in enumerate(in_2_name):
#   out_name.writerow(row)


# for i, row in enumerate(in_3_name):
#   out_name.writerow(row)