class animal:
    def __init__(self, health, sleep):
        self.health = health
        self.sleep = sleep

    def double_sleep(self):
        self.sleep = self.sleep * 2

class dog(animal):
    def __init__(self, health, sleep):
        super().__init__(health, sleep)
    
        
a1 = dog(100,10)
a1.double_sleep()
a1.double_sleep()

print(a1.sleep)