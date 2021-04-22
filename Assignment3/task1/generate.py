import networkx as nx
import utils
import matplotlib.pyplot as plt

# g = generators.random_graph_generator(10, 0.3)

# nx.draw(g, with_labels = True)
# plt.savefig("path.png")

# g = generators.watts_strogatz_graph_generator(10, 0.7)

g = utils.barabasi_albert_model(10, 4, 3)
# nx.draw(g, with_labels = True)
nx.draw(g, with_labels = True)
plt.savefig("barabasi_albert.png")

probabilities = [0.2, 0.3, 0.5]

for p in probabilities:
    with open(f'graphs/random_{p}.txt', "wb") as f:
        g = utils.random_graph_generator(2000, 0.2)
        nx.write_edgelist(g, f)

for p in probabilities:
    with open(f'graphs/watts_strogatz_{p}.txt', "wb") as f:
        g = utils.watts_strogatz_graph_generator(2000, 0.2)
        nx.write_edgelist(g, f)

links = [2, 5, 10]
for l in links:
    with open(f'graphs/barbasi_albert_{l}.txt', "wb") as f:
        g = utils.barabasi_albert_generator(2000, 50, l)
        nx.write_edgelist(g, f)