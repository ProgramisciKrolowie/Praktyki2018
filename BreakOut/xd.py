import pygame
import numpy as np

# initialize the game engine
pygame.init()

columns = 10
rows = 10

stepReward = 1
deadReward = -10
killReward = 50


class Directions(object):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


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
        self.prevDirection = None
        gameBoard[y][x] = idn


    def move(self):
        """
        method for moving the player
        """

        gameBoard[self.y][self.x] = self.body
        self.x += self.direction[0]
        self.y += self.direction[1]
        if game.checkCollision(self.x, self.y) == False:
            gameBoard[self.y][self.x] = self.idn
            return True
        else:
            return False


class Game:
    def step(self, action1):
        if action1 == Directions.UP:
            player1.direction = (0, -1)
        elif action1 == Directions.DOWN:
            player1.direction = (0, 1)
        elif action1 == Directions.LEFT:
            player1.direction = (-1, 0)
        elif action1 == Directions.RIGHT:
            player1.direction = (1, 0)
        if player1.move():
            reward = stepReward
            p1dead = False
        else:
            reward = deadReward
            p1dead = True
            self.draw()

        return gameBoard, reward, p1dead


    def reset(self):
        for x in range(columns):
            gameBoard[0][x] = -1
            gameBoard[columns-1][x] = -1
        for y in range(rows):
            gameBoard[y][0] = -1
            gameBoard[y][rows-1] = -1

    def draw(self):
        print(gameBoard)

    def checkCollision(self, x, y):
        if gameBoard[y][x] != 0:
            return True
        else:
            return False


player1 = Player(1, 5, 5, Directions.LEFT)
p1action = -1
game = Game()
game.reset()
done = False


action1=Directions.DOWN
img, reward, dead = game.step(action1)
img, reward, dead = game.step(action1)
img, reward, dead = game.step(action1)
action1=Directions.LEFT
img, reward, dead = game.step(action1)
action1=Directions.DOWN
img, reward, dead = game.step(action1)

#print(np.matrix(gameBoard))



pygame.quit()