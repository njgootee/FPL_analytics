import pandas as pd
import json
import requests

#python script for saving fpl api data from gameweeks 1-27
files = ['events', 'teams', 'elements']

def save_data(file_names):
    d=json.loads(requests.get('https://fantasy.premierleague.com/api/bootstrap-static/').text)
    for i in file_names:
        df=pd.json_normalize(d[i])
        df.to_csv('C:/Users/nath1/Documents/CS/105/project/data/' + i + '.csv')

save_data(files)

def player_gw_data():
    for i in range(1,28):
        d2=json.loads(requests.get('https://fantasy.premierleague.com/api/event/'+str(i)+'/live/').text)
        df=pd.json_normalize(d2['elements'])
        df.to_csv('C:/Users/nath1/Documents/CS/105/project/player_gw/player_gw' + str(i) + '.csv')

player_gw_data()

def fixture_gw_data():
    for i in range (1,28):
        d3=json.loads(requests.get('https://fantasy.premierleague.com/api/fixtures/?event='+str(i)).text)
        df=pd.json_normalize(d3)
        df.to_csv('C:/Users/nath1/Documents/CS/105/project/fixture_gw/fixture_gw'+str(i)+'.csv')

fixture_gw_data()