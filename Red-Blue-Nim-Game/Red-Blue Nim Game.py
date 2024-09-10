class RedBlueNimGame:
    def __init__(self, num_red, num_blue, version, first_player):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.current_player = first_player

    def display_state(self):
        """Display the current number of red and blue marbles."""
        print(f"\nRed marbles: {self.num_red}, Blue marbles: {self.num_blue}")
        print(f"Current player: {self.current_player}")

    def is_game_over(self):
        """Check if the game is over."""
        return self.num_red == 0 or self.num_blue == 0

    def make_move(self, red_taken, blue_taken):
        """Update the number of marbles left after a move."""
        self.num_red -= red_taken
        self.num_blue -= blue_taken

    def human_move(self):
        """Prompt the human player to make a move."""
        self.display_state()
        while True:
            try:
                red_taken = int(input("Pick red marbles (1 or 2): "))
                blue_taken = int(input("Pick blue marbles (1 or 2): "))
                if (1 <= red_taken <= 2) and (1 <= blue_taken <= 2):
                    self.make_move(red_taken, blue_taken)
                    break
                else:
                    print("Invalid move. You can only take 1 or 2 marbles of each color.")
            except ValueError:
                print("Please enter valid numbers.")

    def computer_move(self):
        """Make a simple move for the computer."""
        self.display_state()
        # Computer's simple strategy: Take 1 red and 1 blue if possible, otherwise take the available number
        if self.num_red > 0 and self.num_blue > 0:
            red_taken, blue_taken = 1, 1
        elif self.num_red > 0:
            red_taken, blue_taken = 1, 0
        elif self.num_blue > 0:
            red_taken, blue_taken = 0, 1
        print(f"Computer takes {red_taken} red marbles and {blue_taken} blue marbles.")
        self.make_move(red_taken, blue_taken)

    def check_winner(self):
        """Check who wins based on the game version."""
        if self.version == 'standard':
            return "Computer" if self.current_player == 'human' else "Human"
        else:  # Misère version
            return "Human" if self.current_player == 'human' else "Computer"

def play_game(num_red, num_blue, version, first_player):
    """Main function to play the Red-Blue Nim Game."""
    game = RedBlueNimGame(num_red, num_blue, version, first_player)
    
    # Main game loop
    while not game.is_game_over():
        if game.current_player == 'human':
            game.human_move()
            game.current_player = 'computer'
        else:
            game.computer_move()
            game.current_player = 'human'

    # End game and declare winner
    winner = game.check_winner()
    print(f"\nGame over! {winner} wins!")
    print(f"Final State: Red marbles: {game.num_red}, Blue marbles: {game.num_blue}")

if __name__ == "__main__":
    # Setup game from user input
    num_red = int(input("Enter the number of red marbles: "))
    num_blue = int(input("Enter the number of blue marbles: "))
    version = input("Enter the game version (standard/misere): ").strip().lower()
    first_player = input("Who plays first (human/computer): ").strip().lower()

    # Start the game
    play_game(num_red, num_blue, version, first_player)
