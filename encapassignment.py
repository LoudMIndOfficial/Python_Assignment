class Base(object):
    def __private(self):
        print("private value ") #private value DOUBLE underscore
    def _protected(self):
        print("protected value ") #protected value SINGLE underscore 
    def public(self):
        print("public view")
        self.__private()  # private value
        self._protected() #protected value
class Derived(Base):
    def __private(self):
        print("This is  private")
    def _protected(self):
        print("This is protected")
d = Derived()
d.public()

