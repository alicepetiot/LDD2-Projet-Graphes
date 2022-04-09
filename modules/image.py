import sys
sys.path.append('../')

from modules.point import *
from modules.open_digraph import *
from PIL import Image, ImageDraw
import math 
import random 

width = 400  
height = 400 

class Image2():
  def __init__(self,g,w,h,form="manual"):
    if form=="manual":
      img = Image.new("RGB",(width,height),'white')
      draw = ImageDraw.Draw(img)
      draw.graph(g,w,h,method="manual",node_pos=dict_pos,input_pos=in_pos,output_pos=out_pos)
      img.save("manual.jpg")
    elif form=="random":
      img = Image.new("RGB",(width,height),'white')
      draw = ImageDraw.Draw(img)
      draw.graph(g,width,height,method="random")
      img.save("random.jpg")
    elif form=="circle":
      img = Image.new("RGB",(width,height),'white')
      draw = ImageDraw.Draw(img)
      draw.graph(g,width,height,method="circle")
      img.save("circle.jpg")
    elif form=="topological":
      img = Image.new("RGB",(width,height),'white')
      draw = ImageDraw.Draw(img)
      draw.graph(g2,width,height,method="DAG_layout")
      img.save("topological.jpg")

  def distance_fixed(p1,dt,s,w,h):
    '''
    @parameters : 
      - p1 : point
      - dt : int
      - s : int
      - w : int
      - h : int 
    ------------------
    @outputs : p2 (point)
    ------------------
    @returns : a fixed position according to the position x,y 
    in the window 
    (right high, right low, left high, left low,width,height)
    '''
    x = p1.get_x()
    y = p1.get_y()

    '''for the y-axis'''
    if (y >= s and y < h/2):
      y2 = y - dt
    elif (y == 50):
      y2 = y 
    else:
      y2 = y + dt 

    '''for the x-axis'''
    if (x >= s and x < w/2):
      x2 = x - dt
    elif (x == 50):
      x2 = x 
    else:
      x2 = x + dt
    return point(x2,y2) 

  def rotate(p,theta,c=point(0,0)):
    '''
    @parameters 
      - theta : int (degree)
      - c : point
    -------------------------
    @output : point 
    -------------------------
    @returns : the position of the point after rotation of angle
    theta around the point c.
    '''
    theta *= math.pi/180 #pour mettre en radian
    x1 = p.get_x() - c.get_x()
    y1 = p.get_y() - c.get_y()
    x = x1 * math.cos(theta) - y1 * math.sin(theta) + c.get_x() 
    y = x1 * math.sin(theta) + y1 * math.cos(theta) + c.get_y() 
    return point(round(x),round(y))

  def slope_angle(p1, p2):
    '''
    @parameters
      - p1 : point
      - p2 : point
    -----------------------
    @outputs : int (degree)
    -----------------------
    @returns the angle between the segment of the two point and the
    axis Ox in degree 
    '''
    x1,y1,x2,y2 = p1.get_x(),p1.get_y(),p2.get_x(),p2.get_y()
    deg = 180/math.pi
    if x1==x2:
      if y2>y1:
        return math.pi/2*deg
      else:
        return -math.pi/2*deg
    elif x1>x2:
        return math.atan((y2-y1)/(x2-x1))*deg+math.pi
    else:
      return math.atan((y2-y1)/(x2-x1))*deg

  def max_columns(t):
    '''
    @parameters
      - t : double array
    ---------------------
    @outputs : int 
    ---------------------
    @return the lenght of the most important list
    in columns
    '''
    cpt = 0
    for i in range(len(t)):
      columns = len(t[i])
      if (columns > cpt):
        cpt = columns 
    return cpt 

  def drawarrows(self,p1,p2):
    '''
    @parameters two points.
    @outputs line.
    @returns draws arrows between the two given points.
    '''
    self.line([p1.n(),p2.n()],'black')
    x1,y1,x2,y2 = p1.get_x(),p1.get_y(),p2.get_x(),p2.get_y()
    c = point((x2+x1)/2,(y2+y1)/2)
    cx,cy = c.get_x(),c.get_y()
    dt = 10
    theta = Image2.slope_angle(p1,p2) 
    if x1<=x2:
      px = cx-dt
    else:
      px = cx+dt 
    c,p3,p4 = point(cx,cy),point(px,cy+dt),point(px,cy-dt)
    p3f,p4f = Image2.rotate(p3,theta,c),Image2.rotate(p4,theta,c)
    self.line([p3f.n(),c.n()],'black')
    self.line([p4f.n(),c.n()],'black')
  #we define the method 'arrows' from the function
  #'drawarrows' above for ImageDraw.
  ImageDraw.ImageDraw.arrows = drawarrows

  def drawnodes(self,node,p,verbose=False):
    '''
    @parameters one node, one point and one boolean for the id of the node.
    @outputs point with text.
    @draws the node at the position p and print the id if verbose=True.
    '''
    self.point((p.x,p.y),"green")
    self.text((p.x-5,p.y-20),node.get_label(),fill="red")
    if verbose:
      self.text((p.x-5,p.y-30),str(node.get_id()), fill="blue")
  #we define the method 'nodes' from the function
  #'drawnodes' above for ImageDraw
  ImageDraw.ImageDraw.nodes = drawnodes

  def drawgraph(self,g,w,h,method="manual",node_pos=None,input_pos=None,output_pos=None):
    '''
    @parameters
      - g an open_digraph.
      - manual which specifies that we chose the positions ourselves.
      - node_pos a dictionary which associates to the nodes a position.
      - input_pos a list of positions for the incoming arrows. 
      - output_pos a list of positions for the outgoing arrows.
    -------------------------------------------------------------------
    @outputs void.
    --------------
    @draws a open_digraph.
    '''   
    if method=="random":  
      r = Image2.random_layout(g,w,h)
      node_pos = r[0]
      input_pos = r[1]
      output_pos = r[2]
    elif method=="circle":
      c = Image2.circle_layout(g,w,h)
      node_pos = c[0]
      input_pos = c[1]
      output_pos = c[2]
    elif method=="DAG_layout":
      d = Image2.DAG_layout(g,w,h)
      node_pos = d[0]
      input_pos = d[1]
      output_pos = d[2]

    keys = g.get_node_ids()
    size_dict = len(g.get_id_node_map())
    size_in = len(g.get_input_ids())
    size_out = len(g.get_output_ids())

    '''
    draws nodes at the associates positions in node_pos.
    '''
    for i in range(size_dict):
      nodes = g.get_nodes()[i]
      ids = nodes.get_id()
      self.nodes(nodes,node_pos[ids],True)

    '''
    draws arrows between the current node and his childrens.
    '''  

    for i in range(size_dict):
      id_node = keys[i]
      node = g.get_node_by_id(id_node)
      parents = node.get_parent_ids()
      for j in range(len(parents)):
        ids = parents[j]
        self.arrows(node_pos[ids],node_pos[id_node])

    '''
    draws arrows between the position of the node in the
    input list of the graph given above and the position
    associated in the list input_pos.
    '''

    for i in range(size_in):
      idin = g.get_input_ids()[i]
      self.arrows(input_pos[i],node_pos[idin])

    '''
    draws arrows between the position of the node in the
    output list of the graph given above and the position
    associated in the list output_pos.
    '''
    for i in range(size_out):
      idout = g.get_output_ids()[i]
      self.arrows(node_pos[g.get_output_ids()[i]],output_pos[i])
  ImageDraw.ImageDraw.graph = drawgraph

  def random_layout(g, width, height,distance=True):
    '''
    @parameters 
      - width int 
      - height int 
      - distance boolean
    ---------------------
    @outputs [dictionnary,list,list]
    ---------------------------------
    @returns nodes positions associates to an open_digraph and 
    random position for the inputs and outputs nodes if distance is false
    else determines a fixed position according to the position of the node 
    in the window (right high, right low, left high, left low).
    '''
    if (width <= 0 or height <= 0):
      print("width <= 0 or height <= 0 in random_layout line 1112")
    if (not isinstance(width,int) or not isinstance(height,int)):
      print("width or height not int in random_layout 1112")

    '''
    variables
    '''
    start = 50 #smallest position in x and y that the node can take
    ordo_end = height - 50 #largest position in y that the node can take
    absc_end = width - 50 #largest position in x that the node can take
    dt = start - 2 #delta for the point
    dict_key = g.get_node_ids() #keys list of the graph
    inputs = g.get_input_ids() #inputs list of the graph
    outputs = g.get_output_ids() #outputs list of the graph
    node_pos = {} #dictionary of the associated positions for the node in the graph
    input_pos = [] #list of associated positions for the inputs nodes
    output_pos = [] #list of associated positions for the outputs nodes

    '''
    defines randomly the position x and y in the window for each nodes 
    in the graph and adds them in node_pos
    '''
    for key in dict_key:
        x = random.randint(start, absc_end)
        y = random.randint(start, ordo_end)
        node_pos[key] = point(x,y) 

    '''
    if distance is true then we defines the distances for the inputs-outputs
    else we determines randomly the positions of the points
    '''
    if distance:
      for i in inputs:       
        p1 = node_pos[i]
        p2 = Image2.distance_fixed(p1,dt,start,width,height)
        input_pos.append(p2)   

      for o in outputs:
        p1 = node_pos[o]
        p2 = Image2.distance_fixed(p1,dt,start,width,height)
        output_pos.append(p2)   
    else:
      for i in range(len(inputs)):
          x = random.randint(start, absc_end)
          y = random.randint(start, ordo_end)
          input_pos.append(point(x,y))

      for o in range(len(outputs)):
          x = random.randint(start, absc_end)
          y = random.randint(start, ordo_end)
          output_pos.append(point(x,y))
    '''
    At the end we returns the node_pos, input_pos and output_pos 
    '''
    return node_pos,input_pos,output_pos  

  def circle_layout(g,w,h):
    '''
    @parameters 
      - g : open_digraph
      - w : int
      - h : int
    ---------------------
    @returns 
      - node_pos a dictionnary with the position of the node in circle
      - input_pos and output_pos a list of position determinated 
    '''
    start = 50 
    dt = start - 2 
    p0 = point(width/2,start)
    c = point(w/2,h/2)
    keys = g.get_node_ids()
    nb_nodes = len(keys)
    theta = 360/nb_nodes
    node_pos = {}
    input_pos = []
    output_pos = []
    inputs = g.get_input_ids() 
    outputs = g.get_output_ids() 

    for id_node in keys: 
      node_pos[id_node] = p0 
      p0 = Image2.rotate(p0,theta,c)

    for i in inputs:       
      p1 = node_pos[i]
      p2 = Image2.distance_fixed(p1,dt,start,w,h)
      input_pos.append(p2)   

    for o in outputs:
      p1 = node_pos[o]
      p2 = Image2.distance_fixed(p1,dt,start,w,h)
      output_pos.append(p2) 

    return node_pos,input_pos,output_pos

  def DAG_layout(g,w,h):
    '''
    @parameters 
      - g : open_digraph
      - w : width
      - h : height
    ----------------------
    @returns
      - node_pos a dictionnary of the position of the node accorting to topological sorting
      - input_pos and output_pos a list of position determinated 
    '''
    res = g.topological_sorting()
    print(res)
    start = 50 
    dt = start - 2 
    keys = g.get_node_ids()
    node_pos = {}
    input_pos = []
    output_pos = []
    inputs = g.get_input_ids() 
    outputs = g.get_output_ids() 
    nb_lines = len(res)
    dx = (h-(2*start))/nb_lines
    nb_columns = Image2.max_columns(res)
    dy = (w-(2*start))/nb_columns

    for i in range(nb_lines):
      for j in range(len(res[i])):
        node_pos[res[i][j]] = point(start+j*dx,start+i*dy)

    for k,v in node_pos.items():
      print(str(v))  

    for i in inputs:       
      p1 = node_pos[i]
      p2 = Image2.distance_fixed(p1,dt,start,w,h)
      input_pos.append(p2)   

    for o in outputs:
      p1 = node_pos[o]
      p2 = Image2.distance_fixed(p1,dt,start,w,h)
      output_pos.append(p2) 

    return node_pos,input_pos,output_pos


'''
@Affichages
'''

'''manual'''
n0 = node(0,'a',[8,4,1],[1,7])
n1 = node(1,'b',[0,4],[0])
n4 = node(4,'c',[7],[1,0])
n7 = node(7,'d',[0],[4,8])
n8 = node(8,'e',[7],[0])
p0 = point(200,100)
p1 = point(100,200)
p4 = point(150,300)
p7 = point(250,300)
p8 = point(300,200)
p2 = point(50,150)
p3 = point(350,150)
p5 = point(300,350)
g1 = open_digraph([1,8],[7],[n0,n1,n4,n7,n8])
dict_pos = {0:p0,1:p1,4:p4,7:p7,8:p8}
in_pos = [p2,p3]
out_pos = [p5]
'''acyclic'''
n02 = node(0,'a',[],[1,2])
n12 = node(1,'b',[0],[3,4])
n22 = node(2,'c',[0],[])
n32 = node(3,'d',[1],[])
n42 = node(4,'e',[1],[])
g2 = open_digraph([],[],[n02,n12,n22,n32,n42])
'''draw'''
im1 = Image2(g1,width,height,form="manual")
im2 = Image2(g1,width,height,form="random")
im3 = Image2(g1,width,height,form="circle")
im4 = Image2(g2,width,height,form="topological")