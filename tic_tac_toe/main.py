class Play:
    def __init__(self, board):
        print("Welcome to Tic-Tac-Toe")
        # Board()
        self.type = choice(["X", "O"])
        self.board = {0:0, 0:1, 0:2, 0:3, 0:4, 0:5, 0:6, 0:7, 0:8}

    def round(self):
        self.won = False
        while self.won == False:
            Play.make_move()
            Play.check_if_won()
            Computer.make_move()
            Computer.check_if_won()

    def make_move(self, move):
        #move = [<square>]
        pass
