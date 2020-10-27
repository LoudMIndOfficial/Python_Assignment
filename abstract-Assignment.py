# Python program showing 
# abstract base class work 
  
from abc import ABC, abstractmethod 
  
class color(ABC): 
  
    # abstract method 
    def iamcolor(self): 
        pass
  
class red(color): 
  
    # overriding abstract method 
    def iamcolor(self): 
        print("I am the color red") 
  
class blue(color): 
  
    # overriding abstract method 
    def iamcolor(self): 
        print("I am the color blue") 
  
class green(color): 
  
    # overriding abstract method 
    def iamcolor(self): 
        print("I am the color green") 
  
class orange(color): 
  
    # overriding abstract method 
    def iamcolor(self): 
        print("I am the color orange") 
  
# Driver code 
R = red() 
R.iamcolor() 
  
B = blue() 
B.iamcolor() 
  
R = green() 
R.iamcolor() 
  
K = orange() 
K.iamcolor() 
