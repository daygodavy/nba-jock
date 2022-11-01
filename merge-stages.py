from bs4 import BeautifulSoup
from numpy import NaN
import csv
import requests
import json
import pandas as pd
  

in_1_name = "stage1-part3.csv"
in_2_name = "stage1-part1-stage2.csv"
in_3_name = "stage3.csv"
out_name = "jock-nba-final.csv"

with open(in_1_name) as in_1, open(in_2_name) as in_2, open(in_3_name) as in_3, open(out_name, 'w') as out:
    reader1 = csv.reader(in_1, delimiter=";")
    reader2 = csv.reader(in_2, delimiter=";")
    reader3 = csv.reader(in_3, delimiter=";")
    writer = csv.writer(out, delimiter=";")
    # for row1 in reader1:
    #   print(row1)
    #   print("=====")

    idx = 0
    for row2 in reader2:
      if reader1[idx] and reader3[idx]:
        writer.writerow(reader1[idx] + row2 + reader3[idx])
      else:
        print("NO")

      # row1 = reader1[idx]
      # row3 = reader3[idx]
      # writer.writerow(row1 + row2 + row3)
      idx +=1

    # for row1, row2, row3 in zip(reader1, reader2, reader3):
    #     print(row2)
    #     writer.writerow(row1 + row2 + row3)

        # print(row2)
        # print(row3)
        

    # for row1, row2, row3 in zip(reader1, reader2, reader3):
    #     print(row1)
    #     print(row2)
    #     print(row3)
    #     print("\n")
      # if row1[0] and row2[0] and row3[0]:
      #   print(row1[0])
      #   print(row2[0])
      #   print(row3[0])
      #   print("\n")
        # writer.writerow([row1[0], row2[0], row3[0]])


# !!! import csv

# in_1_name = "/home/julien/input.csv"
# in_2_name = "/home/julien/excel/output.csv"
# out_name = "/home/julien/excel/merged.csv"

# with open(in_1_name) as in_1, open(in_2_name) as in_2, open(out_name, 'w') as out:
#     reader1 = csv.reader(in_1, delimiter=";")
#     reader2 = csv.reader(in_2, delimiter=";")
#     writer = csv.writer(out, delimiter=";")
#     for row1, row2 in zip(reader1, reader2):
#         if row1[0] and row2[0]:
#             writer.writerow([row1[0], row2[0]])








# data1 = pd.read_csv('stage1-part3.csv')
# data2 = pd.read_csv('stage1-part1-stage2.csv')
# data3 = pd.read_csv('stage3.csv')

# finalStages = data1.merge(data2, how='cross')
# finalStages = finalStages.merge(data3, how='cross')

# print(finalStages)

# # finalCsv = finalStages.to_csv(header=False)


# print(type(finalStages))
# # df = pd.DataFrame(finalCsv)

# with open('nba-jock-stages.csv', 'w') as csv_file:
#     finalStages.to_csv(path_or_buf=csv_file)

# # ~~ reading csv files
# data1 = pd.read_csv('datasets/loan.csv')
# data2 = pd.read_csv('datasets/borrower.csv')
  
# # using merge function by setting how='left'
# output2 = pd.merge(data1, data2, 
#                    on='LOAN_NO', 
#                    how='left')
  
# # displaying result
# print(output2)
