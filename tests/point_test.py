import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.point import *

class InitTest(unittest.TestCase):

  def test_init_node(self):
    p0 = point(0,0)
    self.assertEqual(p0.x,0)
    self.assertEqual(p0.y,0)
    self.assertIsInstance(p0,point)

class PointTest(unittest.TestCase):

  def setUp(self):
    self.p0 = point(0,0)
    self.p1 = point(125,100)
    self.p2 = point(-100,25)
    self.p3 = point(-300,-200)
    self.p4 = point(100,-400)

  def test_copy(self):
    p = self.p0.copy() 
    p.x = 100 
    self.assertEqual(self.p0.x,0)
    self.assertEqual(self.p0.y,0)
    self.assertEqual(p.x,100)
    self.assertEqual(p.y,0)
  
  def test__eq__(self):
    self.assertEqual(self.p0.__eq__((0,0)),True)
    self.assertEqual(self.p0.__eq__(point(0,0)),True)
    self.assertEqual(self.p0.__eq__(self.p1),False)
    self.assertEqual(self.p0.__eq__((-100,0)),False)
    self.assertEqual(self.p0.__eq__(0),None)
  
  def test__str__(self):
    self.assertEqual(self.p0.__str__(),'(0,0)')
    self.assertEqual(self.p1.__str__(),'(125,100)')
    self.assertEqual(self.p2.__str__(),'(-100,25)')
    self.assertEqual(self.p3.__str__(),'(-300,-200)')
    self.assertEqual(self.p4.__str__(),'(100,-400)')

  def test_get_x(self):
    self.assertEqual(self.p0.get_x(),0)
    self.assertEqual(self.p1.get_x(),125)
    self.assertEqual(self.p2.get_x(),-100)
    self.assertEqual(self.p3.get_x(),-300)
    self.assertEqual(self.p4.get_x(),100)
    
  def test_get_y(self):
    self.assertEqual(self.p0.get_y(),0)
    self.assertEqual(self.p1.get_y(),100)
    self.assertEqual(self.p2.get_y(),25)
    self.assertEqual(self.p3.get_y(),-200)
    self.assertEqual(self.p4.get_y(),-400)

  def test_set_x(self):
    self.p0.set_x(-100)
    self.p1.set_x(125.25)
    self.assertEqual(self.p0.get_x(),-100)
    self.assertEqual(self.p1.get_x(),125.25)
    self.assertEqual(self.p2.set_x('a'),None)
    
  def test_set_y(self):
    self.p1.set_y(-100)
    self.p2.set_y(0.75)
    self.assertEqual(self.p0.set_y(True),None)
    self.assertEqual(self.p1.get_y(),-100)
    self.assertEqual(self.p2.get_y(),0.75)

  def test__add__(self):
    self.assertEqual(self.p0+self.p1,self.p1)
    self.assertEqual(self.p2+self.p1,point(25,125))
    self.assertEqual(self.p3+self.p4,point(-200,-600))
    self.assertEqual(self.p4+(-100,25.5),point(0,-374.5))
    self.assertEqual(self.p1+False,None)

  def test__rmul__(self):
    self.assertEqual(self.p0.__rmul__(0.0),point(0.0,0.0))
    self.assertEqual(self.p2.__rmul__(4),point(-400,100))
    self.assertEqual(self.p3.__rmul__(-2.5),point(750,500))
    self.assertEqual(self.p4.__rmul__('a'),None)

  def test__sub__(self):
    self.assertEqual(self.p0-self.p1,self.p1.__rmul__(-1))
    self.assertEqual(self.p1-self.p4,point(25,500))
    self.assertEqual(self.p4-self.p1,point(-25,-500))
    self.assertEqual(self.p3-(-100,600),point(-200,-800))
    self.assertEqual(self.p2-'troll',None)

