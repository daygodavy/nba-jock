from bs4 import BeautifulSoup
from numpy import NaN
import csv
import requests
import json
import pandas as pd
  

df1 = pd.read_csv("stage1-part3.csv")
df2 = pd.read_csv("stage1-part1-stage2.csv")
df3 = pd.read_csv("stage3.csv")

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