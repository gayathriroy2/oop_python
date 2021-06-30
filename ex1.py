class Rectangle(object):
  def __init__(self,length,width):
    self.length=length
    self.width=width
  def Perimeter(self):
     return 2*(self.length+self.width)
  def Area(self):
     return (self.length*self.width)
  def display(self):
     print("length:",self.length)
     print("width",self.width)
     print("perimeter",self.Perimeter())
     print("area",self.Area())
     
class Parallelepipede(Rectangle):
   def __init__(self,length,width,height):
     Rectangle.__init__(self,length,width)
     self.height=height
   def volume(self):
     return (self.length*self.width*self.height)
     
my=Rectangle(7,5)
print(my.display())
#my1=Parallelepipede(7,5,2)
#print(my1.volume())

class Person(object):
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
    print("name:",self.name)
    print("age:",self.age)
class Student(Person):
  def __init__(self,name,age,section):
    Person.__init__(self,name,age)
    self.section=section
  def displayStudent(self):
     print("name:",self.name)
     print("age:",self.age)
     print("section:",self.section)
student=Student('gayathri',20,'first')
print(student.displayStudent())


class bankaccount(object):
  def __init__(self,accno,name,bal):
    self.accno=accno
    self.name=name
    self.bal=bal
    
  def deposit(self,d):
      self.bal=self.bal+d
  def withdraw(self,w):
      if self.bal<w:
        print('not possible')
      else:
        self.bal=self.bal-w
        
  def bankfee(self):
    self.bal=(0.95)self.bal
  def display(self):
        print("Account Number : " , self.accno)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.bal , " $") 
     
