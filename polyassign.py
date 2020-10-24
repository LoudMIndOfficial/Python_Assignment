class Mustang(): 
    def fuel(self): 
        print("Some Mustangs use gasoline for fuel") 
   
    def transmission(self): 
        print("Some Mustangs have a 6 speed transmisson") 
   
    def manufacturer(self): 
        print("Mustand's manufacturer is Ford.") 
   
class Civic(): 
    def fuel(self): 
        print("Some civics are electric.") 
   
    def transmission(self): 
        print("Most have automatic transmissions ") 
   
    def manufacturer(self): 
        print("Civic's manufacturer is Honda") 
  
def func(obj): 
    obj.fuel() 
    obj.transmission() 
    obj.manufacturer() 
   
obj_mustang = Mustang() 
obj_civic = Civic() 
   
func(obj_mustang) 
func(obj_civic) 
