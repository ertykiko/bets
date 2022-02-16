from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


web = "https://www.betclic.pt/futebol-s1"
path = "C:/Users/Francisco/Documents/bets/chromedriver.exe"
teams = []
x12 = []  # 3-way
odds_events = []

driver = webdriver.Chrome(path)

driver.get(web)
events = []

events = driver.find_elements(By.CLASS_NAME, 'ng-star-inserted')

#Find single row
for match in events:
    odds_event = match.find_elements(
        By.CLASS_NAME, 'market_odds ng-star-inserted')
    odds_event.append(odds_event)

    #teams
    for team in match.find_elements(By.CLASS_NAME, 'scoreboard_contestantLabel'):
        teams.append(team.text)


