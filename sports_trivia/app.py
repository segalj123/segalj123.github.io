from flask import Flask, render_template, request
import os
import random

app = Flask('SportsTrivia', template_folder=os.path.abspath('templates'))

# Define the correct answers for each category
correct_answers = {
    'rushing_yards': 'Player1, Player2, Player3, Player4, Player5',
    'interceptions': 'PlayerA, PlayerB, PlayerC, PlayerD, PlayerE',
    # Add correct answers for other categories
}

# Variable to keep track of the user's score
user_score = 0

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global user_score

    if request.method == 'POST':
        # Process form submissions
        user_category = request.form.get('question_category')
        user_answer = request.form.get('user_answer')

        if user_category == 'random':
            # Choose a random category
            user_category = random.choice(list(correct_answers.keys()))

        # Check user answer and update score
        if user_answer and user_answer.lower() == correct_answers.get(user_category, '').lower():
            user_score += 1

        # After processing the question, you can redirect to a results page or display a message

    return render_template('quiz.html')
def home():
    return render_template('index.html')

# @app.route('/quiz')
# def quiz():
#     print("Trying to render quiz.html")
#     return render_template('quiz.html')

if __name__ == '__main__':
    app.run(debug=True)