import sys
sys.path.append('../') 

from modules.utils import count_occurrences

class well_formed_mx:
  def id_inputs_in_nodes(self):
    '''
    output : boolean
    returns true if the inputs list is in the keys list of the nodes 
    '''
    return all(item in self.get_node_ids() for item in self.inputs)

  def id_outputs_in_nodes(self):
    '''
    output : boolean
    returns true if the outputs list is in the keys list of the nodes 
    '''
    return all(item in self.get_node_ids() for item in self.outputs)

  def id_nodes_in_keys(self):
    '''
    return True if the nodes ids are in the keys of the dictionnary
    '''
    for i in range(len(self.nodes)):
      if self.get_nodes()[i].get_id() != self.get_node_ids()[i]:
        return False
    return True 

  def valide_edges_graph(self):
    '''
    output : boolean
    returns true if j appears n times in the children of index node i 
    then i must appear n times in the parents of index node j 
    '''
    dict_node = self.get_id_node_map()
    '''
    scrolls through the list of node keys
    watches for each node the first value of his children, then the second
    one to j 
    '''
    for i in range(len(self.get_node_ids())):
      for j in range(len(self.nodes[i].get_children_ids())):

        '''
        gets the list of children of node i
        '''
        list_children_node_i = dict_node[i].get_children_ids()
        '''
        gets the j-th value from the list of children of node i 
        '''
        occurence_j = list_children_node_i[j]
        '''
        gets the list of parents of node j
        '''
        list_parents_node_j = dict_node[occurence_j].get_parent_ids()
        '''
        gets the if of node i
        '''
        occurence_id_node_i = dict_node[i].get_id()

        '''
        return false if the number of occurrences of j in the list of children
        of node i is not equal to the number of occurrences of i in the list of
        parents of node j
        '''
        if  not(count_occurrences(list_children_node_i,occurence_j) == 
                count_occurrences(list_parents_node_j,occurence_id_node_i)):
          return False;

    '''
    same thing but with the parents
    '''
    for i in range(len(self.get_node_ids())):
      for j in range(len(self.nodes[i].get_parent_ids())):

        list_parents_node_i = dict_node[i].get_parent_ids()
        occurence_j_bis = list_parents_node_i[j]
        list_children_node_j = dict_node[occurence_j_bis].get_children_ids()
        occurence_id_node_i_bis = dict_node[i].get_id()

        '''
        returns false if the number of occurrences of j in the parents list of 
        node i is not equal to the number of occurrences of i in the children 
        list of the node j
        '''
        if not(count_occurrences(list_parents_node_i,occurence_j_bis) ==
                count_occurrences(list_children_node_j,occurence_id_node_i_bis)):
          return False;
    return True;

  def is_well_formed(self):
    '''
    output : boolean
    verifies that a graph is always well formed meaning that the functions
    id_inputs_in_nodes(), id_outputs_in_nodes() and valide_edges_graph()
    returns true
    '''
    return  (self.id_inputs_in_nodes() and 
            self.id_outputs_in_nodes() and 
            self.id_nodes_in_keys() and
            self.valide_edges_graph())