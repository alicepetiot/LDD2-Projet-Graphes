class getters_mx:
  def get_input_ids(self):
    '''
    output : int list
    returns the ids of the input nodes
    '''
    return self.inputs

  def get_output_ids(self):
    '''
    output : int list
    returns the ids of the output nodes
    '''
    return self.outputs

  def get_id_node_map(self):
    '''
    output : dictionnary
    returns a dictionnary of the type id:nodes
    '''
    return self.nodes

  def get_nodes(self):
    '''
    output : value of the node list 
    returns the values of the dictionnary
    '''
    return list(self.nodes.values())

  def get_node_ids(self):
    '''
    output : int list 
    returns the keys of the dictionnary
    '''
    return list(self.nodes.keys())

  def get_node_by_id(self, id_node):
    '''
    output : node
    returns the node of the id 
    '''
    return self.get_id_node_map()[id_node]

  def get_nodes_by_ids(self, ids):
    '''
    output : nodes list
    returns the nodes list of the ids list 
    '''
    l = []
    for i in range(len(ids)):
      l.append(self.get_node_by_id(ids[i]))
    return l