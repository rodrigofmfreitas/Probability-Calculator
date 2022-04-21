import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for k, v in kwargs.items():
            for item in range(v):
                self.contents.append(k)
        print(self.contents)
    
    def draw(self, num):
        drawn_balls = list()
        for i in range(num):
            try:
                ball = self.contents.pop(random.randrange(len(self.contents)))
                drawn_balls.append(ball)
            except:
                return drawn_balls
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    eballs = list()

    for k, v in expected_balls.items():
        for i in range(v):
            eballs.append(k)
    for i in range(num_experiments):
        checker = 0
        newhat = copy.deepcopy(hat)
        drawn = newhat.draw(num_balls_drawn)
        copyballs = copy.deepcopy(eballs)
        for color in eballs:
            if color in drawn and color in copyballs:
                copyballs.remove(color)
                drawn.remove(color)
                checker += 1
        if checker == len(eballs):
            count +=1
    return count/num_experiments