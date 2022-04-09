class point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  
  def n(self):
    '''
    returns a simple tuple
    '''
    return (round(self.x),round(self.y))

  def copy(self):
    '''
    returns a copy of the point
    '''
    return point(self.x,self.y)

  def __eq__(self,p2):
    '''
    output : boolean
    returns true if two point/tuple are equals
    '''
    if isinstance(p2,point) and p2.x == self.x and p2.y == self.y:
      return 1
    elif isinstance(p2,tuple) and p2[0] == self.x and p2[1] == self.y:
      return 1
    else:
      if isinstance(p2,point) or isinstance(p2,tuple):
        return 0
      else : 
        print("wrong type (expected point or tuple) : "+str(type(p2))+" in __eq__()")

  def __str__(self):
    '''
    output: string 
    returns the string to be displayed by print
    '''
    return ("("+str(self.x)+","+str(self.y)+")")

  def get_x(self):
    '''
    output : int
    returns the coordinate x of the point
    '''
    return self.x

  def get_y(self):
    '''
    output : int
    returns the coordinate y of the point
    '''
    return self.y

  def set_x(self,x):
    '''
    initializes the coordinate x of the point at x
    '''
    if isinstance(x,int) or isinstance(x,float):
      self.x = x
    else:
      print("wrong type (expected int) : "+str(type(x))+" in set_x()")

  def set_y(self,y):
    '''
    initializes the coordinate y of the point at y
    '''
    if isinstance(y,int) or isinstance(y,float):
      self.y = y 
    else:
      print("wrong type (expected int) : "+str(type(y))+" in set_y()")
    
  def __add__(self,p2):
    '''
    output : point
    adds two points or a point and a tuple
    '''
    if isinstance(p2,point):
      return point(self.x+p2.x,self.y+p2.y)
    elif isinstance(p2,tuple):
      return point(self.x+p2[0],self.y+p2[1])
    else :
      print("wrong type (expected point or tuple) : "+str(type(p2))+" in __add__()")
  
  def __rmul__(self,s):
    '''
    output : point
    multiplies a point with a scalar
    '''
    if isinstance(s,int) or isinstance(s,float):
      return point(self.x*s,self.y*s)
    else:
      print("wrong type (expected int) : "+str(type(s))+" in __rmul__()")
  
  def __sub__(self,p2):
    '''
    output : point
    subs two points or a point and a tuple
    '''
    if isinstance(p2,point):
      return point(self.x-p2.x,self.y-p2.y)
    elif isinstance(p2,tuple):
      return point(self.x-p2[0],self.y-p2[1])
    else :
      print("wrong type (expected point or tuple) : "+str(type(p2))+" in __sub__()")