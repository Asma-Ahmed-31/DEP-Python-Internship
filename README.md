# DEP-Python-Internship
Red-Blue Nim Game 🔴🔵
Welcome to the Red-Blue Nim Game! This Python-based project lets you play the classic Nim game with a twist—featuring both Standard and Misère versions. With an AI opponent powered by the Minimax Algorithm and Alpha-Beta Pruning, the game offers a fun and strategic experience for players of all skill levels.

🚀 Features
Standard and Misère Versions: Play two different versions of Nim with unique win conditions.
AI Opponent: Challenge yourself against an AI using the Minimax algorithm with Alpha-Beta pruning.
Interactive Gameplay: Play against either a human or the computer, making strategic decisions on every turn.
🛠️ Prerequisites
Ensure the following are installed:

Python 3.x
📥 Installation
Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/red-blue-nim-game.git
cd red-blue-nim-game
Run the Game
bash
Copy code
python3 red_blue_nim_game.py
💻 Usage
1. Command Line Parameters
You can configure the game using command-line input. When prompted, enter the following:

Number of Red Marbles: Specify how many red marbles the game starts with.
Number of Blue Marbles: Specify how many blue marbles the game starts with.
Version: Choose between the 'standard' or 'misere' version of the game.
First Player: Select who starts first, either the 'human' or the 'computer'.
2. Example
bash
Copy code
Enter the number of red marbles: 5
Enter the number of blue marbles: 3
Enter the game version (standard/misere): standard
Who plays first (human/computer): human
The game alternates turns between the human and computer players, prompting moves and displaying the game state after each round.

📚 Game Rules
1. Standard Version
Objective: Players lose if either pile (red or blue marbles) is empty on their turn.
2. Misère Version
Objective: Players win if either pile (red or blue marbles) is empty on their turn.
3. Scoring System
Red Marbles Left: Each remaining red marble is worth 2 points.
Blue Marbles Left: Each remaining blue marble is worth 3 points.
🤖 AI Logic
1. Minimax Algorithm
The computer opponent is powered by the Minimax algorithm, which ensures optimal decision-making during the game.

2. Alpha-Beta Pruning
To improve efficiency, Alpha-Beta Pruning is implemented to reduce the number of nodes evaluated in the decision tree.

3. Move Ordering (Standard)
In the standard version, the AI prioritizes the following moves:

Pick 2 red marbles.
Pick 2 blue marbles.
Pick 1 red marble.
Pick 1 blue marble.
4. Move Ordering (Misère)
In the misère version, the AI inverts the move order:

Pick 1 blue marble.
Pick 1 red marble.
Pick 2 blue marbles.
Pick 2 red marbles.
🎨 Future Enhancements
Difficulty Levels: Add options for different AI difficulty levels.
GUI: Develop a graphical interface to enhance the gaming experience.
Multiplayer: Enable online multiplayer functionality to allow friends to play together.
🤝 Contributing
We welcome contributions! Feel free to open issues or submit pull requests for any improvements or bug fixes. For any questions, reach out via GitHub issues.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📧 Contact
For further inquiries or feedback, please contact [asmaahmedzia111@gmail.com] or open an issue on the GitHub repository.
