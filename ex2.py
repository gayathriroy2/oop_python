mport math
class Circle(object):
  def __init__(self,a,b,r):         
        self.a = a         
        self.b = b         
        self.r = r
        
  def area(self):
      print(math.pi*self.r**2)
  def perimeter(self):
      print(2*math.pi*self.r)
  def test(self,x,y):
     if x<=self.a+self.r and x>=self.a-self.r:
       if y<=self.b+self.r and y>=self.b-self.r:
         print(True)
         
my=Circle(2,1,3)
my.area()
my.perimeter()
my.test(4,-1)

class computation(object):
  def __init__(self):
    pass
  def fact(self,n):
    
    if n==0:
      print(1)
    elif n==1:
      print(1)
    else:
      return (n * self.fact(n-1))
   
  def sum(self,n):
    x=0
    for i in range(1,n+1):
      x=x+i
    print(x)
  def prime(self,n):
    if n>1:
      for i in range(2,n):
        if n%2==0:
          print('not')
          break
      print("yes")
          
my=computation()
my.fact(6)
my.sum(3)
my.prime(10)
