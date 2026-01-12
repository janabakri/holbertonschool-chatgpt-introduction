def play(self):
    while True:
        self.print_board()
        try:
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))

            # Check if coordinates are within the board
            if not (0 <= x < self.width and 0 <= y < self.height):
                print("Coordinates out of bounds. Try again.")
                continue

            # Reveal the chosen cell
            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

            # Check if player has won
            if self.check_win():
                self.print_board(reveal=True)
                print("Congratulations! You've won the game.")
                break

        except ValueError:
            print("Invalid input. Please enter numbers only.")
