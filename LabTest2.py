from math import sqrt
from math import pow

#Lab Test 2

#Write a python class to represent a 3D vector

#Name: Jade Brennan-Keane
#Student Number: C18512336


#Vector class
class Vector3D:
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    #Vector Addition
    def __add__ (self, v2):
        return(self.x + v2.x, self.y + v2.y, self.z + v2.z)
    
    #Vector Subtraction
    def __sub__ (self, v2):
        return(self.x - v2.x, self.y - v2.y, self.z - v2.z)
    
    #Vector Multiplication
    def __mul__ (self, n):
        try:
            #by an int:
            return(self.x * n,  self.y * n,  self.z * n)
        except:
            #by another Vector
            return(self.x * v2.x + self.y * v2.y + self.z * v2.z)
        
    #Vector Magnitude
    def magnitude (self):
        return(sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2)))
    
    #format for printing the vectors
    def __str__ (self):
        return ("({},{},{})".format(self.x, self.y, self.z))
        
#MAIN
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(5, 5, 5)

#Display v1
print ("Printing v1")
print ("v1 =", v1)
#Display v2
print ("Printing v2")
print ("v2 = ", v2)
#Print the Addition of the two vectors
v3 = v1 + v2
print ("Printing addition")
print("v1 + v2 = ", v3)
#printing the Subtraction of the two vectors
v4 = v1 - v2
print ("Printing subtraction")
print("v1 - v2 = ", v4)
#printing the two vectors multiplied together
print ("Printing dot product")
v5 = v1 * v2
print("v1 * v2 = ", v5)
#printing v1 multiplied by 2.5
print ("Printing integer multiplication")
v6 = v1 * 2
print("v1 * 2.5 = ", v6)
#printing the Magnitude of v1
print("v1 magnitude is ", v1.magnitude())