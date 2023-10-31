import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

adjacency_matrix = np.array([
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0]
    ])

damping_factor = 0.85

num_pages = len(adjacency_matrix)
page_rank = np.ones(num_pages) / num_pages

num_iterations = 100

for i in range (num_iterations):
        new_page_rank = np.zeros(num_pages)
        for j in range (num_pages):
                linking_pages = [k for k in range(num_pages) if adjacency_matrix[k, j] == 1]
                for linking_page in linking_pages:
                        new_page_rank[j] += page_rank[linking_page] / sum(adjacency_matrix[linking_page, :])
                new_page_rank[j] = damping_factor * new_page_rank[j] + (1 - damping_factor) / num_pages
        page_rank = new_page_rank

for page, rank in enumerate(page_rank):
        print(f"PR(Page {page + 1} = {rank:.3f})" )

#Create a directed graph
G = nx.DiGraph()

#Add nodes
G.add_nodes_from(range(num_pages))

#add edges based on the adjacency matrix
for i in range(num_pages):
        for j in range(num_pages):
                if adjacency_matrix[i,j] == 1:
                        G.add_edge(i, j)

#draw the graph
pos = nx.spring_layout(G)
labels = {i: f"Page {i + 1}" for i in range(num_pages)}
nx.draw(G, pos, with_labels=True, labels=labels, node_size = 1000, node_color = 'lightblue', font_size =10, font_color = 'black', font_weight = 'bold', arrowsize = 20)
plt.title("PageRank Examine Graph")
plt.show()

