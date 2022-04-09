from modules.open_digraph import *
from modules.utils import *
import inspect 
import test

#n0 = node(0,'a',[],[1])
#n1 = node(1,'b',[0],[])
#n2 = node(2,'c',[],[])
#n3 = node(3,'d',[],[])
#g0 = open_digraph([],[],[])
#g1 = open_digraph([0],[1],[n0,n1])
#g2 = open_digraph([0],[2],[n0,n1,n2])
#g3 = open_digraph([0],[3],[n0,n2,n3])

n0 = node(0,'a',[1,0,3],[0,3])
n1 = node(1,'b',[],[0,3])
n3 = node(3,'c',[1,0],[0])
g = open_digraph([0,2],[1,2,2],[n0,n1,n3])


'''
print("methods of the class node :\n ", dir(node),"\n")
print("methods of the class open_digraph :\n", dir(open_digraph),"\n")
print("source code of the method add_edge in open_digraph: \n",inspect.getsource(open_digraph.add_edge),"\n")
print("doc of the method add_edge in open_digraph:\n",inspect.getdoc(open_digraph.add_edge),"\n")
print("file where the add_edge method is located:\n",inspect.getfile(open_digraph.add_edge),"\n")

print(g3.add_input_id(4))
print(g3.get_node_ids())
print(random_int_list(10,100),"\n")

print_matrix(random_matrix(4,5,null_diag=True))
print_matrix(random_matrix(4,5,symetric=True))
print_matrix(random_matrix(4,5,oriented=True))
print_matrix(random_matrix(4,5,triangular=True))
print_matrix(random_matrix(2,1))
print(open_digraph.graph_from_adjency_matrix(random_matrix(2,1)))
'''

'''
QUESTIONS :
NORMALIZE (3,2) (2,3) PAS POSSIBLE ?
'''
'''
s = "((x0)&((x1)&(x2)))|((x1)&(~(x2)))"
g = bool_circ.parse_parentheses(s)
print(g)
'''


