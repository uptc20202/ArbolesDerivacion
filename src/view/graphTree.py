import networkx as nx
import matplotlib.pyplot as plt

class graphTree:
    
    sequential = 0

def create_graph(root_node):
   
    G = nx.DiGraph()

    node_symbols = {}

    def add_nodes_and_edges(node):
        node_id = node.get_id()
        node_symbol = node.get_symbol().get_symbol()
        node_symbols[node_id] = node_symbol
        G.add_node(node_id, label=node_symbol)

        for child in node.get_children_symbol():
            child_id = child.get_id()
            child_symbol = child.get_symbol().get_symbol()
            node_symbols[child_id] = child_symbol
            G.add_node(child_id, label=child_symbol)
            G.add_edge(node_id, child_id)

            add_nodes_and_edges(child)

    add_nodes_and_edges(root_node)

    pos = nx.spring_layout(G,seed=5000)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
    plt.show()


def plot_graph(root_node):
    G = nx.DiGraph()

    def add_node_to_graph(node):
        G.add_node(node.symbol)

        if node.left:
            G.add_edge(node.symbol, node.left.symbol)
            add_node_to_graph(node.left)

        if node.right:
            G.add_edge(node.symbol, node.right.symbol)
            add_node_to_graph(node.right)

    add_node_to_graph(root_node)

    pos = nx.spring_layout(G, seed=5000)
    labels = {node: node for node in G.nodes()}
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
    plt.title("Grafo del Árbol")
    plt.show()
