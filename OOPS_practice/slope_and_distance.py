'''
Calculate Slope and Distance of a line

Create Line class method to accept coordinates as a pair of tuples and return the slope and distance of the line.

'''

class Line:
    
    def __init__(self,coor1,coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2
    
    def distance(self):
        return (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2)) ** (1/2)
    
    def slope(self):
        return ((self.y2 - self.y1) / (self.x2 - self.x1))
