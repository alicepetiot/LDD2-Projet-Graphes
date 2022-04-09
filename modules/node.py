import sys
sys.path.append('../') # allows us to fetch files from the project root

from modules.utils import *

class node:
  def __init__(self, identity, label, parents, children):
    '''
    identity: int; its unique id in the graph
    label: string;
    parents: int list; a sorted list containing the ids of its parents
    children: int list; a sorted list containing the ids of its children
    '''
    self.id = identity
    self.label = label
    self.parents = parents
    self.children = children

  def __str__(self):
    '''
    output string :
    returns the string to be displayed by print
    '''
    return ("("+str(self.id)+","+self.label+","+str(self.parents)
            +","+str(self.children)+")")

  def __repr__(self):
    '''
    output : string
    returns the string to be displayed by print
    '''
    return str(self)

  def __eq__(self,node2):
    '''
    output : booleen
    returns true if the two nodes are equals else false
    '''
    if isinstance(node2,node):
      if self.id == node2.id and self.label == node2.label and self.parents == node2.parents and self.children == node2.children:
        return 1;
      return 0;
    else:
      print("### Oops! You can't compare apples with oranges : "+" node != "+str(type(node2))+" in __eq__() ###")

  def copy(self):
    '''
    output : node
    returns a copy of the node
    '''
    return node(self.id, self.label, self.parents.copy(), self.children.copy())

  def get_id(self):
    '''
    output : int
    returns the id of the node
    '''
    return self.id 

  def get_label(self):
    '''
    output : int
    returns the label of the node
    '''
    return self.label

  def get_parent_ids(self):
    '''
    output : int list
    returns the ids of the parents
    '''
    return self.parents

  def get_children_ids(self):
    '''
    output : int list
    returns the ids of the childrens
    '''
    return self.children

  def set_id(self, i):
    '''
    changes the id of the node
    '''
    if isinstance(i,int):
      self.id = i
    else:
      print("### You can't compare apples with oranges : "+" int != "+str(type(i))+" in set_id() ###")

  def set_label(self, l):
    '''
    changes the label of the node
    '''
    if isinstance(l,str):
      self.label = l
    else:
      print("### You can't compare apples with oranges : "+" str != "+str(type(l))+" in set_label() ###")

  def set_parent_ids(self, p):
    '''
    changes the entire parent ids list of the node
    '''
    intL = all(isinstance(x,int) for x in p)
    posL = all(x>=0 for x in p)
    if intL and posL:
      self.parents = p
    if not posL:
      print("### not positive list in set_parent_ids() ###")
    if not intL:
      print("### not int list in set_parent_ids() ###")
  
  def set_children_ids(self, c):
    '''
    changes the entire children ids list of the node
    '''
    ''''
    intL = all(isinstance(x,int) for x in c)
    posL = all(x>=0 for x in c)
    if intL and posL:
    '''
    self.children = c
    '''
    if not posL:
      print("### not positive list in set_children_ids() ###")
    if not intL:
      print("### not int list in set_children_ids() ###")
    '''

  def add_child_id(self, child_id):
    '''
    adds a children id to the children list of the node
    '''
    self.children.append(child_id)

  def add_parent_id(self, parent_id):
    '''
    adds a parent id to the parent list of the node
    '''
    self.parents.append(parent_id)

  def remove_parent_id(self, parent_id):
    '''
    removes one occurrence of parent_id in the list of parents of the node
    '''
    if parent_id in self.get_parent_ids():
      self.get_parent_ids().remove(parent_id)

  def remove_child_id(self, child_id):
    '''
    removes one occurrence of child_id in the list of children of the node
    '''
    if child_id in self.get_children_ids():
      self.get_children_ids().remove(child_id)
    
  def remove_parent_id_all(self, parent_id):
    '''
    removes all occurrences of parent_id in the list of parents of the node
    '''
    remove_all(self.get_parent_ids(), parent_id)

  def remove_child_id_all(self, child_id):
    '''
    removes all occurrences of child_id in the list of children of the node
    '''
    remove_all(self.get_children_ids(), child_id)
  
  def indegree(self):
    '''
    output : int
    returns the in degree 
    '''
    return len(self.get_parent_ids())
  
  def outdegree(self):
    '''
    output : int
    returns the out degree 
    '''
    return len(self.get_children_ids())

  def degree(self):
    '''
    output : int
    returns the total degree 
    '''
    return (self.indegree() + self.outdegree())
  
  def shift_indices_nodes(self,n):
    '''
    increase of nall the index 
    '''
    self.set_id(self.get_id()+n)
    if (self.get_parent_ids() !=[]):
      self.set_parent_ids([x+n for x in self.get_parent_ids()])
    if (self.get_children_ids() !=[]):
      self.set_children_ids([x+n for x in self.get_children_ids()])