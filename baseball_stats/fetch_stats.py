# Import required libraries
from pybaseball import team_game_logs, statcast_pitcher
import pandas as pd
import os

# Save the output to your GitHub project folder
output_folder = os.path.join(os.getcwd(), 'data')  # Adjust if needed

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get team game logs for the last month
def get_team_logs(team, start_date, end_date, log_type='pitching'):
    game_logs = team_game_logs(team, start_date, end_date, log_type=log_type)
    return game_logs[['Date', 'Opp', 'Result', 'W/L', 'ERA']]

# Get pitcher stats for the last month
def get_pitcher_stats(pitcher_name, start_date, end_date):
    from pybaseball import playerid_lookup

    # Lookup pitcher ID
    player_id = playerid_lookup(pitcher_name.split(' ')[1], pitcher_name.split(' ')[0])
    mlb_id = player_id.iloc[0]['key_mlbam']

    # Get pitcher stats from Statcast
    pitcher_stats = statcast_pitcher(start_date, end_date, mlb_id)
    return pitcher_stats[['game_date', 'pitch_type', 'release_speed', 'release_spin_rate', 'p_throws', 'home_team', 'away_team', 'outs_when_up', 'inning', 'release_extension', 'game_pk', 'pitcher']]

# Example usage
if __name__ == '__main__':
    team_name = 'BOS'  # Boston Red Sox
    pitcher_name = 'Clayton Kershaw'
    start_date = '2023-08-01'
    end_date = '2023-09-01'

    # Fetch team logs
    print(f"Fetching team game logs for {team_name}")
    team_logs = get_team_logs(team_name, start_date, end_date)
    team_logs.to_csv(os.path.join(output_folder, f'{team_name}_game_logs.csv'), index=False)
    print(team_logs)

    # Fetch pitcher stats
    print(f"\nFetching pitcher stats for {pitcher_name}")
    pitcher_stats = get_pitcher_stats(pitcher_name, start_date, end_date)
    pitcher_stats.to_csv(os.path.join(output_folder, f'{pitcher_name}_stats.csv'), index=False)
    print(pitcher_stats)
