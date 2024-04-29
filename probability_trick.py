import random

class Hat:
    # a class of a magicians hat with a specifaid number of different coler balls
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color]*count)

    def draw(self, amount, expirament=False):
        # draws an amount of balls randomly from the hat and returns the balls
        if expirament:
            # chacks if its a probability test so it wont remove the withdraw balls from the hat
            drow_balls = random.sample(self.contents, amount)
        else:
            
            if amount >= len(self.contents):
                # if amount of balls to withdraw from hat bigger then 
                # the amont of balls in the hat returns all the balls that are left
                drow_balls =  self.contents
                self.contents = []
            
            else:
                # baisic case
                drow_balls = random.sample(self.contents, amount)
                for ball in drow_balls:
                    self.contents.remove(ball)
        return drow_balls
    

        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # probability experiment draws an specifaid amount of balls from
    # the hat number of times to find the probability of drawn balls include
    # specific balls(color an amount)
    ans = {}
    num = 0
    precentge = 0
    # inits a hat class innstins with the balls from the hat dic
    hat = Hat(**hat)
    while num <= num_experiments:
        balls = hat.draw(num_balls_drawn,  expirament=True)
        n_precentge = 0
        for ball in balls:
            if ball in expected_balls:
                ans[ball] = balls.count(ball)

        for col_e, num_e in expected_balls.items():
            if col_e in ans:
                if ans[col_e] == num_e:
                    n_precentge += 1
                else:
                    n_precentge = 0
        if n_precentge == len(expected_balls):
            if precentge == 0:
                precentge = 100 
            precentge = (precentge + 100) / 2
        else:
            precentge = (precentge + 0) / 2
        precentge = round(precentge) 
            
        num += 1
    return precentge

def main():                   
    ha = {"blue": 5, "red": 4, "green": 2}
    expected_balls = {"red": 1, "green": 2}
    num_balls_drawn = 4
    num_experiments = 10000

    probability = experiment(ha, expected_balls, num_balls_drawn, num_experiments)
    print(f"Estimated Probability: {probability}")
if __name__ =='__main__':
    main()


    