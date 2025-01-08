import networkx as nx
import matplotlib.pyplot as plt


# Створення пустого графа
G = nx.Graph()


# Додавання вершин
G.add_nodes_from([1, 2, 3, 4, 5])


# Додавання ребер (з'єднань між вершинами)
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])


# Візуалізація графа
pos = nx.spring_layout(G) # Визначення позицій вершин
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10, edge_color='gray')
plt.show()

def visualize_graph(graph, title):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray')
    plt.title(title)
    plt.show()


# 1. Повний граф
complete_graph = nx.complete_graph(5)
visualize_graph(complete_graph, "Complete Graph")

# 2. Циклічний граф
cycle_graph = nx.cycle_graph(6)
visualize_graph(cycle_graph, "Cyclic Graph")


# 3. Створення орієнтованого графа
directed_graph = nx.DiGraph()
directed_graph.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4)])


# Визначення позицій вершин для візуалізації
pos = nx.spring_layout(directed_graph)


# Візуалізація орієнтованого графа
nx.draw(directed_graph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray', arrowsize=20, connectionstyle="arc3,rad=0.1")


plt.title("Directed Graph")
plt.show()

# 4. Ациклічний граф
acyclic_graph = nx.DiGraph()
acyclic_graph.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])
visualize_graph(acyclic_graph, "Acyclic Graph")

# 5. Створення дводольного графа
bipartite_graph = nx.complete_bipartite_graph(2, 3)


# Розділення графа на дві групи вершин
group1_nodes = {0, 1}
group2_nodes = {3, 2, 4}


# Визначення позицій вершин для візуалізації
pos = nx.spring_layout(bipartite_graph)


# Визначення кольорів вершин для різних груп
node_colors = [0 if node in group1_nodes else 1 for node in bipartite_graph.nodes()]


# Візуалізація дводольного графа
nx.draw(bipartite_graph, pos, with_labels=True, font_size=10, node_size=700, node_color=node_colors, cmap=plt.cm.Paired)


plt.title("Bipartite Graph with Node Colors")
plt.show()

# 6. Multigraph 
G = nx.DiGraph()
edge_list = [(1,2,{'w':'A1'}),(2,1,{'w':'A2'}),(2,3,{'w':'B'}),(3,1,{'w':'C'}),
            (3,4,{'w':'D1'}),(4,3,{'w':'D2'}),(1,5,{'w':'E1'}),(5,1,{'w':'E2'}),
            (3,5,{'w':'F'}),(5,4,{'w':'G'})]
G.add_edges_from(edge_list)
pos=nx.spring_layout(G,seed=5)
fig, ax = plt.subplots()
nx.draw_networkx_nodes(G, pos, ax=ax)
nx.draw_networkx_labels(G, pos, ax=ax)
fig.savefig("1.png", bbox_inches='tight',pad_inches=0)


curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
straight_edges = list(set(G.edges()) - set(curved_edges))
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)
arc_rad = 0.25
nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges, connectionstyle=f'arc3, rad = {arc_rad}')
fig.savefig("2.png", bbox_inches='tight',pad_inches=0)

plt.title("Multigraph")
plt.show()



# 7. Створення зваженого графа
weighted_graph = nx.Graph()
weighted_graph.add_weighted_edges_from([(1, 2, 3), (2, 3, 2), (3, 4, 1), (4, 5, 4)])


# Визначення позицій вершин для візуалізації
pos = nx.spring_layout(weighted_graph)


# Витягнення ваг кожного ребра
edge_labels = {(u, v): d["weight"] for u, v, d in weighted_graph.edges(data=True)}


# Візуалізація зваженого графа
nx.draw(weighted_graph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray')
nx.draw_networkx_edge_labels(weighted_graph, pos, edge_labels=edge_labels, font_color='red', font_size=8)


plt.title("Weighted Graph")
plt.show()


# 8. Створення псевдографа
pseudograph = nx.MultiDiGraph()
pseudograph.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 1)])


# Визначення позицій вершин для візуалізації
pos = nx.spring_layout(pseudograph)


# Візуалізація псевдографа
nx.draw(pseudograph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray', arrowsize=20, connectionstyle="arc3,rad=0.1")


plt.title("Pseudograph")
plt.show()

# 9. Створення бінарного дерева
G = nx.DiGraph()


# Додавання вершин
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7])


# Додавання ребер
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)])


# Візуалізація бінарного дерева
pos = {1: (0, 0), 2: (-1, -1), 3: (1, -1), 4: (-2, -2), 5: (0, -2), 6: (2, -2), 7: (1, -3)}


nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, edge_color='gray', arrows=True)
plt.show()