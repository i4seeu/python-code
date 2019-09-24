class Person:
    def __init__(self, firstname, lastname, age, weight):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.weight = weight

    def setFirstname(self, firstname):
        self.firstname = firstname
    def getFirstname(self):
        return self.firstname
    def setLastname(self, lastname):
        self.lastname = lastname
    def getLastname(self):
        return self.lastname
    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age
    def setWeight(self, weight):
        self.weight = weight
    def getWeight(self):
        return self.weight
    def isObes(self):
        if self.weight >= 80:
            return True
        else:
            return False

class Student(Person):
    def __init__(self, firstname, lastname, age, weight):
        Person.__init__(self, firstname, lastname, age, weight)

class Staff(Person):
    def __init__(self, firstname, lastname, age, weight):
        Person.__init__(self, firstname, lastname, age, weight)
    
stud1 = Student("Van","Nar",20, "40kg")
print(stud1.isObes())



