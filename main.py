import networkx as nx
graph=nx.Graph()
graph.add_edges_from([ [1,2,{'weight':7}], [1,3,{'weight':9}], [1,6,{'weight':14}], [2,3,{'weight':10}], [2,4,{'weight':15}], [3,4,{'weight':11}], [3,6,{'weight':2}], [4,5,{'weight':6}], [5,6,{'weight':9}] ])
result = nx.dijkstra_path(graph,1,5)
print(result)
