from random import randint

class MontyHall:
    """
    The Monty Hall Problem
    """
    def __init__(self,doors=3,change=False):
        """
        Initialize game

        @param doors : an int used to generate the doors list from one up to the input number (must be at least 2).
	@param change : a boolean to determine whether to stay with the original door pick
        """
        self.doors = [x for x in xrange(1,doors + 1)]
        self.change = change

    def play(self):
        """
        Play game

        @return : a boolean representing whether the correct door was choosen
        """

        #copy the doors list
        doors = self.doors + []
        
        #randomly assign the prize to one of the doors
        prize = doors[randint(0,len(doors) - 1)]

        #randomly assign a guess for which door the prize is behind
        choice = doors.pop(randint(0,len(doors) - 1))

        #open all unchosen doors except for one and call it the "alternative"
        #let the player select between the chosen door and the alternative
        #if the prize was not selected, make the alternative door the prize
        #otherwise, pick a door at random for the alternative
        if prize in doors:
            alternative = prize
        else:
            alternative = doors.pop(randint(0,len(doors) - 1))
    
        #if change is True, pick the alternative door
        #otherwise stay with the choosen door
        if self.change:
            choice = alternative
    
        #return True if the correct door was selected
        return prize == choice

    def test(self,iterations=1000):
        """
        Test strategy

        @param iterations : 
        @return : a float representing the success rate for the chosen strategy
        """
        score = 0
        i = 0
        while i < iterations:
            if self.play():
                score += 1
            i+=1
        return float(score) / iterations


m = MontyHall()
print m.test()

#change the default strategy from False to True
m = MontyHall(change=True)
print m.test()

m = MontyHall(5)
print m.test()

#change the default strategy from False to True
m = MontyHall(5,change=True)
print m.test()
