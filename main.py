import networkx as nx
from networkx.algorithms.flow import edmonds_karp
import matplotlib.pyplot as plt

def draw_graph(graph):
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

#Algorithm Dijkstra
def algorithm_dijkstra(graph):
    graph.add_edges_from([ [1,2,{'weight':7}], [1,3,{'weight':9}], [1,6,{'weight':14}], [2,3,{'weight':10}], [2,4,{'weight':15}], [3,4,{'weight':11}], [3,6,{'weight':2}], [4,5,{'weight':6}], [5,6,{'weight':9}], ])
    result = nx.dijkstra_path(graph, 1, 5)
    print(result)
    return graph

#Algorithm Ford-Fulkerson
def algorithm_ford_fulkerson(graph):
    graph.add_edges_from([ ['s','a',{'capacity':4.0}], ['s','c',{'capacity':3.0}], ['a','b',{'capacity':4.0}], ['b','c',{'capacity':3.0}], ['c','d',{'capacity':6.0}], ['b','t',{'capacity':2.0}], ['d','t',{'capacity':6.0}], ])
    result = edmonds_karp(graph, 's', 't')
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
