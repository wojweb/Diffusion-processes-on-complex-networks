import utils
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
import collections

g = nx.Graph()

# (g, fiend = utils.get_list_of_friends("valerois")
def add_friends_of_friends_to_graph(g, name, level):
    if level == 0:
        return g
    else:
        friends = utils.get_list_of_friends(name)
        for friend in friends:
            print(str(level) + friend)

            g.add_edge(name, friend)
            g = add_friends_of_friends_to_graph(g, friend, level - 1)

    return g
snowball_level = 2

# g = add_friends_of_friends_to_graph(g, "valerois", snowball_level)
# nx.write_edgelist(g, "friends_of_valerois_level2.graph")

g = nx.read_edgelist("friends_of_valerois_level2.graph")
print(f'number of nodes {g.number_of_nodes()}')
print(f'number of edges {g.number_of_edges()}')
print()

print(f'celebrities in this network are:')
for name, number in sorted(list(g.degree()), key = itemgetter(1), reverse=True)[:5]:
    print(f'-> {name} with {number} friends')
print() 


degree_sequence = sorted([d for n, d in g.degree()])
degreeCount = collections.Counter(degree_sequence)
degs = dict(degreeCount).keys()
pvals = [k / g.number_of_nodes() for k in dict(degreeCount).values()]

plt.stem(degs, pvals)
plt.xlabel("degree $k$")
plt.ylabel("$p_k$")
plt.title("Degree distribution")
plt.savefig("distribution")

print()


print(f'communication bottlenecks in this network are:')
for name, number in sorted(list(nx.betweenness_centrality(g).items()), key = itemgetter(1), reverse=True)[:5]:
    print(f'-> {name} with {number} shortests paths')
print() 

