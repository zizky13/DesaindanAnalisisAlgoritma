import numpy as np

adjacency_matrix = np.array([
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]]
)

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