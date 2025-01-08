import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()


# Додавання вершин
G.add_nodes_from(["One", "Two", "Three", "Four", "Five", "Six", "Seven"])


# Додавання ребер
G.add_edges_from([
    ("One", "Two"), 
    ("One", "Three"), 
    ("Two", "Four"), 
    ("Two", "Five"), 
    ("Three", "Six"), 
    ("Three", "Seven")
])


# Візуалізація бінарного дерева
pos = {"One": (0, 0), "Two": (-1, -1), "Three": (1, -1), "Four": (-2, -2), "Five": (0, -2), "Six": (2, -2), "Seven": (1, -3)}


nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=10, edge_color='gray', arrows=True)
plt.show()
