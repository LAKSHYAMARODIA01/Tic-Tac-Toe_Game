import os

class TicTacToe:
    def __init__(self):
        self.board = ['-' for _ in range(9)]
        self.current_turn = 1
        self.player_symbols = {1: 'X', 2: 'O'}

    def print_board(self):
        print("Current Board:")
        for i in range(3):
            print(" " + " | ".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("---+---+---")

    def is_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '-':
                return True
        return False

    def is_draw(self):
        return '-' not in self.board

    def make_move(self, position):
        if self.board[position] == '-':
            self.board[position] = self.player_symbols[self.current_turn]
            return True
        return False

    def switch_turn(self):
        self.current_turn = 2 if self.current_turn == 1 else 1

    def save_game(self):
        with open('game_state.txt', 'w') as f:
            f.write(','.join(self.board) + '\n')
            f.write(f'Player Turn: {self.current_turn}\n')
        print("Game state saved!")

    def load_game(self):
        if os.path.exists('game_state.txt'):
            with open('game_state.txt', 'r') as f:
                lines = f.readlines()
                self.board = lines[0].strip().split(',')
                self.current_turn = int(lines[1].strip().split(': ')[1])
            print("Game state loaded!")
        else:
            print("No saved game found.")

    def play(self):
        print("Welcome to Tic Tac Toe!")
        print("Player 1: X")
        print("Player 2: O")
        
        while True:
            self.print_board()
            print(f"Player {self.current_turn}, enter your move (1-9) or 's' to save, 'l' to load: ")
            move = input().strip()

            if move.lower() == 's':
                self.save_game()
                continue
            elif move.lower() == 'l':
                self.load_game()
                continue

            try:
                position = int(move) - 1
                if position < 0 or position > 8:
                    print("Invalid move! Please enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            if self.make_move(position):
                if self.is_winner():
                    self.print_board()
                    print(f"Player {self.current_turn} wins!")
                    break
                elif self.is_draw():
                    self.print_board()
                    print("It's a draw!")
                    break
                self.switch_turn()
            else:
                print("Invalid move! That position is already taken.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play()