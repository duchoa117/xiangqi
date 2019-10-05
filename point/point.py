class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y


    def checkOnBoard(self):
        a = -1 < self.x < 9
        b = -1 < self.y < 10
        return(a and b)

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    def __eq__(self, other):
        return(self.x == other.x and self.y == other.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)
    def __mul__(self, other):
        x = self.x*other
        y = self.y*other
        return Point(x,y)
    def __lt__(self, other):
        return((self.x < other.x) and (self.y < other.y))
    def __le__(self, other):
        return((self.x <= other.x) and (self.y <= other.y))
    def __ne__(self, other):
        return((self.x != other.x) and (self.y != other.y))
    def __gt__(self, other):
        return((self.x > other.x) and(self.y > other.y))
    def __ge__(self, other):
        return((self.x >= other.x) and(self.y >= other.y))


    
    


    