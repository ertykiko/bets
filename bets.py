from typing import Counter
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.betclic.pt/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

counter = 0
home_teams = []
away_teams = []
home_odds = []
away_odds = []
tie_odds= []



#Get the names of the home and away teams 
""" for teams in soup.find_all('div', attrs={'class': 'scoreboard_contestantLabel'}):
    if(counter%2==0):
        home_teams.append(teams.text.strip()) 
    else:
        away_teams.append(teams.text.strip())
    counter += 1 """

#Get the odds for thoose teams
counter = 0

for odd in soup.find_all('div', attrs={'class': 'oddButtonWrapper prebootFreeze ng-trigger ng-trigger-oddsStateAnimation'}, limit=3):  
    if(counter % 3 == 0):
        home_odds.append(odd.text.strip())
    elif(counter % 2 == 0):
        away_odds.append(odd.text.strip())
    else:
        tie_odds.append(odd.text.strip())
    counter += 1


print(home_odds)
print(tie_odds)
print(away_odds)
