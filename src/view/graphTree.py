import networkx as nx
import matplotlib.pyplot as plt

class graphTree:
    # ... (tu definición de clase aquí)
    sequential = 0

def create_graph(root_node):
    # Creamos un objeto de grafo dirigido
    G = nx.DiGraph()

    # Creamos un diccionario para realizar un seguimiento de los nodos y sus símbolos
    node_symbols = {}

    # Función recursiva para agregar nodos y bordes al grafo
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

            # Llamada recursiva para procesar los hijos
            add_nodes_and_edges(child)

    # Comenzamos el proceso de agregación desde el nodo raíz
    add_nodes_and_edges(root_node)

    # Dibuja el grafo
    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
    plt.show()


def plot_graph(root_node):
    # Crear un gráfico dirigido (DiGraph) de NetworkX
    G = nx.DiGraph()

    # Función recursiva para agregar nodos y aristas al gráfico
    def add_node_to_graph(node):
        G.add_node(node.symbol)  # Agregar el símbolo del nodo como un nodo en el gráfico

        # Si el nodo tiene un hijo izquierdo, agregar una arista desde el nodo actual al hijo izquierdo
        if node.left:
            G.add_edge(node.symbol, node.left.symbol)
            add_node_to_graph(node.left)

        # Si el nodo tiene un hijo derecho, agregar una arista desde el nodo actual al hijo derecho
        if node.right:
            G.add_edge(node.symbol, node.right.symbol)
            add_node_to_graph(node.right)

    add_node_to_graph(root_node)

    # Dibujar el gráfico utilizando Matplotlib
    pos = nx.spring_layout(G, seed=42)  # Posicionamiento de nodos
    labels = {node: node for node in G.nodes()}  # Etiquetas de nodos
    nx.draw(G, pos, labels=labels, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
    plt.title("Grafo del Árbol")
    plt.show()
