import networkx as nx
from networkx.algorithms.flow import edmonds_karp
import matplotlib.pyplot as plt

def draw_graph(graph):
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

#Algorithm Dijkstra
def algorithm_dijkstra(graph):
    graph.add_edges_from([ [1,5,{'weight':4}], [1,7,{'weight':1}], [5,7,{'weight':2}], [2,5,{'weight':2}], [5,6,{'weight':7}], [5,8,{'weight':2}], [2,6,{'weight':8}], [6,8,{'weight':1}], [6,4,{'weight':1}], [4,8,{'weight':3}], [3,8,{'weight':9}], [7,8,{'weight':8}], [3,7,{'weight':3}],])
    result = nx.dijkstra_path(graph, 7, 6)
    print(result)
    return graph

#Algorithm Ford-Fulkerson
def algorithm_ford_fulkerson(graph):
    graph.add_edges_from([ [1,2,{'capacity':1}], [3,1,{'capacity':2}], [1,9,{'capacity':8}], [1,10,{'capacity':5}], [2,4,{'capacity':4}], [2,3,{'capacity':3}], [4,3,{'capacity':6}], [4,14,{'capacity':4}], [4,5,{'capacity':5}], [5,14,{'capacity':3}], [5,7,{'capacity':1}], [5,6,{'capacity':8}], [14,7,{'capacity':2}], [6,8,{'capacity':3}], [3,6,{'capacity':7}], [6,9,{'capacity':7}], [7,15,{'capacity':6}], [8,15,{'capacity':4}], [8,13,{'capacity':3}], [8,11,{'capacity':9}], [9,13,{'capacity':8}], [9,10,{'capacity':4}], [10,11,{'capacity':3}], [11,12,{'capacity':6}], [12,13,{'capacity':5}], [12,15,{'capacity':1}], [13,15,{'capacity':2}],])    result = edmonds_karp(graph, 's', 't')
    print(result.graph['flow_value'])
    return graph

#Algorithm Maximum flow
def algorithm_maximum_flow(graph):
    graph.add_edges_from([ ['s','a',{'capacity':4.0}], ['s','c',{'capacity':3.0}], ['a','b',{'capacity':4.0}], ['b','c',{'capacity':3.0}], ['c','d',{'capacity':6.0}], ['b','t',{'capacity':2.0}], ['d','t',{'capacity':6.0}], ])
    flow_value, flow_dict = nx.maximum_flow(graph, 's', 't')
    print(flow_value)
    print(flow_dict)
    return graph

graph = nx.Graph()

print('Network algorithm:\n[1] Algorithm Dijkstra;\n[2] Algorithm Ford-Fulkerson;\n[3] Algorithm Maximum flow;\n\n')
command = input('Enter number of algorithm: ')

if command == '1': algorithm_dijkstra(graph)
elif command == '2': algorithm_ford_fulkerson(graph)
elif command == '3': algorithm_maximum_flow(graph)
else: print('Unknown command!')

draw_graph(graph)
