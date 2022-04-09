import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.bool_circ import *

class InitTest(unittest.TestCase):  
  def test_init_bool_circ(self):
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    g0 = open_digraph([n0.id],[n1.id],[n0,n1])
    c0 = bool_circ(g0)
    self.assertEqual(c0.inputs,[n0.id])
    self.assertEqual(c0.outputs,[n1.id])
    self.assertEqual(c0.nodes,{0:n0,1:n1})
    self.assertIsInstance(c0,open_digraph)

class BoolCircTest(unittest.TestCase):
  def setUp(self):
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    n2 = node(2,'c',[],[])
    n3 = node(3,'d',[],[])
    g0 = open_digraph([],[],[])
    g1 = open_digraph([0],[1],[n0,n1])
    g2 = open_digraph([0],[2],[n0,n1,n2])
    g3 = open_digraph([0],[3],[n0,n1,n2,n3])
    self.c0 = bool_circ(g0)
    self.c1 = bool_circ(g1)
    self.c2 = bool_circ(g2)
    self.c3 = bool_circ(g3)

  def test_is_well_formed_circ(self):
    n0 = node(0,'a',[],[1,2])
    n1 = node(1,' ',[0],[3,4])
    n2 = node(2,'b',[0],[])
    n3 = node(3,'c',[1],[])
    n4 = node(4,'d',[1],[])
    g3 = open_digraph([],[],[n0,n1,n2,n3,n4])
    c3 = bool_circ(g3)
    self.assertEqual(c3.is_well_formed_circ(),True)

    n0b = node(0,'&',[],[1,2])
    g4 = open_digraph([],[],[n0b,n1,n2,n3,n4])
    #c4 = bool_circ(g4)

  def test_convert_circ_digraph(self):
    n0 = node(0,'a',[],[1])
    n1 = node(1,'b',[0],[])
    n2 = node(2,'c',[],[])
    g0 = self.c0.convert_circ_digraph()
    g1 = self.c2.convert_circ_digraph()
    self.assertEqual(g0.inputs,[])
    self.assertEqual(g0.outputs,[])
    self.assertEqual(g0.nodes,{})
    self.assertIsInstance(g0,open_digraph)
    self.assertEqual(g1.inputs,[0])
    self.assertEqual(g1.outputs,[2])
    self.assertEqual(g1.nodes,{0:n0,1:n1,2:n2})
    self.assertIsInstance(g1,open_digraph)
  
  
  def test_parse_parentheses(self):
    c,dico = bool_circ.parse_parentheses("((x0)&((x1)&(x2)))|((x1)&(~(x2)))","((x0)&(~(x1)))|(x2)")
    #print(c)
    #print(dico)
    self.assertEqual(len(c.get_output_ids()),2)
    self.assertEqual(len(c.get_input_ids()),3)
    c1,dico1 = bool_circ.parse_parentheses("((x0)&(x1))")
    #print(c1)
    #print(dico1)
    self.assertEqual(len(c1.get_input_ids()),2)
    self.assertEqual(len(c1.get_output_ids()),1)
  
  '''
  def test_random_bool_circ(self):
    #g = bool_circ.random_bool_circ(4,2)
    g = bool_circ.random_bool_circ(4,2,2,3)
    #g = bool_circ.random_bool_circ(4,1,2,3)
    #print(g)
    for i in (g.get_node_ids()):
      #on vérifie les changements de label
      if ((g.get_node_by_id(i).indegree() == 1) and (g.get_node_by_id(i).outdegree() == 1)):
        self.assertIn(g.get_node_by_id(i).get_label(), [' ','~'])
      #changement de label et vérifie la séparation des noeuds
      if (g.get_node_by_id(i).indegree() > 1):
        #vérifie l'ajoût aux outputs
        if (g.get_node_by_id(i).outdegree() == 0):
          self.assertIn(i,g.get_output_ids())
        else :
          self.assertIn(g.get_node_by_id(i).get_label(), ['&','|'])
          self.assertEqual(len(g.get_node_by_id(i).get_children_ids()),1)
      if (g.get_node_by_id(i).outdegree() > 1):
        #vérifie l'ajoût aux inputs
        if (g.get_node_by_id(i).indegree()==0):
          self.assertIn(i,g.get_input_ids())
        else : 
          self.assertEqual(len(g.get_node_by_id(i).get_parent_ids()),1)
    
    self.assertEqual(len(g.get_input_ids()),2)
    self.assertEqual(len(g.get_output_ids()),3)
  '''

  def test_binaire(self):
    g = bool_circ.binaire(11,8)
    #print(g)
    self.assertEqual(len(g.get_nodes()),8)
    self.assertEqual(len(g.get_output_ids()),8)
    for i in (g.get_nodes()):
      self.assertIn(i.get_label(),['0','1'])