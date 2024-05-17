class Plane():

    def __init__(self, speed, hp, damage, xPos, yPos, heading, player):
        self._speed = speed
        self._hp = hp
        self._damage = damage
        self._xPos = xPos
        self._yPos = yPos
        self._player = player # key that player has to press to shoot
        self._heading = heading     #describes the direction of the Plane in the field  | 1 upwards;  2 diagonal right upwards; 3 right; 4 ...

    def shoot(self):
        print("shoot")
        

    def move(self):
        #funciton to fly upwards, the yPos changes with every tick by speed 
        def up(self):
            yPos = self._yPos - self._speed
        
        switcher = {
            "1": up()
            
        }

        pass

    def recieveDamage(self, damage):
        pass

    def getDestroyed(self):

        if self._hp <= 0:
            pass
        else: 
            pass

    