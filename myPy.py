import sys

class Game: ### Game Class ###
    boards = {} 
    gameState = None
    xUsedUndo = False
    yUsedUndo = False
    def __init__(self):
        tempBoard = [1,2,3,4,5,6,7,8,9]
        self.gameState = 0
        self.boards[0] = tempBoard
    def getBoard(self, state):
        return self.boards[state]

    def getBlock(self, state, i):
        return self.boards[state]

    def newBoard(self, plr, local): # Copy previous board, add to list, and incriment time
        oldBoard = self.boards[self.gameState].copy()
        self.gameState = self.gameState + 1
        self.boards[self.gameState] = oldBoard
        self.setBlock(plr, local)

    def isEmpty(self, index): #Check if a square has been picked yet
        index = index - 1
        if isinstance(self.boards[self.gameState][index], int):
            return True
        else:
            return False
    def setBlock(self, plr, index):
        if plr == 0:
            plr = "x"
        else:
            plr = "o"
        self.boards[self.gameState][index-1] = plr

    def print(self):
        for i in range(3): #loop through rows
            for j in range(3): #loop through columns
                print(self.boards[self.gameState][i*3+j], end="")
                if j <= 1:
                    print(end=" | ")
            print()
    def isDone(self):
        if self.gameState >= 8:
            return True
        winning_combinations = [
                [0, 1, 2], # row 1
                [3, 4, 5], # row 2
                [6, 7, 8], # row 3
                [0, 3, 6], # column 1
                [1, 4, 7], # colum 2
                [2, 5, 8], #column 3
                [0, 4, 8], # diagonal 1
                [2, 4, 6] # diagonal 2
            ]
        # check each winning combination
        for combination in winning_combinations:
            a, b, c = combination
            if self.boards[self.gameState][a] == self.boards[self.gameState][b] == self.boards[self.gameState][c] and isinstance(self.boards[self.gameState][a], str):
                print(f"{self.boards[self.gameState][a]} wins!") # print output                                                            
                return True
        return False
    def undo(self, plrId):
        self.boards.pop(self.gameState)
        self.gameState -= 1
        self.boards.pop(self.gameState)
        self.gameState -= 1
        self.plrMove(plrId)
    def plrMove(self, plrId):
        plr_input = None
        if plrId == 0:
            plrName = 'x'
        else: plrName = 'o'
        self.print() # print the game for the player to see
        while True:
            try:
                plr_input = input(f"Enter your move 1-9, or undo with 'u' player {plrName}:")
                if plr_input == 'u': # undo with player input
                    if self.gameState < 3: 
                        self.print()
                        print("It's too soon in the game for that!") 
                    else:
                        if plrId == 0:
                            if game.xUsedUndo == True: print("You've already used your undo!")
                            else:
                                self.undo(plrId)
                                self.xUsedUndo = True
                                break;
                        if plrId == 1:
                            if game.yUsedUndo == True: print("You've already used your undo!")
                            else:
                                self.undo(plrId)
                                self.yUsedUndo = True
                                break;
                # End undo code #
                elif 1 <= int(plr_input) <= 9 and self.isEmpty(int(plr_input)):
                    plr_input = int(plr_input)
                    break # pass thorugh the while loop to setting a new board  
                else: 
                    self.print()
                    print("Please enter an integer 1-9 for a space which hasn't been picked")
            except ValueError:
                self.print()
                print("Please enter an integer 1-9 for a space which hasn't been picked. error")
        self.newBoard(plrId, plr_input)
        if plrId == 0:
            game.setBlock(0, plr_input)
        else:
            game.setBlock(1, plr_input)
        if self.isDone():
            self.print()
            sys.exit()




# Start of running code

game = Game()
for i in range(11):
    player = i % 2 # Alternates between 0 and 1
    game.plrMove(player)
    if game.isDone():
        break;
print("Game Over!")
