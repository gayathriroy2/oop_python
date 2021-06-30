class mystr(object):
  def __init__(self,s):
    self.s=s
  def append(self,p):
    print(self.s+p)
  def pop(self,n):
    a=self.s[n]
    if len(self.s)>=n+2:
      new = self.s[:n]+self.s[n+1:]
    else:
      new=self.s[:n]
    print(a)
    print(new)
my=mystr('abcd')
my.append('efg')
my.pop(3)
