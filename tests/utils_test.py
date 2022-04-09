import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.open_digraph import *

class InitTest(unittest.TestCase):
  def test_remove_all(self):
    l = [2,2,0,1,-2,2]
    self.assertEqual(remove_all(l,2),[0,1,-2])

  def test_count_occurences(self):
    l1 = [0,0,2,1,0,1]
    l2=[]
    self.assertEqual(2, count_occurrences(l1,1))
    self.assertEqual(3, count_occurrences(l1,0))
    self.assertEqual(0, count_occurrences(l2,4))

  def test_random_matrix(self):
    '''random'''
    M0 = random_matrix(3, 10, True)
    self.assertEqual(M0[0][0], 0)
    self.assertEqual(M0[1][1], 0)
    self.assertEqual(M0[2][2], 0)

    '''symetric'''
    M1 = random_matrix(4, 10,True,form="symetric")
    self.assertEqual(M1[0][1],M1[1][0])
    self.assertEqual(M1[0][2],M1[2][0])
    self.assertEqual(M1[0][3],M1[3][0])
    self.assertEqual(M1[1][2],M1[2][1])
    self.assertEqual(M1[1][3],M1[3][1])
    self.assertEqual(M1[2][3],M1[3][2])
