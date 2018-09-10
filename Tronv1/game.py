import numpy as np

columns = 10
rows = 8

stepReward = 1
deadReward = -10
killReward = 50


#gameBoard = [[0 for x in range(columns)] for y in range(rows)]
gameBoard = np.zeros((columns, rows))



class Player:
    def __init__(self, idn, x, y, d):
        """
        init method for class
        """
        self.idn = idn
        self.x = x  # player x coord
        self.y = y  # player y coord
        self.speed = 1  # player speed
        self.body = idn + 1
        self.direction = d  # player direction
        self.prevDirection = d
        self.dead = False
        self.reward = 0
        gameBoard[x][y] = idn


    def move(self):
        """
        method for moving the player
        """

        gameBoard[self.x][self.y] = self.body
        self.x += self.direction[0]
        self.y += self.direction[1]


class Game:
    def __init__(self):

        self.player1 = Player(1, 5, 5, 2)
        self.player2 = Player(3, 2, 5, 13)
        self.reset()
    #UP-DOWN-LEFT-RIGHT

    def step(self, action):
        if action == 0:#RAK KOD:)
            if self.player1.prevDirection == (1, 0):
                self.player1.direction = (1, 0)#w dol
            else:
                self.player1.direction = (-1, 0)#do gory
                self.player1.prevDirection = self.player1.direction
        elif action == 1:
            if self.player1.prevDirection == (-1, 0):
                self.player1.direction = (-1, 0)
            else:
                self.player1.direction = (1, 0)
                self.player1.prevDirection = self.player1.direction
        elif action == 2:
            if self.player1.prevDirection == (0, 1):
                self.player1.direction = (0, 1)
            else:
                self.player1.direction = (0, -1)
                self.player1.prevDirection = self.player1.direction
        elif action == 3:
            if self.player1.prevDirection == (0, -1):
                self.player1.direction = (0, -1)
            else:
                self.player1.direction = (0, 1)
                self.player1.prevDirection = self.player1.direction
        else:
            if action == 10:#RAK KOD:)
                if self.player2.prevDirection == (1, 0):
                    self.player2.direction = (1, 0)#w dol
                else:
                    self.player2.direction = (-1, 0)#do gory
                    self.player2.prevDirection = self.player2.direction
            elif action == 11:
                if self.player2.prevDirection == (-1, 0):
                    self.player2.direction = (-1, 0)
                else:
                    self.player2.direction = (1, 0)
                    self.player2.prevDirection = self.player2.direction
            elif action == 12:
                if self.player2.prevDirection == (0, 1):
                    self.player2.direction = (0, 1)
                else:
                    self.player2.direction = (0, -1)
                    self.player2.prevDirection = self.player2.direction
            elif action == 13:
                if self.player2.prevDirection == (0, -1):
                    self.player2.direction = (0, -1)
                else:
                    self.player2.direction = (0, 1)
                    self.player2.prevDirection = self.player2.direction
        if action < 10:
            self.player1.move()
            if self.checkCollision(self.player1.x, self.player1.y) == False:
                self.player1.reward = stepReward
                gameBoard[self.player1.x][self.player1.y] = self.player1.idn
            else:
                self.player1.reward = deadReward
                self.player1.dead = True
                gameBoard[self.player1.x][self.player1.y] = self.player1.idn
            """
            print("PLAYER1STEP: _________________________")
            print(gameBoard)
            print("______________________________________")
            print("Reward: " + str(self.player1.reward) + " Dead: " + str(self.player1.dead))
            """
            return gameBoard, self.player1.reward, self.player1.dead
        elif action > 9:
            self.player2.move()
            if self.checkCollision(self.player2.x, self.player2.y) == False:
                self.player2.reward = stepReward
                gameBoard[self.player2.x][self.player2.y] = self.player2.idn
            else:
                self.player2.reward = deadReward
                self.player2.dead = True
                gameBoard[self.player2.x][self.player2.y] = self.player2.idn
            """
            print("PLAYER2STEP: _________________________")
            print(gameBoard)
            print("______________________________________")
            print("Reward: " + str(self.player2.reward) + " Dead: " + str(self.player2.dead))
            """
            return gameBoard, self.player2.reward, self.player2.dead

    def reset(self):
        #self.player1 = Player(1, 5, 5, 2)
        #self.player2 = Player(3, 2, 2, 13)
        self.player1.x = 5
        self.player1.y = 5
        self.player2.x = 2
        self.player2.y = 5
        self.player1.direction = 2
        self.player2.direction = 13
        self.player1.dead = False
        self.player2.dead = False
        self.player1.reward = 0
        self.player2.reward = 0
        for x in range(columns):
            for y in range(rows):
                gameBoard[x][y] = 0
        for x in range(columns):
            gameBoard[x][0] = -1
            gameBoard[x][rows - 1] = -1
        for y in range(rows):
            gameBoard[0][y] = -1
            gameBoard[columns - 1][y] = -1
        return gameBoard

    def render(self):
        print(gameBoard)

    def checkCollision(self, x, y):
        if gameBoard[x][y] != 0:
            return True
        else:
            return False
