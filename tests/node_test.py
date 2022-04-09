import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.node import *

class InitTest(unittest.TestCase):  

  def test_init_node(self):
    '''__init__node'''
    n0 = node(0, 'i', [], [1])
    self.assertEqual(n0.id, 0)
    self.assertEqual(n0.label, 'i')
    self.assertEqual(n0.parents, [])
    self.assertEqual(n0.children, [1])
    self.assertIsInstance(n0, node)

class NodeTest(unittest.TestCase):
  def setUp(self):
    '''setUp node'''
    self.n0 = node(0, 'a', [], [1])
    self.n1 = node(1, 'b', [0], [])
    self.n2 = node(2,'c',[0,1,0],[0,1,1])

  def test_copy(self):
    '''copy()'''
    n2 = self.n0.copy()
    n2.label = 'c'
    self.assertEqual(n2.id, self.n0.id)
    self.assertEqual(n2.parents, self.n0.parents)
    self.assertEqual(n2.children, self.n0.children)
    self.assertNotEqual(n2.label, self.n0.label)
    self.assertIsNot(n2, self.n0)

  def test__eq__(self):
    '''__eq__()'''
    self.assertEqual(self.n0 == self.n1, 0)
    self.assertEqual(self.n0 == self.n0, 1)
    #self.assertEqual(self.n0 == 1,None)

  def test_get_id(self):
    '''get_id()'''
    self.assertEqual(self.n0.get_id(), 0)
    self.assertEqual(self.n1.get_id(), 1)

  def test_get_label(self):
    '''get_label()'''
    self.assertEqual(self.n0.get_label(), 'a')
    self.assertEqual(self.n1.get_label(), 'b')

  def test_get_parent_ids(self):
    '''get_parent_ids()'''
    self.assertEqual(self.n0.get_parent_ids(), [])
    self.assertEqual(self.n1.get_parent_ids(), [0])

  def test_get_children_ids(self):
    '''get_children_ids()'''
    self.assertEqual(self.n0.get_children_ids(), [1])
    self.assertEqual(self.n1.get_children_ids(), [])

  def test_set_id(self):
    '''set_id()'''
    self.n0.set_id(1)
    self.assertEqual(self.n0.get_id(), 1)
    #self.assertEqual(self.n1.set_id('a'),None)

  def test_set_label(self):
    '''set_label()'''
    self.n0.set_label('c')
    self.assertEqual(self.n0.get_label(), 'c')
    #self.assertEqual(self.n2.set_label(True),None)

  def test_set_parent_ids(self):
    '''set_parent_ids()'''
    self.n0.set_parent_ids([0,1,2])
    self.assertEqual(self.n0.get_parent_ids(), [0,1,2])
    #self.assertEqual(self.n1.set_parent_ids([0,-1,'a']),None)

  def test_set_children_ids(self):
    '''set_children_ids()'''
    '''
    self.assertEqual(self.n0.set_children_ids(['b',0,-2]),None)
    self.n1.set_children_ids([1,2,0])
    self.assertEqual(self.n1.get_children_ids(),[1,2,0])
    '''
    self.n0.set_children_ids(['b',0,-2])

  def test_add_child_id(self):
    '''add_child_id()'''
    self.n0.add_child_id(2)
    self.assertEqual(self.n0.get_children_ids(), [1,2])

  def test_add_parent_id(self):
    '''add_parent_id'''
    self.n0.add_parent_id(3)
    self.assertEqual(self.n0.get_parent_ids(), [3])

  def test_remove_parent_id(self):
    '''remove_parent_id'''
    self.n2.remove_parent_id(0)
    self.assertEqual(self.n2.get_parent_ids(), [1,0])
    self.n2.remove_parent_id(2)
    self.assertEqual(self.n2.get_parent_ids(), [1,0])

  def test_remove_child_id(self):
    '''remove_child_id'''
    self.n2.remove_child_id(1)
    self.assertEqual(self.n2.get_children_ids(), [0,1])
    self.n2.remove_child_id(22)
    self.assertEqual(self.n2.get_children_ids(), [0,1])

  def test_remove_parent_id_all(self):
    '''remove_parent_id_all'''
    self.n2.remove_parent_id_all(0)
    self.assertEqual(self.n2.get_parent_ids(), [1])
    self.n2.remove_parent_id_all(8)
    self.assertEqual(self.n2.get_parent_ids(), [1])

  def test_remove_child_id_all(self):
    '''remove_child_id_all'''
    self.n2.remove_child_id_all(1)
    self.assertEqual(self.n2.get_children_ids(), [0])
    self.n2.remove_child_id_all(3)
    self.assertEqual(self.n2.get_children_ids(), [0])

  def test_indegree(self):
    '''indegree()'''
    self.assertEqual(self.n0.indegree(),0)
    self.assertEqual(self.n1.indegree(),1)
    self.assertEqual(self.n2.indegree(),3)
  
  def test_outdegree(self):
    '''outdegree()'''
    self.assertEqual(self.n0.outdegree(),1)
    self.assertEqual(self.n1.outdegree(),0)
    self.assertEqual(self.n2.outdegree(),3)
  
  def test_degree(self):
    '''degree()'''
    self.assertEqual(self.n0.degree(),1)
    self.assertEqual(self.n1.degree(),1)
    self.assertEqual(self.n2.degree(),6)
  
  def test_shift_indices_nodes(self):
    '''shift_indices_nodes()'''
    n = 2
    self.n0.shift_indices_nodes(n)
    self.n2.shift_indices_nodes(n)
    self.assertEqual(self.n0.get_id(),2)
    self.assertEqual(self.n2.get_id(),4)
    self.assertEqual(self.n2.get_parent_ids(),[2,3,2])
    self.assertEqual(self.n2.get_children_ids(),[2,3,3])