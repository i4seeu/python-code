class Student:
  def __init__(self , name, id,age):
    self.name = name
    self.id = id
    self.age = age
  def assessPassMark(self, marks):
     print(self.name, " mark is ", marks)
  def changeName(self, newname):
    self.name = newname
  def setAge(self, age):
    self.age = age
  def getAge(self):
    return self.age
student1 = Student("Noordeen Malango","RG123",35)
student1.assessPassMark(40)
student1.changeName("Vanessa Narciso")
student1.assessPassMark(40)
student1.setAge(60)
student_age = student1.getAge()
print(student_age)