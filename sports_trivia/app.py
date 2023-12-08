from flask import Flask, render_template, session, redirect, url_for, request
import sys
import pandas as pd
import nfl_data_py as nfl
import random


app = Flask(__name__)
app.secret_key = '14'
app.config['SESSION_TYPE'] = 'filesystem'

# @app.route('/set_session')
# def set_session():
#     session['user_id'] = 1234
#     session['username'] = 'jonathan_segal'
#     return 'Session data set!'

# Add the nfl_data_py package to the system path
sys.path.append(r'C:\Users\jsegal1\Downloads\nfl_data_py-main\nfl_data_py-main\build\lib')

# Import NFL Data Python library on github
import site
import numpy

# Display all site packages- in the program
print(site.getsitepackages())

# Set display options for Pandas
pd.set_option('display.max_columns', None)

# Import NFL data for the 2022 season - all data
df1_2022 = nfl.import_team_desc()
df_2022 = nfl.import_seasonal_data([2022])
df_schedule = nfl.import_schedules([2022])
ids = nfl.import_ids()

# Display player QB stats
qb_passing_columns = [
    'player_id', 'season', 'season_type', 'completions', 'attempts', 'passing_yards', 'passing_tds',
    'interceptions', 'sacks', 'sack_yards', 'passing_air_yards', 'passing_yards_after_catch',
    'passing_first_downs', 'passing_epa', 'passing_2pt_conversions', 'fantasy_points','fantasy_points_ppr'
]
qb_passing_stats = df_2022[qb_passing_columns]

# Display player RB stats
rb_rushing_columns = [
    'player_id', 'season', 'season_type', 'carries', 'rushing_yards', 'rushing_tds',
    'rushing_fumbles', 'rushing_fumbles_lost', 'rushing_first_downs', 'rushing_epa',
    'rushing_2pt_conversions', 'fantasy_points','fantasy_points_ppr'
]
rb_rushing_stats = df_2022[rb_rushing_columns]

wr_te_receiving_columns = [
    'player_id', 'season', 'season_type', 'receptions', 'targets', 'receiving_yards', 'receiving_tds',
    'receiving_fumbles', 'receiving_fumbles_lost', 'receiving_air_yards', 'receiving_yards_after_catch',
    'receiving_first_downs', 'receiving_epa', 'receiving_2pt_conversions', 'racr', 'target_share',
    'air_yards_share', 'wopr_x', 'fantasy_points','fantasy_points_ppr', 'tgt_sh'
]
wr_te_receiving_stats = df_2022[wr_te_receiving_columns]

pk_columns = [
    'player_id','fantasy_points','fantasy_points_ppr'
]
pk_stats = df_2022[pk_columns]

general_stats_columns = [
    'special_teams_tds', 'games', 'ay_sh', 'yac_sh',
    'wopr_y', 'ry_sh', 'rtd_sh', 'rfd_sh', 'rtdfd_sh', 'dom', 'w8dom', 'yptmpa', 'ppr_sh'
]
general_stats = df_2022[general_stats_columns]


# Filter players from the IDs to positions. Match ID to ID in different lists. 
qb_players_ids = ids[ids['position'] == 'QB']
receiver_player_ids = ids[ids['position'] == 'WR']
te_player_ids = ids[ids['position'] == 'TE']
rb_player_ids = ids[ids['position'] == 'RB']
pk_ids = ids[ids['position'] == 'PK']

# Merge stats with player IDs using 'gsis_id' from categories and other list
qb_passing_stats_qb_with_name = pd.merge(qb_passing_stats, qb_players_ids, left_on='player_id', right_on='gsis_id')
receiver_receiving_stats_with_name = pd.merge(wr_te_receiving_stats, receiver_player_ids, left_on='player_id', right_on='gsis_id')
te_receiving_stats_with_name = pd.merge(wr_te_receiving_stats, te_player_ids, left_on='player_id', right_on='gsis_id')
rb_rushing_stats_with_name = pd.merge(rb_rushing_stats, rb_player_ids, left_on='player_id', right_on='gsis_id')
pk_stats_with_name = pd.merge(pk_stats, pk_ids, left_on='player_id', right_on='gsis_id')

# Merge player  stats with team info using 'team_abbr'. Match the last list to the second to get full info on all players. 
qb_passing_stats_qb_with_team = pd.merge(qb_passing_stats_qb_with_name, df1_2022, left_on='team', right_on='team_abbr')
receiver_receiving_stats_wr_with_team = pd.merge(receiver_receiving_stats_with_name, df1_2022, left_on='team', right_on='team_abbr')
te_receiving_stats_te_with_team = pd.merge(te_receiving_stats_with_name, df1_2022, left_on='team', right_on='team_abbr')
rb_rushing_stats_rb_with_team = pd.merge(rb_rushing_stats_with_name, df1_2022, left_on='team', right_on='team_abbr')
pk_stats_pk_with_team = pd.merge(pk_stats_with_name, df1_2022, left_on='team', right_on='team_abbr')

# # Print passing stats for QB players with additional columns from IDs
# print(qb_passing_stats_qb_with_team[
#     ['player_id', 'name', 'position', 'team', 'team_name', 'team_conf', 'team_division', 'completions', 'attempts',
#      'passing_yards', 'passing_tds', 'interceptions', 'sacks', 'sack_yards', 'passing_air_yards',
#      'passing_yards_after_catch', 'passing_first_downs', 'passing_epa', 'passing_2pt_conversions']])

#qb_passing_stats_qb_with_name = pd.merge(qb_passing_stats, qb_players_ids, left_on='player_id', right_on='gsis_id')



# Define a function to generate questions for a given category
def generate_category_question(category_df, category_names):

    # Randomly select a category
    selected_category = random.choice(category_names)
    
    formatted_category = selected_category.replace('_', ' ')

    # Sort the DataFrame by the selected category
    sorted_df = category_df.sort_values(by=selected_category, ascending=False)
    
    # Get the player with the highest value in the randomly selected category
    correct_answer = sorted_df.iloc[0]['name']
    
    # Get the top 15 players in the selected category (excluding the correct answer)
    top_15_players = sorted_df.iloc[1:16]['name'].tolist()

    # Select three random players from the top 15
    other_players = random.sample(top_15_players, 3)

    # Generate the multiple-choice question
    
    question = f"What player in 2022 leads the NFL in {selected_category}?"
    options = [correct_answer] + other_players

    #Print the question and options
    print(selected_category.replace('_', ' '))
    random.shuffle(options)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    print("\nCorrect Answer:", correct_answer)
    print("\n\n")

    return selected_category.replace('_', ' '), options, correct_answer

def generate_and_store_rb_question():
    selected_category = random.choice(['carries', 'rushing_yards', 'rushing_tds',
    'rushing_fumbles', 'rushing_fumbles_lost', 'rushing_first_downs', 'rushing_epa',
    'rushing_2pt_conversions', 'fantasy_points','fantasy_points_ppr'])
    formatted_category = selected_category.replace('_', ' ')

    # Sort the RB rushing stats by the selected category
    sorted_df = rb_rushing_stats_with_name.sort_values(by=selected_category, ascending=False)

    # Get the player with the highest value in the selected category
    correct_answer = sorted_df.iloc[0]['name']

    # Get the top 15 RB players in the selected category (excluding the correct answer)
    top_15_players = sorted_df.iloc[1:16]['name'].tolist()

    # Select three random RB players from the top 15
    other_players = random.sample(top_15_players, 3)

    # Generate the RB multiple-choice question
    question = f"Which RB in 2022 leads the NFL in {formatted_category}?"
    options = [correct_answer] + other_players

    # Store the RB question and answer in the session
    session['questions'].append({'question': question, 'correct_answer': correct_answer})
    session['user_answers'].append({'question': question, 'selected_option': None, 'correct_answer': correct_answer})

    return question.replace('_', ' '), options

def generate_and_store_wr_question():
    selected_category = random.choice(['receptions', 'targets', 'receiving_yards', 'receiving_tds',
    'receiving_fumbles', 'receiving_fumbles_lost', 'receiving_air_yards', 'receiving_yards_after_catch',
    'receiving_first_downs', 'receiving_epa', 'receiving_2pt_conversions', 'racr', 'target_share',
    'air_yards_share', 'wopr_x', 'fantasy_points','fantasy_points_ppr', 'tgt_sh'])

    formatted_category = selected_category.replace('_', ' ')

    # Sort the WR receiving stats by the selected category
    sorted_df = wr_te_receiving_stats_with_name.sort_values(by=selected_category, ascending=False)

    # Get the player with the highest value in the selected category
    correct_answer = sorted_df.iloc[0]['name']

    # Get the top 15 WR players in the selected category (excluding the correct answer)
    top_15_players = sorted_df.iloc[1:16]['name'].tolist()

    # Select three random WR players from the top 15
    other_players = random.sample(top_15_players, 3)

    # Generate the WR multiple-choice question
    question = f"Which WR in 2022 leads the NFL in {formatted_category}?"
    options = [correct_answer] + other_players

    # Store the WR question and answer in the session
    session['questions'].append({'question': question, 'correct_answer': correct_answer})
    session['user_answers'].append({'question': question, 'selected_option': None, 'correct_answer': correct_answer})

    return question.replace('_', ' '), options

def generate_and_store_te_question():
    selected_category = random.choice(['receptions', 'targets', 'receiving_yards', 'receiving_tds',
    'receiving_fumbles', 'receiving_fumbles_lost', 'receiving_air_yards', 'receiving_yards_after_catch',
    'receiving_first_downs', 'receiving_epa', 'receiving_2pt_conversions', 'racr', 'target_share',
    'air_yards_share', 'wopr_x', 'fantasy_points','fantasy_points_ppr', 'tgt_sh'])
    formatted_category = selected_category.replace('_', ' ')

    # Sort the TE receiving stats by the selected category
    sorted_df = wr_te_receiving_stats_with_name.sort_values(by=selected_category, ascending=False)

    # Get the player with the highest value in the selected category
    correct_answer = sorted_df.iloc[0]['name']

    # Get the top 15 TE players in the selected category (excluding the correct answer)
    top_15_players = sorted_df.iloc[1:16]['name'].tolist()

    # Select three random TE players from the top 15
    other_players = random.sample(top_15_players, 3)

    # Generate the TE multiple-choice question
    question = f"Which TE in 2022 leads the NFL in {formatted_category}?"
    options = [correct_answer] + other_players

    # Store the TE question and answer in the session
    session['questions'].append({'question': question, 'correct_answer': correct_answer})
    session['user_answers'].append({'question': question, 'selected_option': None, 'correct_answer': correct_answer})

    return question.replace('_', ' '), options

def generate_and_store_pk_question():
    selected_category = random.choice(['fantasy_points', 'fantasy_points_ppr'])  # You can choose the relevant category for PK
    formatted_category = selected_category.replace('_', ' ')

    # Sort the PK stats by the selected category
    sorted_df = pk_stats_with_name.sort_values(by=selected_category, ascending=False)

    # Get the player with the highest value in the selected category
    correct_answer = sorted_df.iloc[0]['name']

    # Get the top 15 PK players in the selected category (excluding the correct answer)
    top_15_players = sorted_df.iloc[1:16]['name'].tolist()

    # Select three random PK players from the top 15
    other_players = random.sample(top_15_players, 3)

    # Generate the PK multiple-choice question
    question = f"Which PK in 2022 leads the NFL in {formatted_category}?"
    options = [correct_answer] + other_players

    # Store the PK question and answer in the session
    session['questions'].append({'question': question, 'correct_answer': correct_answer})
    session['user_answers'].append({'question': question, 'selected_option': None, 'correct_answer': correct_answer})

    return question.replace('_', ' '), options

# Generate a random question for a random category
categories = ['completions', 'attempts', 'passing_yards', 'passing_tds',
    'interceptions', 'sacks', 'sack_yards', 'passing_air_yards', 'passing_yards_after_catch',
    'passing_first_downs', 'passing_epa', 'passing_2pt_conversions', 'fantasy_points','fantasy_points_ppr']
generate_category_question(qb_passing_stats_qb_with_name, categories)

def initialize_quiz_session():
    session['questions'] = []  # List to store generated questions
    session['user_answers'] = []  # List to store user's answers
    session['score'] = {'correct': 0, 'wrong': 0}  # Dictionary to store the score

def generate_top5_question(category_df, category_names):
    # Randomly select a category
    selected_category = random.choice(category_names)
    
    formatted_category = selected_category.replace('_', ' ')

    # Sort the DataFrame by the selected category
    sorted_df = category_df.sort_values(by=selected_category, ascending=False)
    
    # Get the players in the top 5 in the selected category
    top_5_players = sorted_df.head(5)['name'].tolist()
    
    # Get the player with the highest value in the selected category (should be in the top 5)
    correct_answer = sorted_df.iloc[0]['name']

    # Select three random players from the list of players above 5th in the category
    other_players = random.sample(sorted_df.iloc[6:]['name'].tolist(), 3)

    # Generate the multiple-choice question
    question = f"Which player in the NFL in 2022 is in the top 5 in {formatted_category}?"
    options = [correct_answer] + other_players

    return question.replace('_', ' '), options, correct_answer

def generate_and_store_question(category_df, category_names, question_type):
    if question_type == 'top5':
        selected_category = random.choice(category_names)
        formatted_category = selected_category.replace('_', ' ')
        sorted_df = category_df.sort_values(by=selected_category, ascending=False)
        top_5_players = sorted_df.head(5)['name'].tolist()
        correct_answer = sorted_df.iloc[0]['name']
        other_players = random.sample(sorted_df.iloc[6:20]['name'].tolist(), 3)
        question = f"Which player in the NFL in 2022 is in the top 5 in {formatted_category}?"
        options = [correct_answer] + other_players
    else:
        selected_category = random.choice(category_names)
        formatted_category = selected_category.replace('_', ' ')
        sorted_df = category_df.sort_values(by=selected_category, ascending=False)
        correct_answer = sorted_df.iloc[0]['name']
        top_15_players = sorted_df.iloc[1:16]['name'].tolist()
        other_players = random.sample(top_15_players, 3)
        question = f"What player in 2022 leads the NFL in {formatted_category}?"
        options = [correct_answer] + other_players

    session['questions'].append({'question': question, 'correct_answer': correct_answer})
    session['user_answers'].append({'question': question, 'selected_option': None, 'correct_answer': correct_answer})
    return question.replace('_', ' '), options

@app.route('/')
def home():
    initialize_quiz_session()
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if len(session['user_answers']) == 10:
        percent_score = (session['score']['correct'] / 10) * 100
        return render_template('quiz_result.html', percent_score=percent_score)

    # total_questions = 5  #
    # percent_score = 0  # percent score

    # if len(session['user_answers']) == total_questions:
    #percent_score = (session['score']['correct'] / total_questions) * 100

    # return render_template('quiz_result.html', percent_score=percent_score)

    if request.method == 'POST':
        # Handle submitted answer
        if 'answer' in request.form:
            selected_option = request.form['answer']

            # Check if user_answers list is empty
            if not session['user_answers']:
                # Handle the case when the user_answers list is empty (e.g., session not properly initialized)
                return render_template('error.html', error_message="Session not properly initialized")

            current_question_index = len(session['user_answers']) - 1

            # Update the selected_option for the current question
            session['user_answers'][current_question_index]['selected_option'] = selected_option

            correct_answer = session['user_answers'][current_question_index]['correct_answer']

            if selected_option == correct_answer:
                session['score']['correct'] += 1
            else:
                session['score']['wrong'] += 1



    # Choose the category based on the player position
    player_position = 'RB'  # Change this to the desired player position
    if player_position == 'QB':
        # Generate and store questions for QB
        question_type = random.choice(['top5', 'category'])
        question, options = generate_and_store_question(qb_passing_stats_qb_with_name, categories, question_type)
    elif player_position == 'RB':
        # Generate and store questions for RB
        question, options = generate_and_store_rb_question()
    elif player_position == 'WR':
        # Generate and store questions for WR
        question, options = generate_and_store_wr_question()
    elif player_position == 'TE':
        # Generate and store questions for TE
        question, options = generate_and_store_te_question()
    elif player_position == 'PK':
        # Generate and store questions for PK
        question, options = generate_and_store_pk_question()

    return render_template('quiz.html', question=question, options=options, score=session['score'])


if __name__ == '__main__':
    app.run(debug=True)