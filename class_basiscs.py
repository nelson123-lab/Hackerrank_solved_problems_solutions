class schools:
    school_no = 0
    def __init__(self,name, year, board, price):
        self.name = name
        self.year = year
        self.board = board
        self.price = price
        schools.school_no += 1

    def report(self):
        return "{} {} {} {}".format(self.name, self.year, self.board,self.price)

school_1 = schools("depaul",1992,"cbse", 50000)
school_2 = schools("vimala",1999,"cbse", 70000)
school_3 = schools("jai rani",1949,"cbse", 60000)

class malayalam(schools): #inheritance
    def __init__(self,name, year, board, price, place):
        super().__init__(name, year, board, price)
        """if we want to add an extra attribute "place" to the inherited class malayalam"""
        self.place = place
school_4 = malayalam("stjoseph", 1992, "state", 2000, "karimanooor")



class uniform(schools):# subclass (incomplete)
    def __init__(self, name,year, board,price,school = None):
        super().__init__(name,year,board,price)
        if schools is None:
            self.school = []
        else:
            self.school = school
