# -*- coding: utf-8 -*-
"""premierleague 크롤링

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YBP0apkk_G-hHmlg57xSAWnkKQt_rgaR
"""

from google.colab import drive
drive.mount('/content/drive')

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.premierleague.com/tables"

team_list = [] #팀 저장 리스트
goal_list = [] #팀 득점과 실점 저장 리스트
win_score_list = [] #승점 저장 리스트

def get_team():
  resp = requests.get(url)

  soup = BeautifulSoup(resp.text)
  team = soup.find_all('td', {'class' : 'team'})

  for i in team:
    team_list.append(i.get_text())

  print(team_list)

def get_goal():
  resp = requests.get(url)

  soup = BeautifulSoup(resp.text)
  goal = soup.find_all('td', {'class' : 'hideSmall'})

  for s in goal:
    goal_list.append(s.get_text().replace('\r',''))

  print(goal_list)

def get_win():
  resp = requests.get(url)

  soup = BeautifulSoup(resp.text)
  win = soup.find_all('td', {'class' : 'points'})

  for s in win:
    win_score_list.append(s.get_text().replace('\r',''))

  print(win_score_list)

get_team()

get_goal()

get_win()

total_list = [0 for _ in range(len(team_list))]

for c in range(0, len(team_list)):
  sum_list = []
  sum_list.append(team_list[c])
  sum_list.append(goal_list[c*2])
  sum_list.append(goal_list[c*2+1])
  sum_list.append(win_score_list[c])

  total_list[c] = sum_list

print(total_list)

df = pd.DataFrame(total_list)

df.columns = ['team','goals scored','goals conceded','win score']

df.to_csv('/content/drive/MyDrive/Colab Notebooks/202121224_강지웅_premierleague.csv')

print(df)

