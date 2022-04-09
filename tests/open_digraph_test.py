import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.open_digraph import *
from modules.utils import *

class InitTest(unittest.TestCase):
  def test_init_open_digraph(self):
    '''__init__graph'''
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    g0 = open_digraph([n0.id],[n1.id],[n0,n1])
    self.assertEqual(g0.inputs,[n0.id])
    self.assertEqual(g0.outputs,[n1.id])
    self.assertEqual(g0.nodes,{0:n0,1:n1})
    self.assertIsInstance(g0,open_digraph)

class DigraphTest(unittest.TestCase):

  def setUp(self):
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    n2 = node(2,'c',[],[])
    n3 = node(3,'d',[],[])
    self.g0 = open_digraph([],[],[])
    self.g1 = open_digraph([0],[1],[n0,n1])
    self.g2 = open_digraph([0],[2],[n0,n1,n2])
    self.g3 = open_digraph([0],[3],[n0,n1,n2,n3])

  def test_copy(self):
    g = self.g1.copy()
    n2 = node(2,'c',[1],[])
    g.inputs = [n2.id]
    self.assertNotEqual(g.inputs, self.g1.inputs)
    self.assertEqual(g.outputs,self.g1.outputs)
    g.nodes.__eq__(self.g0.nodes)
    self.assertIsNot(g, self.g1)

  def test_get_input_ids(self):
    n0 = node(0,'a',[],[1])
    self.assertEqual(self.g0.get_input_ids(), [])
    self.assertEqual(self.g1.get_input_ids(), [n0.id])

  def test_get_output_ids(self):
    n1 = node(1,'b',[0],[])
    self.assertEqual(self.g0.get_output_ids(), [])
    self.assertEqual(self.g1.get_output_ids(), [n1.id])

  def test_get_id_node_map(self):
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    self.assertEqual(self.g0.get_id_node_map(),{})
    self.assertEqual(self.g1.get_id_node_map(),{0:n0,1:n1})

  def test_get_nodes(self):
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    self.assertEqual(self.g0.get_nodes(),[])
    self.assertEqual(self.g1.get_nodes(),[n0,n1])

  def test_get_node_ids(self):
    self.assertEqual(self.g0.get_node_ids(),[])
    self.assertEqual(self.g1.get_node_ids(),[0,1])

  def test_get_node_by_id(self):
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    self.assertEqual(self.g1.get_node_by_id(0),n0)
    self.assertEqual(self.g1.get_node_by_id(1),n1)

  def test_get_nodes_by_ids(self):
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    self.assertEqual(self.g1.get_nodes_by_ids([0]),[n0])
    self.assertEqual(self.g1.get_nodes_by_ids([0,1]),[n0,n1])
    
  def test_set_input_ids(self):
    self.g1.set_input_ids([1,2,3])
    self.assertEqual(self.g1.get_input_ids(), [1,2,3])

  def test_set_output_ids(self):
    self.g1.set_output_ids([0,1,2])
    self.assertEqual(self.g1.get_output_ids(), [0,1,2])

  def test_add_input_id(self):
    self.g1.add_input_id(1)
    self.assertEqual(self.g1.get_input_ids(), [0,1])
    self.g1.add_input_id(4)
    self.assertEqual(self.g1.get_input_ids(), [0,1])

  def test_add_output_id(self):
    self.g1.add_output_id(0)
    self.assertEqual(self.g1.get_output_ids(), [1,0])
    self.g1.add_output_id(-2)
    self.assertEqual(self.g1.get_output_ids(), [1,0])
  
  def test_remove_input_id(self):
    self.g1.remove_input_id(0)
    self.assertEqual(self.g1.get_input_ids(),[])
    self.g1.remove_input_id(3)
    self.assertEqual(self.g1.get_input_ids(),[])
  
  def test_remove_output_id(self):
    self.g1.remove_output_id(2)
    self.assertEqual(self.g1.get_output_ids(),[1])
    self.g1.remove_output_id(1)
    self.assertEqual(self.g1.get_output_ids(),[])

  def test_new_id(self):
    self.assertEqual(self.g1.new_id(),2)

  def test_add_edge(self):
    self.g2.add_edge(1,2)
    self.assertEqual(self.g2.get_id_node_map()[1].get_children_ids(),[2])
    self.assertEqual(self.g2.get_id_node_map()[2].get_parent_ids(),[1])

  def test_add_edges(self):
    self.g3.add_edges([1,1,3],[2,3,3])
    self.assertEqual(self.g3.get_id_node_map()[1].get_children_ids(),[2,3])
    self.assertEqual(self.g3.get_id_node_map()[2].get_parent_ids(),[1])
    self.assertEqual(self.g3.get_id_node_map()[3].get_parent_ids(),[1,3])
    self.assertEqual(self.g3.get_id_node_map()[3].get_children_ids(),[3])
    self.g3.add_edges([1,1,3],[2,4,3])  

  def test_add_node(self):
    n0 = node(0,'a',[],[1,4,4])
    n1 = node(1,'b',[0,4],[4])
    n2 = node(2,'c',[4],[])
    n3 = node(3,'d',[4],[])
    self.g3.add_node('e',[0,1,0],[1,2,3])
    n4 = node(4,'e',[0,1,0],[1,2,3])
    d1 = self.g3.get_id_node_map()
    d2 = {0:n0,1:n1,2:n2,3:n3,4:n4}
    self.assertEqual(d1,d2)

  def test_remove_edge(self):
    self.g3.add_edges([1,1,3],[2,3,3])
    self.g3.remove_edge(1,2)
    self.assertEqual(self.g3.get_id_node_map()[1].get_children_ids(),[3])
    self.assertEqual(self.g3.get_id_node_map()[2].get_parent_ids(),[])

  def test_remove_edges(self):
    self.g3.add_edges([1,1,3],[2,3,3])
    self.g3.remove_edges([1,1],[2,3])
    self.assertEqual(self.g3.get_id_node_map()[1].get_children_ids(),[])
    self.assertEqual(self.g3.get_id_node_map()[2].get_parent_ids(),[])
    self.assertEqual(self.g3.get_id_node_map()[3].get_parent_ids(),[3])
    self.g3.remove_edges([1,-1,0],[0,0])
  
  def test_remove_node_by_id(self):
    n0 = node(0,'a',[1,0,3],[0,3])
    n1 = node(1,'b',[],[0,3])
    n3 = node(3,'c',[1,0],[0])
    g = open_digraph([0,2],[1,2,2],[n0,n1,n3])
    g.remove_node_by_id(0)
    self.assertEqual(g.get_id_node_map(), {1:n1,3:n3})
    self.assertEqual(g.get_input_ids(), [2])
    self.assertEqual(g.get_output_ids(),[1,2,2])
    self.assertEqual(n1.get_children_ids(),[3])
    self.assertEqual(n1.get_parent_ids(),[])
    self.assertEqual(n3.get_parent_ids(),[1])
    self.assertEqual(n3.get_children_ids(),[])
    g.remove_node_by_id(0)

  
  def test_remove_nodes_by_id(self):
    n0 = node(0,'a',[1,0,3],[0,3])
    n1 = node(1,'b',[],[0,3])
    n2 = node(2,'c',[],[])
    n3 = node(3,'c',[1,0],[0])
    g = open_digraph([0,2],[1,2,2],[n0,n1,n2,n3])
    g.remove_nodes_by_id([0,1,2])
    self.assertEqual(g.get_id_node_map(), {3:node(3,'c',[],[])})
    self.assertEqual(g.get_input_ids(), [])
    self.assertEqual(g.get_output_ids(),[])
    self.assertEqual(n3.get_children_ids(),[])
    self.assertEqual(n3.get_parent_ids(),[])
    g.remove_nodes_by_id([19,3])
  

  def test_id_inputs_in_nodes(self):
    self.g3.add_input_id(1)
    self.assertEqual(self.g3.id_inputs_in_nodes(),True)
    self.g3.inputs.append(5)
    self.assertEqual(self.g3.id_inputs_in_nodes(),False)

  def test_id_outputs_in_nodes(self):
    self.g3.add_output_id(2)
    self.assertEqual(self.g3.id_outputs_in_nodes(),True)
    self.g3.outputs.append(-1)
    self.assertEqual(self.g3.id_outputs_in_nodes(),False)

  def test_valide_edges_graph(self):
    self.assertEqual(self.g0.valide_edges_graph(),True)
    self.assertEqual(self.g1.valide_edges_graph(),True)
    n0 = node(0,'a',[],[1])
    n1 = node(1,'c',[0,0],[])
    g = open_digraph([],[],[n0,n1])
    self.assertEqual(g.valide_edges_graph(),False)

  def test_is_well_formed(self):
    self.assertEqual(self.g1.is_well_formed(),True)
    self.assertEqual(self.g2.is_well_formed(),True)
    self.assertEqual(self.g3.is_well_formed(),True)
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0,0],[])
    g1 = open_digraph([],[],[n0,n1])
    self.assertEqual(g1.is_well_formed(),False)
    self.g2.outputs.append(3)
    self.assertEqual(self.g2.is_well_formed(),False)
    self.g3.inputs.append(4)
    self.assertEqual(self.g3.is_well_formed(),False)

  def test_graph_from_adjency_matrix(self):
    matrix = random_matrix(4,4,True,True)
    g = open_digraph.graph_from_adjency_matrix(matrix)
    self.assertEqual(g.is_well_formed(),True)
  
  def test_change_id(self):
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    n2 = node(3,'c',[],[])     
    self.g2.change_id(2,3)
    self.assertEqual(self.g2.get_id_node_map(),{0:n0,1:n1,3:n2})

  
  def test_changes_ids(self):
    d2 = {0:node(0,'a',[],[4]),4:node(4,'b',[0],[]),3:node(3,'c',[],[])}
    n0 = node(0,'a',[3],[2])
    n2 = node(2,'c',[0,3],[])
    n3 = node(3,'d',[],[0,2])
    g3 = open_digraph([2,3],[0,2,2],[n0,n2,n3])
    d3 = {0:n0,1:node(1,'c',[0,2],[]),2:node(2,'d',[],[0,1])}
    self.g2.change_ids([(2,3),(1,4)])
    g3.change_ids([(3,2),(2,1)])
    self.assertEqual(self.g2.get_input_ids(),[0])
    self.assertEqual(self.g2.get_output_ids(),[3])
    self.assertEqual(g3.get_input_ids(),[1,2])
    self.assertEqual(g3.get_output_ids(),[0,1,1])
    self.assertEqual(self.g2.get_id_node_map(),d2)
    self.assertEqual(g3.get_id_node_map(),d3)
  

  def test_in_dictionnary(self):
   self.assertEqual(self.g0.in_dictionnary(0),False) 
   self.assertEqual(self.g1.in_dictionnary(0),True)
   self.assertEqual(self.g1.in_dictionnary(1),True)
   self.assertEqual(self.g1.in_dictionnary(2),False)
   self.assertEqual(self.g2.in_dictionnary(0),True)
   self.assertEqual(self.g2.in_dictionnary(1),True)
   self.assertEqual(self.g2.in_dictionnary(2),True)
   self.assertEqual(self.g2.in_dictionnary(3),False)
   self.assertEqual(self.g3.in_dictionnary(0),True)
   self.assertEqual(self.g3.in_dictionnary(1),True)
   self.assertEqual(self.g3.in_dictionnary(2),True)
   self.assertEqual(self.g3.in_dictionnary(3),True)
   self.assertEqual(self.g3.in_dictionnary(4),False)

  
  def test_normalise_ids(self):
    n4 = node(4,'e',[1,2,4],[3,4])
    n1 = node(1,'b',[3,2],[4])
    n3 = node(3,'d',[4],[1])
    n2 = node(2,'c',[],[4,1])
    g = open_digraph([],[],[n4,n1,n3,n2])
    dg = {0:node(0,'e',[1,2,0],[3,0]),
         1:node(1,'b',[3,2],[0]),
         3:node(3,'d',[0],[1]),
         2:node(2,'c',[],[0,1])}
    g.normalise_ids()
    self.assertEqual(g.get_id_node_map(),dg) 
  
  
  def test_adjacency_matrix(self):
    n0 = node(0,'a',[3],[2])
    n2 = node(2,'c',[0,3],[])
    n3 = node(3,'d',[],[0,2])
    g3 = open_digraph([2,3],[0,2,2],[n0,n2,n3])
    matrix = g3.adjacency_matrix()
    self.assertEqual(matrix[0][0],0)
    self.assertEqual(matrix[0][1],1)
    self.assertEqual(matrix[0][2],0)
    self.assertEqual(matrix[1][0],0)
    self.assertEqual(matrix[1][1],0)
    self.assertEqual(matrix[1][2],0)
    self.assertEqual(matrix[2][0],1)
    self.assertEqual(matrix[2][1],1)
    self.assertEqual(matrix[2][2],0)
    
  def test_node_indegree(self):
    n0 = node(0,'a',[],[1,2,3])
    n1 = node(1,'b',[0,3],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'c',[0],[1])
    g1 = open_digraph([0,1],[2,3],[n0,n1,n2,n3])
    self.assertEqual(g1.node_indegree(0),1)
    self.assertEqual(g1.node_indegree(1),3)
    self.assertEqual(g1.node_indegree(2),2)
    self.assertEqual(g1.node_indegree(3),1)
  
  def test_node_outdegree(self):
    n0 = node(0,'a',[],[1,2,3])
    n1 = node(1,'b',[0,3],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'c',[0],[1])
    g1 = open_digraph([0,2,1],[2,2],[n0,n1,n2,n3])
    self.assertEqual(g1.node_outdegree(0),3)
    self.assertEqual(g1.node_outdegree(1),1)
    self.assertEqual(g1.node_outdegree(2),2)
    self.assertEqual(g1.node_outdegree(3),1)

  def test_node_degree(self):
    n0 = node(0,'a',[],[1,2,3])
    n1 = node(1,'b',[0,3],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'c',[0],[1])
    g1 = open_digraph([0,2,1],[2,2],[n0,n1,n2,n3])
    self.assertEqual(g1.node_degree(0),4)
    self.assertEqual(g1.node_degree(1),4)
    self.assertEqual(g1.node_degree(2),5)
    self.assertEqual(g1.node_degree(3),2)

  def test_max_indegree(self):
    n0 = node(0,'a',[],[1,2,3])
    n1 = node(1,'b',[0,3],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'c',[0],[1])
    g1 = open_digraph([0,2,1],[2,2],[n0,n1,n2,n3])
    self.assertEqual(self.g0.max_indegree(),0)
    self.assertEqual(g1.max_indegree(),3)

  def test_min_indegree(self):
    n0 = node(0,'a',[],[1,2,3])
    n1 = node(1,'b',[0,3],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'c',[0],[1])
    g1 = open_digraph([0,2,1],[2,2],[n0,n1,n2,n3])
    self.assertEqual(self.g0.min_indegree(),0)
    self.assertEqual(g1.min_indegree(),1)

  def test_max_outdegree(self):
    n0 = node(0,'a',[],[1,2,3])
    n1 = node(1,'b',[0,3],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'c',[0],[1])
    g1 = open_digraph([0,2,1],[2,2,0],[n0,n1,n2,n3])
    self.assertEqual(self.g0.max_outdegree(),0)
    self.assertEqual(g1.max_outdegree(),4)

  def test_min_outdegree(self):
    n0 = node(0,'a',[],[1,2,3])
    n1 = node(1,'b',[0,3],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'c',[0],[1])
    g1 = open_digraph([0,2,1],[2,2],[n0,n1,n2,n3])
    self.assertEqual(self.g0.min_outdegree(),0)
    self.assertEqual(g1.min_outdegree(),1)

  def test_max_degree(self):
    n0 = node(0,'a',[],[1,2,3])
    n1 = node(1,'b',[0,3],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'c',[0],[1])
    g1 = open_digraph([0,2,1],[2,2],[n0,n1,n2,n3])
    self.assertEqual(self.g0.max_degree(),0)
    self.assertEqual(g1.max_degree(),5)

  def test_min_degree(self):
    n0 = node(0,'a',[],[1,2,3])
    n1 = node(1,'b',[0,3],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'c',[0],[1])
    g1 = open_digraph([0,2,1],[2,2],[n0,n1,n2,n3])
    self.assertEqual(self.g0.min_degree(),0)
    self.assertEqual(g1.min_degree(),2)

  def test_is_cyclic(self):
    n0 = node(0,'a',[],[1,2])
    n1 = node(1,'b',[0],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'d',[],[])
    g3 = open_digraph([0],[3],[n0,n1,n2,n3])
    self.assertEqual(g3.is_cyclic(),False)
    n0b = node(0,'a',[3],[1,2,3])
    n3b = node(3,'d',[0],[0])
    g2 = open_digraph([0],[3],[n0b,n1,n2,n3b])
    self.assertEqual(g2.is_cyclic(),True)
  

  def test_min_id(self):
    n0 = node(0,'a',[],[1,2])
    n1 = node(1,'b',[0],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'d',[],[])
    g3 = open_digraph([0],[3],[n0,n1,n2,n3])
    g2 = open_digraph([],[],[n3])
    self.assertEqual(g3.min_id(),0)
    self.assertEqual(g2.min_id(),3)
  
  def test_max_id(self):
    n0 = node(0,'a',[],[2])
    n1 = node(1,'b',[],[])
    n2 = node(2,'c',[0],[])
    n3 = node(3,'d',[],[])
    g3 = open_digraph([0],[3],[n0,n1,n2,n3])
    g2 = open_digraph([],[],[n1])
    self.assertEqual(g3.max_id(),3)
    self.assertEqual(g2.max_id(),1)


  def test_shift_indices(self):
    i1 = 2
    i2 = -1
    n0 = node(0,'a',[],[2])
    n1 = node(1,'b',[],[])
    n2 = node(2,'c',[0],[])
    n3 = node(3,'d',[],[])
    g3 = open_digraph([0],[3],[n0,n1,n2,n3])
    g3.shift_indices(i1)
    self.assertEqual(g3.get_node_ids(),[2,3,4,5])
    g3.shift_indices(i2)
    self.assertEqual(g3.get_node_ids(), [1,2,3,4])

  
  def test_iparallel(self):
    n0 = node(0,'a',[],[1,2])
    n1 = node(1,'b',[0],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'d',[1],[])
    n4 = node(1,'e',[],[3])
    g3 = open_digraph([0],[2],[n0,n1,n2])
    g4 = open_digraph([1],[3],[n3,n4])
    g3.iparallel(g4)
    l0 = node(4,'a',[],[5,6])
    l1 = node(5,'b',[4],[6])
    l2 = node(6,'c',[4,5],[])
    g = open_digraph([4,1],[6,3],[l0,l1,l2,n3,n4])
    self.assertEqual(g3.inputs,g.inputs)
    self.assertEqual(g3.outputs,g.outputs)
    self.assertEqual(g3.nodes,g.nodes)


  def test_parallel(self):
    n0 = node(0,'a',[],[1,2])
    n1 = node(1,'b',[0],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'d',[1],[])
    n4 = node(1,'e',[],[3])
    g3 = open_digraph([0],[2],[n0,n1,n2])
    g4 = open_digraph([1],[3],[n3,n4])

    l0 = node(4,'a',[],[5,6])
    l1 = node(5,'b',[4],[6])
    l2 = node(6,'c',[4,5],[])
    
    h = g3.parallel(g4)

    g = open_digraph([4,1],[6,3],[l0,l1,l2,n3,n4])
    self.assertEqual(h.inputs,g.inputs)
    self.assertEqual(h.outputs,g.outputs)
    self.assertEqual(h.nodes,g.nodes)


  def test_icompose(self):
    n0 = node(0,'a',[],[1,2])
    n1 = node(1,'b',[0],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'d',[1],[])
    n4 = node(1,'e',[],[3])
    g3 = open_digraph([0],[2],[n0,n1,n2])
    g4 = open_digraph([1],[3],[n3,n4])
    g3.icompose(g4)

    l0 = node(4,'a',[],[5,6])
    l1 = node(5,'b',[4],[6])
    l2 = node(6,'c',[4,5],[])
    g = open_digraph([4],[3],[l0,l1,l2,n3,n4])
    self.assertEqual(g3.inputs,g.inputs)
    self.assertEqual(g3.outputs,g.outputs)
    self.assertEqual(g3.nodes,g.nodes)
  

  def test_compose(self):
    n0 = node(0,'a',[],[1,2])
    n1 = node(1,'b',[0],[2])
    n2 = node(2,'c',[0,1],[])
    n3 = node(3,'d',[1],[])
    n4 = node(1,'e',[],[3])
    g3 = open_digraph([0],[2],[n0,n1,n2])
    g4 = open_digraph([1],[3],[n3,n4])
    
    h = g3.compose(g4)

    l0 = node(4,'a',[],[5,6])
    l1 = node(5,'b',[4],[6])
    l2 = node(6,'c',[4,5],[])
    g = open_digraph([4],[3],[l0,l1,l2,n3,n4])
    self.assertEqual(h.inputs,g.inputs)
    self.assertEqual(h.outputs,g.outputs)
    self.assertEqual(h.nodes,g.nodes)

  def test_connected_components(self):
    n0 = node(0,'a',[],[3])
    n1 = node(1,'b',[],[5])
    n2 = node(2,'c',[],[4])
    n3 = node(3,'d',[0],[5,7])
    n4 = node(4,'e',[2],[6])
    n5 = node(5,'f',[1,3],[7])
    n6 = node(6,'g',[4],[8,9])
    n7 = node(7,'h',[3,5],[])
    n8 = node(8,'i',[6],[])
    n9 = node(9,'j',[6],[])
    g = open_digraph([0,2],[7],[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])
    res, nb = g.connected_components()
    #print(res)
    #print(nb)
    self.assertEqual(nb,2)
    self.assertEqual(res[5],0)
    self.assertEqual(res[6],1)
  
  def test_dijkstra(self):
    n0 = node(0,'a',[],[3])
    n1 = node(1,'b',[],[4,5,8])
    n2 = node(2,'c',[],[4])
    n3 = node(3,'d',[0],[5,6,7])
    n4 = node(4,'e',[1,2],[6])
    n5 = node(5,'f',[1,3],[7])
    n6 = node(6,'g',[3,4],[8,9])
    n7 = node(7,'h',[3,5],[])
    n8 = node(8,'i',[1,6],[])
    n9 = node(9,'j',[6],[])
    g = open_digraph([0,2],[7],[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])
    #print(g.dijkstra(5,None, None))
    dist, prev = g.dijkstra(5,None,8)
    self.assertEqual(dist[8],2)
    self.assertEqual(prev[8],1)
    dist2, prev2 = g.dijkstra(1,1,7)
    #print(dist2)
    #print(prev2)
    self.assertEqual(dist2[7],2)
    self.assertEqual(prev2[7],5)
    dist3, prev3 = g.dijkstra(8,-1,2)
    #print(dist3)
    #print(prev3)
    self.assertEqual(dist3[2],3)
    self.assertEqual(prev3[2],4)

  
  def test_shortest_path(self):
    n0 = node(0,'a',[],[3])
    n1 = node(1,'b',[],[4,5,8])
    n2 = node(2,'c',[],[4])
    n3 = node(3,'d',[0],[5,6,7])
    n4 = node(4,'e',[1,2],[6])
    n5 = node(5,'f',[1,3],[7])
    n6 = node(6,'g',[3,4],[8,9])
    n7 = node(7,'h',[3,5],[])
    n8 = node(8,'i',[1,6],[])
    n9 = node(9,'j',[6],[])
    g = open_digraph([0,2],[7],[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])
    #print(g.shortest_path(5,8))
    chemin = g.shortest_path(5,8)
    self.assertEqual(chemin, [5,1,8])
  

  def test_dist_ancestors(self):
    n0 = node(0,'a',[],[3])
    n1 = node(1,'b',[],[4,5,8])
    n2 = node(2,'c',[],[4])
    n3 = node(3,'d',[0],[5,6,7])
    n4 = node(4,'e',[1,2],[6])
    n5 = node(5,'f',[1,3],[7])
    n6 = node(6,'g',[3,4],[8,9])
    n7 = node(7,'h',[3,5],[])
    n8 = node(8,'i',[1,6],[])
    n9 = node(9,'j',[6],[])
    g = open_digraph([0,2],[7],[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])
    dist = g.dist_ancestors(5,8)
    self.assertEqual(dist[1],(1,1))
    self.assertEqual(dist[0],(2,3))
    self.assertEqual(dist[3],(1,2))
  
  
  def test_topological_sorting(self):
    n0 = node(0,'a',[],[3])
    n1 = node(1,'b',[],[4,5,8])
    n2 = node(2,'c',[],[4])
    n3 = node(3,'d',[0],[5,6,7])
    n4 = node(4,'e',[1,2],[6])
    n5 = node(5,'f',[1,3],[7])
    n6 = node(6,'g',[3,4],[8,9])
    n7 = node(7,'h',[3,5],[])
    n8 = node(8,'i',[1,6],[])
    n9 = node(9,'j',[6],[])
    g = open_digraph([0,2],[7],[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])
    liste = g.topological_sorting()
    #print(liste)
    self.assertEqual(liste[0],[0,1,2])
    self.assertEqual(liste[1],[3,4])
    self.assertEqual(liste[2],[5,6])
    self.assertEqual(liste[3],[7,8,9])

  def test_depth_node(self):
    n0 = node(0,'a',[],[3])
    n1 = node(1,'b',[],[4,5,8])
    n2 = node(2,'c',[],[4])
    n3 = node(3,'d',[0],[5,6,7])
    n4 = node(4,'e',[1,2],[6])
    n5 = node(5,'f',[1,3],[7])
    n6 = node(6,'g',[3,4],[8,9])
    n7 = node(7,'h',[3,5],[])
    n8 = node(8,'i',[1,6],[])
    n9 = node(9,'j',[6],[])
    g = open_digraph([0,2],[7],[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])
    #print(g.depth_node(3))
    self.assertEqual(g.depth_node(3),1)
    self.assertEqual(g.depth_node(1),0)
    self.assertEqual(g.depth_node(5),2)
    self.assertEqual(g.depth_node(9),3)
  
  def test_depth_graph(self):
    n0 = node(0,'a',[],[3])
    n1 = node(1,'b',[],[4,5,8])
    n2 = node(2,'c',[],[4])
    n3 = node(3,'d',[0],[5,6,7])
    n4 = node(4,'e',[1,2],[6])
    n5 = node(5,'f',[1,3],[7])
    n6 = node(6,'g',[3,4],[8,9])
    n7 = node(7,'h',[3,5],[])
    n8 = node(8,'i',[1,6],[])
    n9 = node(9,'j',[6],[])
    g = open_digraph([0,2],[7],[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])
    depth = g.depth_graph()
    #print(depth)
    self.assertEqual(depth, 4)
  
  
  def test_longuest_path(self):
    n0 = node(0,'a',[],[3])
    n1 = node(1,'b',[],[4,5,8])
    n2 = node(2,'c',[],[4])
    n3 = node(3,'d',[0],[5,6,7])
    n4 = node(4,'e',[1,2],[6])
    n5 = node(5,'f',[1,3],[7])
    n6 = node(6,'g',[3,4],[8,9])
    n7 = node(7,'h',[3,5],[])
    n8 = node(8,'i',[1,6],[])
    n9 = node(9,'j',[6],[])
    g = open_digraph([0,2],[7],[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9])
    path = g.longuest_path(1,8)
    #print(path)
    self.assertEqual(path, [1,4,6,8])
  
  
  def test_fusion(self):
    n0 = node(0,'a',[],[2,1])
    n1 = node(1,'b',[0,2],[2])
    n2 = node(2,'c',[0,1],[1])
    g = open_digraph([],[1],[n0,n1,n2])
    n3 = node(0,'b',[0,0,2],[2,0,0,2])
    n4 = node(2,'c',[0,0],[0])
    h = open_digraph([],[0],[n3,n4])
    g.fusion(0,1,1)
    #print(g)
    self.assertEqual(g.get_output_ids(),h.get_output_ids())
    self.assertEqual(g.get_input_ids(),h.get_input_ids())
    self.assertEqual(g.get_id_node_map(),h.get_id_node_map())
  
if __name__ == '__main__': # the following code is called only when
  unittest.main()          # precisely this file is run