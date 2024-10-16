from math import sin,cos,radians
import random

""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize, ballSize):
        self.players = [Player(self, False, -90, "blue"), Player(self, True, 90, "red")]
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        self.index = 0
        self.windSpeed = (random.random() * 20) - 10
        pass 

    """ A list containing both players """
    def getPlayers(self):
        return self.players
    
    """ The height/width of the cannon """
    def getCannonSize(self):
        return self.cannonSize
    
    """ The radius of cannon balls """
    def getBallSize(self):
        return self.ballSize    
    
    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.getPlayers()[self.getCurrentPlayerNumber()]

    """ The opponent of the current player """
    def getOtherPlayer(self):
        if self.getCurrentPlayerNumber() == 0:
            return self.players[1]
        else:
            return self.players[0]
    
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.index 
    
    """ Switch active player """
    def nextPlayer(self):
        if self.index == 0:
            self.index = 1
        else:
            self.index = 0


    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
        self.windSpeed = wind

    
    def getCurrentWind(self):
        return self.windSpeed

    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        self.windSpeed = (random.random() * 20) - 10

""" Models a player """
class Player:
    def __init__(self, game, isReverted, position, color):
        self.game = game
        self.isReverted = isReverted
        self.position = position
        self.color = color
        self.angleVelocity = (45,40)
        self.score = 0
    
    def fire(self, angle, velocity):
        if self.isReverted == True:
            self.angleVelocity = ((180 - angle),velocity)
            return Projectile((180 - angle), velocity, self.game.getCurrentWind(), self.getX(), (self.game.getCannonSize()/2), -110, 110)
        else:
            self.angleVelocity = (angle,velocity)
            return Projectile(angle, velocity, self.game.getCurrentWind(), self.getX(), (self.game.getCannonSize()/2), -110, 110)
        

    def projectileDistance(self, proj):
        projectilePosX = proj.getX()
        playerTargetX = self.getX()
        cannonRadius = self.game.getCannonSize() / 2
        ballRadius = self.game.getBallSize()
        centerDistance = abs(playerTargetX - projectilePosX)

        edgeDistance = centerDistance - (cannonRadius + ballRadius) 
        
        if edgeDistance <= 0: 
            return 0

        elif projectilePosX < playerTargetX:
            return -edgeDistance

        else:
            return edgeDistance

    def getScore(self):
        return self.score

    def increaseScore(self):
        self.score += 1

    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self.color

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self.position

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        return self.angleVelocity



""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
            angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind


    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
         for large values the projectile may move erratically)
    """
    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        
        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        
        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)
        
        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1
        
    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """
    def getY(self):
        return self.yPos
