from __future__ import division
from person import *
from pylab import *
import random as rnd
import networkx as nx

def build_adjacency(data):
    adj_dict = dict()
    for node in data:
        a = node[0]
        b = node[1]
        if a in adj_dict:
            adj_dict[a].append(b)
        else:
            adj_dict[a] = [b]
        if b in adj_dict:
            adj_dict[b].append(a)
        else:
            adj_dict[b] = [a]
    return adj_dict

rcParams['figure.figsize'] = 12, 12 
def draw_graph(graph, labels=None,node_size=1600, node_color='blue', node_alpha=0.3,node_text_size=12,
edge_color='blue', edge_alpha=0.3, edge_tickness=1,edge_text_pos=0.3,text_font='sans-serif'):
    G=nx.Graph()
    for edge in graph:
        G.add_edge(edge[0], edge[1])
    graph_pos=nx.shell_layout(G)
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size,alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,font_family=text_font)
    plt.show()
    plt.savefig(r'C:\Users\calri\Documents\data_prep\Social_Network\friends.png',dpi=200)

if __name__ == '__main__' :
    net = network()
    p1 = person("Anita", "Racinez",net)
    p2 = person("Clem", "Jameson",net)
    p3 = person("Lars", "Eriksson",net)
    p4 = person("Jed", "Jones",net)
    data = [(p1.first_name, p2.first_name), (p2.first_name, p3.first_name), (p1.first_name, p4.first_name), (p2.first_name, p4.first_name)]
    draw_graph(data)