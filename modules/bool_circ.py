import sys
sys.path.append('../') # allows us to fetch files from the project root

from modules.open_digraph import *

class bool_circ(open_digraph):
  def is_well_formed_circ(self):
    '''
    output : boolean
    returns true if the boolean circuit is cyclic and 
    verifies the degree of a node in function of his label 
    '''
    if (not self.is_cyclic()):
      for i in (self.get_node_ids()):
        lab = self.get_node_by_id(i).get_label()
        if lab == '&' and (not self.node_outdegree(i)==1):
          return False
        elif lab == '|' and (not self.node_outdegree(i)==1):
          return False
        elif lab == ' ' and (not self.node_indegree(i)==1):
          return False 
        elif lab == '~' and ((not self.node_outdegree(i)==1)or(not self.node_indegree(i)==1)):
          return False
        elif lab == '^' and ((not self.node_indegree(i)==2) or (not self.node_outdegree(i)==1)):
          return False
        elif lab == '0' and ((not self.node_outdegree(i)==1) or (not self.node_indegree(i)==0)):
          return False
        elif lab == '1' and ((not self.node_outdegree(i)==1) or (not self.node_indegree(i)==0)):
          return False 
      return True
    else :
      return False
    
  def __init__(self,g):
    '''
    initializes boolean circuit 
    '''
    if isinstance(g,open_digraph):
      super().__init__(g.inputs.copy(), g.outputs.copy(), [node.copy() for node in g.get_nodes()])
    if (not self.is_well_formed_circ()) : 
      raise NameError("Le circuit booléen n'est pas bien formé")

  def convert_circ_digraph(self):
    '''
    output : digraph
    converts a boolean circuit in digraph
    '''
    g = open_digraph([],[],[])
    g.inputs = self.inputs
    g.outputs = self.outputs
    g.nodes = self.nodes
    return g

  def parse_parentheses(*args):
    '''
    output : graph and dictionnary
    create a graph with characters chains
    return the order of the nodes in the inputs 
    '''
    g = bool_circ(open_digraph.empty())
    for s in range(len(args)):
      curent_node = g.add_node('',[],[])
      g.add_output_id(curent_node)
      s2 = ''
      for i in (args[s]):
        if (i == '('):
          #récupère le label actuel et y ajoute s2
          l = g.get_node_by_id(curent_node).get_label()
          g.get_node_by_id(curent_node).set_label(l+s2)
          #ajoute un nouveau noeud au graphe avec curent_node comme enfant
          curent_node = g.add_node('',[],[curent_node])
          s2 = ''
        elif (i == ')'):
          #récupère le lable actuel et ajoute s2
          l = g.get_node_by_id(curent_node).get_label()
          g.get_node_by_id(curent_node).set_label(l+s2)
          #ajoute un nouveau noeud avec curent_node comme parent
          curent_node = g.get_node_by_id(curent_node).get_children_ids()[0]
          s2 = ''
        else:
          s2 = s2+i
    #initialise le dictionnaire
    indict={}
    compt=0
    node_ids = g.get_node_ids()
    for j in (node_ids):
      #repère les co-feuilles
      if (g.get_node_by_id(j).get_parent_ids() == []):
        #si déjà vu, on lance la fusion des noeuds
        if (g.get_node_by_id(j).get_label() in indict):
          g.fusion(g.get_input_ids()[indict[g.get_node_by_id(j).get_label()]],j, label=None)
        else:  
          g.add_input_id(j)
          indict[g.get_node_by_id(j).get_label()]=compt
          g.get_node_by_id(j).set_label('')
          compt=compt+1
    return g,indict

  '''
  def random_bool_circ(n, bound,inputs=1,outputs=1):
    
    output : bool_circ
    return a random bool circ based on a random graph
    #le circuit booleen n'est pas bien formé
    
    g = open_digraph.random(n,bound,inputs=0,outputs=0,form="DAG")
    for i in (g.get_node_ids()):
      #ajoute les outputs
      if(g.get_node_by_id(i).get_children_ids() == []):
        g.add_output_id(i)
      #ajoute les inputs
      if(g.get_node_by_id(i).get_parent_ids() == []):
        g.add_input_id(i)
    
    #corrige les inputs
    if (len(g.get_input_ids())!=inputs):
      #si trop d'inputs
      while(len(g.get_input_ids())>inputs):
        r1 = random.choice(g.get_input_ids())
        r2 = random.choice(g.get_input_ids())
        new_id = g.add_node(' ',[],[r1,r2])
        g.add_input_id(new_id)
        g.remove_input_id(r1)
        g.remove_input_id(r2)
      #si pas assez d'inputs
      while(len(g.get_input_ids())<inputs):
        if (g.get_input_ids()!=[]):
          r = random.choice(g.get_input_ids())
        else :
          r = random.choice(g.get_node_ids())
        new_id1 = g.add_node(' ',[],[r])
        new_id2 = g.add_node(' ',[],[r])
        g.add_input_id(new_id1)
        g.add_input_id(new_id2)
        g.remove_input_id(r)
    
    #corrige les outputs
    if (len(g.get_output_ids())!=outputs):
      #si trop d'outputs
      while(len(g.get_output_ids())>outputs):
        r1 = random.choice(g.get_output_ids())
        r2 = random.choice(g.get_output_ids())
        new_id = g.add_node(' ',[r1,r2],[])
        g.add_output_id(new_id)
        g.remove_output_id(r1)
        g.remove_output_id(r2)
      #si pas assez d'outputs
      while(len(g.get_output_ids())<outputs):
        if (g.get_output_ids()!=[]):
          r = random.choice(g.get_output_ids())
        else :
          r = random.choice(g.get_node_ids())
        new_id1 = g.add_node('',[r],[])
        new_id2 = g.add_node('',[r],[])
        g.add_output_id(new_id1)
        g.add_output_id(new_id2)
        g.remove_output_id(r)
  
    for i in (g.get_node_ids()): 
      #modifie le label du noeud en un label d'opérateur unaire
      if(g.node_indegree(i) == 1 and g.node_outdegree(i) == 1):
        r = random.randint(0,1)
        if (r==0):
          g.get_node_by_id(i).set_label(' ')
        else :
          g.get_node_by_id(i).set_label('~')
      
      if(g.node_indegree(i) > 1):
        #modifie le label du noeud en un label d'opérateur binaire
        if (g.node_outdegree(i) == 1):
          r = random.randint(0,1)
          if (r==0):
            g.get_node_by_id(i).set_label('&')
          else :
            g.get_node_by_id(i).set_label('|')
        #sépare le noeud en deux
        if (g.node_outdegree(i)>1):
          #crée les nouveaux noeuds 
          new_node_id = g.add_node('', [i], g.get_node_by_id(i).get_children_ids())
          new_node = g.add_node('',g.get_node_by_id(i).get_parent_ids(),[new_node_id])
          g.remove_node_by_id(i)
          #ajoute le label d'opérateur binaire
          r = random.randint(0,1)
          if (r==0):
            g.get_node_by_id(new_node).set_label('&')
          else :
            g.get_node_by_id(new_node).set_label('|')
    result = bool_circ(g)
    return result
  '''
  
  def binaire(nb,reg_taille=8):
    '''
    output : bool_circ
    return a boolean circuit with the binaire structure of the number nb in size reg_taille
    '''
    b = bin(nb)[2:]
    if (len(b)>reg_taille):
      raise ("Place insuffisante")
    g = bool_circ(open_digraph.empty())
    l = reg_taille - len(b)
    for i in range (l):
      new_id = g.add_node('0',[],[])
      g.add_output_id(new_id)
    for s in (b):
      new_id = g.add_node(s,[],[])
      g.add_output_id(new_id)
    return g