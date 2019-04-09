class Monster(object):
    def __init__(self, sword, obj, hat):
        self.sword = sword
        self.obj_1 = obj
        self.functioning = True
        self.life = 2
        self.hat = hat

    def lives(self, revive):
        if self.functioning:
            if self.life == 0:
                print("You are dead.")
                self.life += revive

    def kill(self):
        self.functioning = False
        print("You...")
        print()
        print()
        print("Have died.")