import json

file_path = r'C:\Users\jsegal1\Documents\GitHub\segalj123.github.io\team_stats.json'

# Read JSON data from the file
with open(file_path, 'r') as file:
    json_data = file.read()

# Convert string to Python dict
data = json.loads(json_data)

miami_dolphins_info = {
    'Standings': data['stats']['Miami Dolphins']['Standings'],
    'Defense': data['stats']['Miami Dolphins']['Defense'],
    'Scoring Defense': data['stats']['Miami Dolphins']['Scoring Defense'],
    'Offense': data['stats']['Miami Dolphins']['Offense'],
    'Scoring': data['stats']['Miami Dolphins']['Scoring'],
}

print(json.dumps(miami_dolphins_info, indent=2))