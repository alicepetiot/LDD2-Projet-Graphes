class tri_topologique_mx:
  def dijkstra(self, src, direction = None, tgt = None):
    '''
    Dijkstra algorithme
    '''
    Q = [src]
    dist = {src:0}
    prev = {}
    while (Q != []):
      u = min(Q, key=lambda x  : dist[x])
      if (u == tgt):
        return dist, prev
      Q.remove(u)
      neighbours =[]
      node = self.get_node_by_id(u)
      if (direction == None):
        for i in (node.get_parent_ids()):
          neighbours.append(self.get_node_by_id(i))
        for i in (node.get_children_ids()):
          neighbours.append(self.get_node_by_id(i))
      if (direction == -1):
        for i in (node.get_parent_ids()):
          neighbours.append(self.get_node_by_id(i))
      if (direction == 1):
        for i in (node.get_children_ids()):
          neighbours.append(self.get_node_by_id(i))
      for v in (neighbours):
        if (v.get_id() not in dist.keys()):
          Q.append(v.get_id())
        if (v.get_id() not in dist.keys() or dist[v.get_id()] > dist[u]+1):
          dist[v.get_id()] = dist[u] + 1
          prev[v.get_id()] = u
    return dist, prev

  def shortest_path(self,u,v,direction = None):
    '''
    output : array
    return the shortest path between u and v
    '''
    dist,prev = self.dijkstra(u, direction, v)
    chemin = [v]
    i=prev[v]
    while (i!=u):
      chemin.append(i)
      i = prev[i]
    chemin.append(u)
    cheminf = list(reversed(chemin))
    return cheminf

  
  def dist_ancestors(self,u,v):
    '''
    output : dictionnary
    return the dictionnary of the common ancestors, with their distance to the both nodes
    '''
    distu, prevu = self.dijkstra(u,-1)
    distv, prevv = self.dijkstra(v,-1)
    common = {}
    for i in (prevu):
      if (i in prevv):
          common[i] = (distu[i],distv[i])
    return common

   
  def topological_sorting(self): 
    '''
    output: double list
    return a topological sorting of the graph
    '''
    g = self.copy()
    if (g.is_cyclic()):
      raise TypeError('The graph is cyclic')
    i = 0
    res = []
    while (g.get_node_ids() != []):
      res.append([])
      for j in (g.get_node_ids()):
        if(g.get_node_by_id(j).get_parent_ids() == []):
          res[i].append(j)
      g.remove_nodes_by_id(res[i])
      i = i+1
    return res

  def depth_node(self, node):
    '''
    return the depth of the node
    '''
    liste = self.topological_sorting()
    for i in range (len(liste)):
      if (node in liste[i]):
        return i
  
  def depth_graph(self):
    '''
    return the depth of the graph
    '''
    liste = self.topological_sorting()
    return len(liste)
  
  def longuest_path(self, u, v):
    '''
    return the longuest path between the node u and v
    '''
    liste = self.topological_sorting()
    dist = {u:0}
    prev = {}
    #récupère l'indice de la couche de u
    for i in range (len(liste)):
      if (u in liste[i]):
        rg_u = i
    #parcours les noeuds depuis la couche supérieure à celle de u
    for j in range(rg_u+1,len(liste)):
      #parcours les noeuds de la couche
      for h in (liste[j]):
        #rempli les distances ainsi que les précédents
        parents = self.get_node_by_id(h).get_parent_ids()
        maxi = max(parents, key = lambda x: dist.get(x,-1), default = None)
        if (maxi in dist):
            dist[h]= dist[maxi]+1
            prev[h]= maxi
        #construit le chemin lorsqu'on arrive à v
        if (h == v):
          path=[v]
          chemin=prev[v]
          while(chemin!=u):
            path.append(chemin)
            chemin = prev[chemin]
          path.append(u)
          pathf = list(reversed(path))
          return pathf

  
  def fusion(self, u, v, label = None):
    '''
    merge the node u with the node v in the graph
    if label = 1 : keep the label of the node v
    '''
    #choisi le label pour le noeud
    if (label == 1):
      l = self.get_node_by_id(v).get_label()
      self.get_node_by_id(u).set_label(l)
    #récupère les parents et enfants de v
    parents = self.get_node_by_id(v).get_parent_ids()
    children = self.get_node_by_id(v).get_children_ids()
    # remplace les occurences de v par u 
    parents = [i if i!=v else u for i in parents]
    children = [i if i!=v else u for i in children]
    #remplace les potentielles occurences de v dans parents et enfants de u par u
    for i in range (len(self.get_node_by_id(u).get_parent_ids())):
      if(i == v):
        self.get_node_by_id(u).get_parent_ids()[i] = u
        self.get_node_by_id(u).add_child_id(u)
    for j in range (len(self.get_node_by_id(u).get_children_ids())):
      if(j == v):
        self.get_node_by_id(u).get_children_ids()[j] = u
        self.get_node_by_id(u).add_parent_id(u)
    #ajoute la liste des enfants ainsi que des parents de v à u
    for h in (parents):
        self.get_node_by_id(u).add_parent_id(h)
        self.get_node_by_id(h).add_child_id(u)
    for k in (children):
        self.get_node_by_id(u).add_child_id(k)
        self.get_node_by_id(k).add_parent_id(u)
    #gère les inputs et les outputs
    for i in range (len(self.get_output_ids())):
      if (self.get_output_ids()[i]==v):
        self.get_output_ids()[i]=u
    for i in range (len(self.get_input_ids())):
      if (self.get_input_ids()[i]==v):
        self.get_input_ids()[i]=u
    #retire le noeud v
    self.remove_node_by_id(v)