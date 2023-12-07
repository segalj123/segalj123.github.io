from flask import Flask, render_template, request, redirect, url_for
import requests
import random
import os

app = Flask('SportsTrivia', template_folder=os.path.abspath('templates'))
app.secret_key = os.urandom(24)

# Replace this with the actual API endpoint
api_endpoint = 'https://nfl-team-stats1.p.rapidapi.com/teamStats' 

# Your RapidAPI key
rapidapi_key = 'a4a55ae3a2msh1218f6b606d46acp118c3djsnc218d9fd10f3'

team_names = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers', 'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos', 'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars', 'Kansas City Chiefs', 'Las Vegas Raiders', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings', 'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers', 'Tennessee Titans', 'Washington Football Team']

# List to store team stats
team_stats_list = []

# Categories to extract
categories_to_extract = [
    'Standings', 'Defense', 'Scoring Defense', 'Offense', 'Defense Per Game',
    'Scoring', 'Scoring Defense Per Game', 'Offense Per Game', 'Passing Defense',
    'Scoring Per Game', 'Rushing Defense', 'Passing Offense', 'Kicking Against',
    'Rushing Offense', 'Passing Defense Per Game', 'Rushing Defense Per Game',
    'Kicking', 'Kicking Against Per Game', 'Passing Offense Per Game', 'Punting Against',
    'Rushing Offense Per Game', 'Punting Against Per Game', 'Kicking Per Game',
    'Kick And Punt Returns Against', 'Punting', 'Kick And Punt Returns',
    'Conversions Against', 'Kick And Punt Returns Per Game', 'Conversions Against Per Game',
    'Kick And Punt Returns Per Game', 'Drive Averages Against', 'Conversions',
    'Conversions Per Game', 'Drive Averages'
]

# Loop through each team and retrieve statistics
for team_name in team_names:
    headers = {
        'X-RapidAPI-Host': 'nfl-team-stats1.p.rapidapi.com',
        'X-RapidAPI-Key': rapidapi_key
    }

    params = {'team': team_name}
    response = requests.get(api_endpoint, headers=headers, params=params)
    
    if response.status_code == 200:
        team_stats = response.json()
        team_stats_entry = {'team_name': team_name}
        for category in categories_to_extract:
            stats_category = team_stats.get('stats', {}).get(team_name, {}).get(category, {})
            team_stats_entry[category] = stats_category

        # Append team stats entry to the list
        team_stats_list.append(team_stats_entry)
    else:
        print(f"Failed to retrieve statistics for {team_name}. Status code: {response.status_code}")

# Sort the list based on points_scored in descending order
sorted_team_stats = sorted(team_stats_list, key=lambda x: x['Scoring']['Pts'], reverse=True)

@app.route('/')
def index():
    return render_template('index.html', team_stats=sorted_team_stats)

if __name__ == '__main__':
    app.run(debug=True)