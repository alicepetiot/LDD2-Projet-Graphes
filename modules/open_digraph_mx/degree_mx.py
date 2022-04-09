class degree_mx:
  def node_indegree(self,node_id):
    '''
    output : int
    returns the indegree of the node with the occurences in the inputs
    '''
    indegree = self.get_node_by_id(node_id).indegree()
    for i in self.get_input_ids():
      if(i == node_id):
        indegree = indegree +1
    return indegree
  
  def node_outdegree(self,node_id):
    '''
    output : int
    return the outdegree of the node with the occurences in the output
    '''
    outdegree = self.get_node_by_id(node_id).outdegree()
    for i in (self.get_output_ids()):
      if(i==node_id):
        outdegree = outdegree + 1
    return outdegree
  
  def node_degree(self, node_id):
    '''
    output : int
    return the total degree of the node
    '''
    return self.node_indegree(node_id)+self.node_outdegree(node_id)
  
  def max_indegree(self):
    '''
    output : int
    returns the max in degree of a graph
    '''
    max_degree_in = 0
    for i in (self.get_node_ids()):
      if (self.node_indegree(i) > max_degree_in):
        max_degree_in = self.node_indegree(i)
    return max_degree_in

  def min_indegree(self):
    '''
    output : int
    returns the min in degree of a graph
    '''
    min_degree_in = self.max_indegree()
    nodes = self.get_node_ids()
    if nodes == []:
      return 0 
    for i in (nodes):
      if (self.node_indegree(i) < min_degree_in):
        min_degree_in = self.node_indegree(i)
    return min_degree_in

  def max_outdegree(self):
    '''
    output : int
    returns the max out degree of a graph
    '''
    max_degree_out = 0
    for i in (self.get_node_ids()):
      if self.node_outdegree(i) > max_degree_out:
        max_degree_out = self.node_outdegree(i)
    return max_degree_out

  def min_outdegree(self):
    '''
    output : int
    returns the min out degree of a graph
    '''
    min_degree_out = self.max_outdegree()
    nodes = self.get_node_ids()
    if nodes == []:
      return 0 
    for i in (self.get_node_ids()):
      if self.node_outdegree(i) < min_degree_out:
        min_degree_out = self.node_outdegree(i)
    return min_degree_out

  def max_degree(self):
    '''
    output : int
    returns the degree max of the node of degree max
    '''
    max_degree_tot = 0
    for i in (self.get_node_ids()):
      if self.node_degree(i) > max_degree_tot:
        max_degree_tot = self.node_degree(i)
    return max_degree_tot

  def min_degree(self):
    '''
    output : int
    returns the degree max of the node of degree max 
    '''
    min_degree_tot = self.max_degree()
    nodes = self.get_node_ids()
    if nodes == []:
      return 0 
    for i in (nodes):
      if self.node_degree(i) < min_degree_tot:
        min_degree_tot = self.node_degree(i)
    return min_degree_tot