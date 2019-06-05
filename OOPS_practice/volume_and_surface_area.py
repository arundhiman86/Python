'''
Calculate Volume and Surface area of a Cylinder

Create Cylinder class method to accept values as a pair of tuples and return the Volume and Sphere of the Cylinder.

'''

class Cylinder:
    
    pi = 3.14
    
    def __init__(self,height=1,radius=1):
        self.h = height
        self.r = radius
        
    def volume(self):
        return self.pi *(self.r**2)* self.h
    
    def surface_area(self):
        return (2*self.pi*self.r*self.h) + (2*self.pi*(self.r**2))
