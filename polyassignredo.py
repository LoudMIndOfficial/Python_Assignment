class mammal:
    def __init__(self,first_name,last_name="Mammal",
                 skeleton="bone", fur=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.fur = fur

    def walk(self):
        print("The mammal is walking.")

    def running(self):
        print("The mammal is running now.")

class Bear(mammal):
    def __init__(self,first_name,last_name="Bear",
                 skeleton="Bone", fur=True,stomach_state=True,teeth="Sharp"):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.fur = fur
        self.stomach_state = stomach_state
        self.teeth = teeth

class dolphin(mammal):
    def __init__(self,first_name,last_name="Dolphin",
                 skeleton="Bone", fur=False,skin="Rubbery and Smooth",breath_air=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.fur = fur
        self.skin= skin
        self.breath_air = breath_air
        

    def walk(self):
        print("Dolphins can not walk they swim everywhere.")

    def running(self):
        print("Dolphins can not run either!")
    
barry = Bear("Barry the")
print(barry.first_name + " " + barry.last_name)
print(barry.skeleton)
print(barry.fur)
barry.walk()
barry.running()
print(barry.stomach_state)
print(barry.teeth)

donny = dolphin("Donny the")
print(donny.first_name + " " + donny.last_name)
donny.walk()
donny.running()
print(donny.skeleton)
print(donny.fur)
print(donny.skin)
print(donny.breath_air)





