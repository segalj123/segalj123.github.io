# Team Members:
-**Jonathan Segal**

## Project Overview
My web application is a NFL Trivia Quiz that is focused on testing the users' knowledge of random 2022 NFL trivia. The Trivia is based on positions and who led in a stat that year. I tried to make the quiz as user friendly as possible while still being engaging with a few interactive features. 

## Usage Guidelines
To interact with the application, users can follow these steps:
1. Click on the "**To The Quiz**" button on the homepage to start the quiz.
2. Answer the trivia questions presented, and click "**Next Question**" to proceed.
3. Receive immediate feedback on correct and incorrect answers.
4. Upon completion, view the quiz result, showing the percentage score and details.

## Dependencies
The project depends on the folllowing: 
- **Bootstrap** (v4.0.0)
- **jQuery** (v3.2.1)
- **Popper.js** (v1.12.9)
- **Canvas Confetti library** (v1.0.3)
- **nfl.import_team_desc()**
- **nfl.import_seasonal_data([2022])**
- **nfl.import_schedules([2022])**
- **nfl.import_ids()**

## Project Structure
The project is structured with key files and directories:
- `quiz.html`: Main HTML file for the quiz interface.
- `quiz_result.html`: HTML file displaying quiz results.
- `index.html`: Homepage HTML file.
- `error.html`: Redirected to page if error with session 
- `app.py` : Directing the other pages while also generating questions and storing stats

## Acknowledgments
We acknowledge the following resources:
- **Bootstrap**, **jQuery**, and **Popper.js** for enhancing the UI.
- **Canvas Confetti library** for adding a dynamic element to quiz results.
- **Professor Li's Github source** for providing the data using **nfl.import_team_desc()**, **nfl.import_seasonal_data([2022])**, **nfl.import_schedules([2022])**, **nfl.import_ids()**.
- **Professor Zhi Li** for helping me with errors and issues I was having,
- **Rapid API** for the beginning of my project even though I didn't end with them.
- **ChatGpt** helped me solve through some styling errors and clean up errors I was confused on. Help me come up with new ideas. 
- **Colorhunt.co** allowed me to find new colors that work well with each other. 
- **Bootstrap** as a website as well as code. 
- **My father** for thinking about why my JSON file might not be working as well.
- **Reddit** had some good responses on errors I was having.
- **Others I could have missed** I would like to thank any source that helped with throughout my project I may have missed. 

## Reflection

### Process Point of View
- **What Went Well:** I'm thrilled with the final version of the project. The web application is fully functional, and I find it personally satisfying. Looking at the site, I could easily believe it was created by someone else — a testament to the completeness and professionalism of the project.

- **Challenges Faced:** The development process wasn't without its hurdles. I encountered numerous challenges, ranging from dealing with the API and JSON file to implementing new sessions. Each addition or modification seemed to introduce a new set of errors. Challenges included generating questions dynamically, managing the scoring system, and grappling with Flask intricacies. However, it's important to note that overcoming these challenges significantly improved the overall quality of my site. Each problem served as an opportunity for learning and enhancement.

- **Improved On:**
    **Project Enjoyment:** The project significantly improved my overall coding experience. It was not only educational but also enjoyable, making me feel more confident in my coding abilities.
    **Availability and Support:** The accessibility to assistance was a positive aspect. However, to further enhance the iterative process, introducing a rough draft day could be beneficial. This would allow for earlier feedback, fostering continuous improvement.
    **Feedback Iteration:** Consider implementing a rough draft day to facilitate early feedback. This could potentially lead to more refined and polished project elements.

### Learning Perspective

**Learnings:**
  - The project served as a profound learning experience, consolidating ideas from the year and providing a holistic view of the coding landscape.
  - Witnessing the Whole Picture: This project enabled me to see the whole picture, bringing together concepts learned over time.
  - Code Structure and Sequels: Reflecting on the project, I realize the potential benefits of incorporating more sequels into the code for a more streamlined development process.
  
  **Website vs. Terminal:**
  - A website-based project delivered a superior final product compared to assignments confined to the terminal. This shift provided a better coding experience and a welcome break from traditional studies.
  - Endless Exploration: The project felt like a never-ending problem, allowing continuous additions to the code and fostering a sense of exploration and creativity.
  
  **Future Coding Endeavors:**
  - I plan to continue coding and explore the possibility of learning new programming languages.
  - Shifting Perspective: While initially hesitant about coding, this class and project have sparked a newfound interest, and I can envision experimenting with coding as a side pursuit.
  - Inspiring Growth: Observing the improvement in my friend's projects over time has been enjoyable and inspiring, adding to the overall positive experience.
  
**ChatGPT's Assistance:**
  - ChatGPT played a crucial role in translating my ideas into code. When faced with uncertainties about where to start or specific commands, ChatGPT provided clear and concise guidance.
  - Simplifying Complexity: Navigating resources like Reddit or the web can be confusing, but ChatGPT simplified the understanding of coding concepts and helped resolve errors.
  - Indentation Assistance: Dealing with numerous indentation errors, ChatGPT offered a convenient solution to align the code correctly, saving time and effort.