from modules.open_digraph_mx.setters_mx import *
from modules.open_digraph_mx.composition_mx import *
from modules.open_digraph_mx.getters_mx import *
from modules.open_digraph_mx.add_change_mx import *
from modules.open_digraph_mx.degree_mx import *
from modules.open_digraph_mx.remove_mx import *
from modules.open_digraph_mx.tri_topologique_mx import *
from modules.open_digraph_mx.well_formed_mx import *
from modules.node import *

class open_digraph(
    setters_mx,getters_mx,degree_mx,
    add_change_mx,remove_mx,well_formed_mx,
    composition_mx,tri_topologique_mx
  ): 
  def __init__(self, inputs, outputs, nodes):
    '''
    inputs: int list; the ids of the input nodes
    outputs: int list; the ids of the output nodes
    nodes: node list;
    '''
    self.inputs = inputs
    self.outputs = outputs
    self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict

  def __str__(self):
    '''
    returns the string to be displayed by print
    '''
    return ("("+str(self.inputs)+","
            +str(self.outputs)+","+str(self.nodes)+")")

  def __repr__(self):
    '''
    returns the string to be displayed by print
    '''
    return "open_digraph"+str(self)

  def empty():
    '''
    output : graph
    returns an empty graph
    '''
    return open_digraph([],[],[])

  def copy(self):
    '''
    output : open_digraph
    returns a copy of the open_digraph
    '''
    return open_digraph(self.inputs.copy(), self.outputs.copy(), [node.copy() for node in self.nodes.values()])
  
  def add_node(self, label, parents,children):
    '''
    output : int
    returns the id of the new node linked to the parent and children id nodes
    '''

    '''
    creates a new id for the new node and initializes the new node
    with the value new id and the parameters label, parents and children
    '''

    new_id = self.new_id()
    init_new_node = node(new_id, label, [], [])

    '''
    creates a list of the lenght of the parents list in parameter with
    the value of the new id
    for example : if the new id is 4 and the parents list is [1,2,3]
    then we creates a l_parents list [4,4,4]
    (resp. l_childs)
    '''
    l_parents = [new_id]*len(parents)
    l_childs = [new_id]*len(children)

    '''
    adds the new node in the nodes dictionnary
    keys = new id 
    value = init_new_node
    '''
    self.nodes[new_id] = init_new_node
    '''
    if the new node parents list is [1,2,3] then we need to add the new
    id at the children list of the node 1,2 and 3 (with l_childs = [4,4,4]
    in this case)
    (resp. children)
    '''
    self.add_edges(parents, l_parents)
    self.add_edges(l_childs, children)

    return init_new_node.id

  def in_dictionnary(self,key):
    '''returns true if the key is in the dictionnary'''
    return key in self.get_id_node_map()

  
  def normalise_ids(self):
    '''
    changes the ids of the graph from 0 to n-1 if the graph size is n
    '''
    ids = sorted(self.get_node_ids())
    k = len(ids)-1
    for key in range(len(ids)):
      if not self.in_dictionnary(key):
        self.change_id(ids[k],key)
        k -= 1

  def adjacency_matrix(self):
    '''
    returns a adjacency matrix of the graph
    '''
    l = len(self.get_nodes())
    matrix = [[0]*l for _ in range(l)]
    self.normalise_ids()
    for i in range(len(self.get_nodes())):
      if (self.get_node_by_id(i).parents != []):
        for j in range(len(self.get_node_by_id(i).parents)):
          v = self.get_node_by_id(i).parents[j]
          matrix[i][v] = matrix[i][v] + 1
    return matrix

  def graph_from_adjency_matrix(matrix):
    '''
    returns a multigraph based on a matrix
    '''
    g = open_digraph([],[],[])
    lenght = len(matrix)
    for i in range(lenght):
      if (i>=0 and i<=25):
        g.add_node(chr(i+97),[],[])
      else :
        print("Le graphe a atteint la taille maximale")
    for i in range(len(g.get_node_ids())):
      for j in range(len(g.get_node_ids())):
        for k in range(matrix[i][j]):
          g.add_edge(i,j)
    return g

  def random(n,bound,inputs=0,outputs=0,form="free"):
    '''
    return a new graph according to a matrix which is
    defines in his form by the word in parameters
    '''
    if form=="free":
      g = open_digraph.graph_from_adjency_matrix(random_matrix(n,bound))
    elif form=="DAG":
      g = open_digraph.graph_from_adjency_matrix(random_matrix(n,bound,True))
    elif form=="oriented":
      g = open_digraph.graph_from_adjency_matrix(random_matrix(n,bound,"oriented"))
    elif form=="loop-free oriented":
      g = open_digraph.graph_from_adjency_matrix(random_matrix(n,bound,True,"oriented"))
    elif form=="undirected":
      g = open_digraph.graph_from_adjency_matrix(random_matrix(n,bound,"symetric"))
    elif form=="loop-free undirected":
      g = open_digraph.graph_from_adjency_matrix(random_matrix(n,bound,True,"symetric"))
    elif form=="triangular":
      g = open_digraph.graph_from_adjency_matrix(random_matrix(n,bound,"triangular"))
    elif form=="loop-free triangular":
      g = open_digraph.graph_from_adjency_matrix(random_matrix(n,bound,True,"triangular"))
    
    key_max = max(g.get_node_ids())
    for i in range(inputs):
      rand = random.randint(0,key_max)
      g.add_input_id(rand)

    for j in range(outputs):
      rand = random.randint(0,key_max)
      g.add_output_id(rand)

    return g

  def is_cyclic(self):
    '''
    output : boolean
    returns true if the digraph is cyclic else false
    '''
    g = self.copy()
    count = 0
    leng = len(g.get_nodes())
    nodes = g.get_nodes()
    while (leng!=0):
      for i in (nodes):
        if i.get_children_ids() == []:
          node_id = i.get_id()
          g.remove_node_by_id(node_id)
        else : 
          count = count + 1
      if (count == leng):
        return True
      leng = len(g.get_nodes())
      nodes = g.get_nodes()
      count = 0
    return False