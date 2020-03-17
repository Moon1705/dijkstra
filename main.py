import networkx as nx

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
    print(' -> '.join(result))

#Algorithm Ford-Bellman
def algorithm_ford_bellman(graph):
    graph.add_edge(1,2, weight=1)
    graph.add_edge(1,3, weight=2)
    graph.add_edge(1,9, weight=8)
    graph.add_edge(1,10, weight=5)
    graph.add_edge(2,4, weight=4)
    graph.add_edge(2,3, weight=3)
    graph.add_edge(3,4, weight=6)
    graph.add_edge(4,14, weight=4)
    graph.add_edge(4,5, weight=5)
    graph.add_edge(5,14, weight=3)
    graph.add_edge(5,7, weight=1)
    graph.add_edge(5,6, weight=8)
    graph.add_edge(7,14, weight=2)
    graph.add_edge(6,8, weight=3)
    graph.add_edge(6,3, weight=7)
    graph.add_edge(6,9, weight=7)
    graph.add_edge(7,15, weight=6)
    graph.add_edge(8,15, weight=4)
    graph.add_edge(8,13, weight=3)
    graph.add_edge(8,11, weight=9)
    graph.add_edge(9,13, weight=8)
    graph.add_edge(9,10, weight=4)
    graph.add_edge(10,11, weight=3)
    graph.add_edge(11,12, weight=6)
    graph.add_edge(12,13, weight=5)
    graph.add_edge(12,15, weight=1)
    graph.add_edge(13,15, weight=2)
    result = dict(sorted(nx.bellman_ford(graph, 12)[1].items()))
    for k, v in result.items():
        print('Point ' + str(k) + ":\t" + str(v))

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
    print("Max flow: " + str(result))

def reservation_communication_networks():
    R = 0.9997
    q = (0.06, 0.065, 0.04, 0.035)
    C = (900, 6000, 8000, 11000)
    Q = 1 - R
    list_result = []
    for i1 in range(1,5):
        for i2 in range(1,5):
            for i3 in range(1,5):
                for i4 in range(1,5):
                    del_q = pow(q[0],i1) + pow(q[1],i2) + pow(q[2],i3) + pow(q[3],i4)
                    if (del_q < Q):
                        del_C = C[0]*i1+C[1]*i2+C[2]*i3+C[3]*i4
                        list_result.append(((i1,i2,i3,i4), del_C, del_q))
    element_max = 1000000000000000000000
    for element in list_result:
        if element[1] < element_max:
            element_max = element[1]
    for element in list_result:
        if element[1] == element_max:
            print("Pow:\t" + str(element[0]))
            print("C:\t" + str(element[1]))
            print("Q:\t" + str(element[2]))


if __name__ == '__main__':
    while(True):
        print('\n\nNetwork algorithm:\n[1] Algorithm Dijkstra;\n[2] Algorithm Ford-Bellman;\n[3] Algorithm Maximum flow;\n[4] Reservation in communication networks;\n[q or Q] Quit\n\n')
        command = input('Enter number of algorithm: ')
        if command == '1': algorithm_dijkstra(nx.Graph())
        elif command == '2': algorithm_ford_bellman(nx.Graph())
        elif command == '3': algorithm_maximum_flow(nx.DiGraph())
        elif command == '4': reservation_communication_networks()
        elif (command == 'q') or (command == 'Q') or (command == 'й') or (command == 'Й'): break
        else: print('Unknown command!')

