class Plane():

    def __init__(self, speed, hp, damage):
        self._speed = speed
        self._hp = hp
        self._damage = damage

    def shoot(self):
        pass

    def move(self):
        pass

    def recieveDamage(self, damage):
        pass

    def getDestroyed(self):

        if self._hp <= 0:
            pass
        else: 
            pass

    