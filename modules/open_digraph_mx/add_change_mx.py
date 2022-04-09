class add_change_mx:
  def add_input_id(self, id_input):
    '''
    adds a input id to the inputs list of the digraph
    '''
    if id_input in self.get_node_ids():
      self.inputs.append(id_input)

  def add_output_id(self, id_output):
    '''
    adds a output id to the outputs list of the digraph
    '''
    if id_output in self.get_node_ids():
      self.outputs.append(id_output)

  def add_edge(self, src, tgt):
    '''
    creates an edge between the node src and tgt
    '''
    try:
      self.get_id_node_map()[src].add_child_id(tgt)
      self.get_id_node_map()[tgt].add_parent_id(src)
    except KeyError:
      if src not in self.get_node_ids():
        print("the id",src,"correspond to any node in the graph")
      if tgt not in self.get_node_ids():
        print("the id",tgt,"correspond to any node in the graph")

  def add_edges(self, l_src, l_tgt):
    '''
    creates edges between the node list src and tgt
    '''
    try:
      for i in range(len(l_src)):
        self.add_edge(l_src[i], l_tgt[i])
    except IndexError:
      print("the two lists have different sizes")

  def new_id(self):
    '''
    output : int
    returns an id not used in the graph
    '''
    g = self.get_node_ids()
    if g == []:
      return 0
    return max(g)+1
    
  def change_id(self, node_id, new_id):
    '''
    changes the id of the node in the graph
    '''
    if new_id in self.get_id_node_map():
      msg = "new_id already exist"
      raise TypeError(msg)

    '''replaces the id in the node by new_id'''
    self.get_node_by_id(node_id).set_id(new_id) 

    for b in range (len(self.get_input_ids())):
      ''' changes the node_id in the input list by the new_id'''
      if (node_id == self.get_input_ids()[b]):
        self.get_input_ids()[b]=new_id

    for d in range (len(self.get_output_ids())):
      ''' changes the node_id in the output list by the new_id'''
      if (node_id == self.get_output_ids()[d]):
        self.get_output_ids()[d]=new_id

    for i in range (len(self.get_nodes())):
      '''replaces node_id by new_id in the node of the children list of node_id'''
      for j in range (len(self.get_nodes()[i].get_children_ids())):
        if (node_id == self.get_nodes()[i].get_children_ids()[j]):
          self.get_nodes()[i].get_children_ids()[j] = new_id

      '''replaces node_id by new_id in the node of the parent list of node_id'''
      for h in range (len(self.get_nodes()[i].get_parent_ids())):
        if (node_id == self.get_nodes()[i].parents[h]):
          self.get_nodes()[i].parents[h] = new_id

    '''deletes node_id of the dictionnary and gives the value for the key new_id'''
    self.get_id_node_map()[new_id] = self.get_id_node_map().pop(node_id)

  
  def change_ids(self, node_list):
    new_list = sorted(node_list, key = lambda t: t[1])
    for i in range(len(new_list)):
      self.change_id(new_list[i][0], new_list[i][1])
  
  
