class composition_mx:
  def min_id(self):
    '''
    return the minimum id of the nodes in the graph
    '''
    if (self.get_node_ids() == []):
      return 0
    minid = self.get_node_ids()[0]
    for i in range (len(self.get_node_ids())):
      if (self.get_node_ids()[i]<minid):
        minid = self.get_node_ids()[i]
    return minid

  def max_id(self):
    '''
    return the maximum id of the nodes in the graph
    '''
    if (self.get_node_ids() == []):
      return 0
    maxid = self.get_node_ids()[0]
    for i in range (len(self.get_node_ids())):
      if (self.get_node_ids()[i]>maxid):
        maxid = self.get_node_ids()[i]
    return maxid


  def shift_indices(self,n):
    '''
    Add n to the indice of every node in the graph
    '''
    d = {}
    for i in (self.get_nodes()):
      i.shift_indices_nodes(n)
      d[i.get_id()] = i
    self.nodes = d
    self.inputs = [x+n for x in self.inputs]
    self.outputs = [x+n for x in self.outputs]


  def iparallel(self, g):
    '''
    add the graph g to the graph without changing g
    '''
    #réarrange les indices de self
    maxi = g.max_id()
    self.shift_indices(maxi+1)
    #ajoute les noeuds de g à self
    self.get_id_node_map().update(g.get_id_node_map())
    #ajoute les inputs et outputs de g à self
    for i in range (len(g.get_input_ids())):
      self.add_input_id(g.get_input_ids()[i])
    for i in range (len(g.get_output_ids())):
      self.add_output_id(g.get_output_ids()[i])


  def parallel(self,g):
    '''
    output : graph
    return the parallel composition of self and g
    '''
    #copie self dans result puis comme iparallel
    result = self.copy()
    maxi = g.max_id()
    result.shift_indices(maxi+1)
    result.get_id_node_map().update(g.get_id_node_map())
    for i in range (len(g.get_input_ids())):
      result.add_input_id(g.get_input_ids()[i])
    for i in range (len(g.get_output_ids())):
      result.add_output_id(g.get_output_ids()[i])
    return result


  def icompose(self,g):
    '''
    change self into the sequential composition of self and g
    '''
    s_outputs = self.get_output_ids()
    g_inputs = g.get_input_ids()

    if (len(s_outputs) != len(g_inputs)):
      raise TypeError("The graphes are not compatible")

    #réarrange les id des nodes de self
    maxi = g.max_id()
    self.shift_indices(maxi+1)
    #complète le dictionnaire de self avec les noeuds de g
    self.get_id_node_map().update(g.get_id_node_map())
    #remplace les outputs de self par les outputs de g
    self.set_output_ids(g.get_output_ids())
    #rajoute des arrêtes entre les outputs de self et les inputs de g
    self.add_edges(s_outputs, g_inputs)


  def compose(self,g):
    '''
    output : graph
    return the sequential composition of self and g
    '''
    g_result = self.copy()
    s_outputs = self.get_output_ids()
    g_inputs = g.get_input_ids()

    if (len(s_outputs) != len(g_inputs)):
      raise TypeError("The graphes are not compatible")
    
    #réarrange les id des nodes de g_result
    maxi = g.max_id()
    g_result.shift_indices(maxi+1)
    #complète le dictionnaire de g_result avec les noeuds de g
    g_result.get_id_node_map().update(g.get_id_node_map())
    #remplace les outputs de g_result par les outputs de g
    g_result.set_output_ids(g.get_output_ids())
    #rajoute des arrêtes entre les outputs de g_result et les inputs de g
    g_result.add_edges(s_outputs, g_inputs)
    return g_result
  
  def connected_parents(self, node, dictres, nb):
    '''
    allows to fill a dictionnary with all the nodes link to one and associate 
    them with a number nb
    '''
    for j in (self.get_node_by_id(node).get_children_ids()):
      if (j not in dictres):
        dictres[j] = nb
        self.connected_parents(j, dictres, nb)
    for h in (self.get_node_by_id(node).get_parent_ids()):
      if(h not in dictres):  
        dictres[h] = nb  
        self.connected_parents(h, dictres, nb)

  def connected_components(self):
    '''
    output : dictionnary, int
    return the number of connected components in the graph and a dictionnary 
    with the indice of the connected components each node is in
    '''
    resdict = {}
    nbcc = 0
    for i in (self.get_node_ids()):
      if (i not in resdict):
        resdict[i] = nbcc
        self.connected_parents(i, resdict, nbcc)
        nbcc = nbcc+1
    return resdict, nbcc