import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.show()

#Algorithm Dijkstra
def algorithm_dijkstra(graph):
    graph.add_edge('1','5', weight=4)
    graph.add_edge('1','7', weight=1)
    graph.add_edge('5','7', weight=2)
    graph.add_edge('2','5', weight=2)
    graph.add_edge('5','6', weight=7)
    graph.add_edge('5','8', weight=2)
    graph.add_edge('2','6', weight=8)
    graph.add_edge('6','8', weight=1)
    graph.add_edge('6','4', weight=1)
    graph.add_edge('4','8', weight=3)
    graph.add_edge('3','8', weight=9)
    graph.add_edge('7','8', weight=8)
    graph.add_edge('3','7', weight=3)
    result = nx.dijkstra_path(graph, '6', '7')
    print(result)
    draw_graph(graph)

#Algorithm Ford-Bellman
def algorithm_ford_bellman(graph):
    graph.add_edge('1','2', weight=1)
    graph.add_edge('1','3', weight=2)
    graph.add_edge('1','9', weight=8)
    graph.add_edge('1','10', weight=5)
    graph.add_edge('2','4', weight=4)
    graph.add_edge('2','3', weight=3)
    graph.add_edge('3','4', weight=6)
    graph.add_edge('4','14', weight=4)
    graph.add_edge('4','5', weight=5)
    graph.add_edge('5','14', weight=3)
    graph.add_edge('5','7', weight=1)
    graph.add_edge('5','6', weight=8)
    graph.add_edge('7','14', weight=2)
    graph.add_edge('6','8', weight=3)
    graph.add_edge('6','3', weight=7)
    graph.add_edge('6','9', weight=7)
    graph.add_edge('7','15', weight=6)
    graph.add_edge('8','15', weight=4)
    graph.add_edge('8','13', weight=3)
    graph.add_edge('8','11', weight=9)
    graph.add_edge('9','13', weight=8)
    graph.add_edge('9','10', weight=4)
    graph.add_edge('10','11', weight=3)
    graph.add_edge('11','12', weight=6)
    graph.add_edge('12','13', weight=5)
    graph.add_edge('12','15', weight=1)
    graph.add_edge('13','15', weight=2)
    result = nx.bellman_ford(graph, '12')
    print(result)
    draw_graph(graph)

#Algorithm Maximum flow
def algorithm_maximum_flow(graph):
    graph.add_edge('s','1', capacity=8)
    graph.add_edge('1','s', capacity=2)
    graph.add_edge('s','2', capacity=11)
    graph.add_edge('2','s', capacity=159)
    graph.add_edge('s','3', capacity=159)
    graph.add_edge('3','s', capacity=20)
    graph.add_edge('s','4', capacity=12)
    graph.add_edge('4','s', capacity=11)
    graph.add_edge('1','2', capacity=2)
    graph.add_edge('2','1', capacity=2)
    graph.add_edge('1','3', capacity=1)
    graph.add_edge('3','1', capacity=15)
    graph.add_edge('1','4', capacity=2)
    graph.add_edge('4','1', capacity=1)
    graph.add_edge('2','3', capacity=7)
    graph.add_edge('3','2', capacity=8)
    graph.add_edge('2','t', capacity=8)
    graph.add_edge('t','2', capacity=11)
    graph.add_edge('3','4', capacity=0)
    graph.add_edge('4','3', capacity=15)
    graph.add_edge('3','t', capacity=99)
    graph.add_edge('t','3', capacity=12)
    graph.add_edge('4','t', capacity=12)
    graph.add_edge('t','4', capacity=2)
    result = nx.maximum_flow_value(graph, 's', 't')
    print(result)
    draw_graph(graph)



if if __name__ == '__main__':
    while(True):
        print('Network algorithm:\n[1] Algorithm Dijkstra;\n[2] Algorithm Ford-Bellman;\n[3] Algorithm Maximum flow;\n\n')
        command = input('Enter number of algorithm: ')
        if command == '1': algorithm_dijkstra(nx.Graph())
        elif command == '2': algorithm_ford_bellman(nx.Graph())
        elif command == '3': algorithm_maximum_flow(nx.DiGraph())
        elif (command == 'q') or (command == 'Q') or (command == 'й') or (command == 'Й'): break
        else: print('Unknown command!')

