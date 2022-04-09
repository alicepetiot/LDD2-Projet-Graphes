from modules.utils import remove_all

class remove_mx: 
  def remove_input_id(self, id_input):
    '''
    remove the id of the input list
    '''
    new_inputs = []
    for i in (self.get_input_ids()):
      if(i != id_input):
        new_inputs.append(i)
    self.set_input_ids(new_inputs)

  def remove_output_id(self, id_output):
    '''
    remove the id of the output list
    '''
    new_outputs = []
    for i in (self.get_output_ids()):
      if(i != id_output):
        new_outputs.append(i)
    self.set_output_ids(new_outputs)

  
  def remove_edge(self, src, tgt):
    '''
    removes an edge between the node src and tgt
    '''
    '''
    if src and tgt in self.get_node_ids():
    '''
    try:
      self.get_id_node_map()[src].remove_child_id(tgt)
      self.get_id_node_map()[tgt].remove_parent_id(src)
    except KeyError:
      if src not in self.get_node_ids():
        print("the id",src,"correspond to any node in the graph")
      if tgt not in self.get_node_ids():
        print("the id",tgt,"correspond to any node in the graph")

  def remove_edges(self, l_src, l_tgt):
    '''
    removes edges between the node list src and tgt
    '''
    try:
      for i in range(len(l_src)):
        self.remove_edge(l_src[i], l_tgt[i])
    except IndexError:
      print("the two lists have different sizes")

  def remove_node_by_id(self, key_id):
    '''
    removes the id in the dictionnary and keeps in memory the value
    '''
    try:
      node = self.get_node_by_id(key_id)
      node_parents = node.get_parent_ids()
      node_childrens = node.get_children_ids()
        
      for i in range(len(node_parents)):
        if node_parents[i] != key_id:
          node_i = self.get_node_by_id(node_parents[i])
          node_i.remove_child_id(key_id)
        
      for j in range(len(node_childrens)):
        if node_childrens[j] != key_id:
          node_i = self.get_node_by_id(node_childrens[j])
          node_i.remove_parent_id(key_id)

      x = self.get_id_node_map().pop(key_id)
      remove_all(self.get_output_ids(),key_id)
      remove_all(self.get_input_ids(),key_id) 
    except KeyError:
      print("the id",key_id,"correspond to any node in the graph")
    
  def remove_nodes_by_id(self,l_key_id):
    '''
    removes all the ids in the dictionnary and keeps in memory the values
    '''
    for i in range(len(l_key_id)):
        self.remove_node_by_id(l_key_id[i])
