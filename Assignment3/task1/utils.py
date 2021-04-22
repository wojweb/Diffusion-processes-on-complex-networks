import networkx as nx
import random
import matplotlib.pyplot as plt
import collections

def random_graph_generator(N, p):
    """Generate graph with N nodes and probability of link equals p."""

    g = nx.Graph()
    g.add_nodes_from(range(N))

    for i in range(N):
        for j in range(i + 1, N):
            if random.random() < p:
                g.add_edge(i, j)

    return g


def watts_strogatz_graph_generator(N, p):
    """Generate watts strogatz graph with N nodes and probability of relink equals p."""

    g = nx.Graph()
    g.add_nodes_from(range(N))
    if N <= 2:
        return g

    for i in range(N - 2):
        g.add_edge(i, i + 1)
        g.add_edge(i, i + 2)
    g.add_edge(N - 2, N - 1)
    g.add_edge(N - 2, 0)
    g.add_edge(N - 1, 0)
    g.add_edge(N - 1, 1)

    for (v, u) in g.edges():
        if random.random() < p:
            g.remove_edge(v, u)
            g.add_edge(v, random.randrange(N))

    return g

def barabasi_albert_generator(N, m0, m):
    """Generate barabasi albert graph with N nodes, starting from random graph with m0 nodes
        and adding in every iteration node with m links"""
    assert m < m0
    g = random_graph_generator(m0, 0.5)

    for n in range(m0, N):
        print(n)
        g.add_node(n)
        degrees = [k for (i,k) in g.degree()]
        for i in range(m):
            added = False
            while not added:
                l = random.randrange(sum(degrees))
                for j in range(n):
                    l -= degrees[j]
                    if l < 0 and g.has_edge(n, j):
                        break
                    elif l < 0:
                        g.add_edge(n, j)
                        added = True
                        break

    return g


def properties(g :nx.Graph):
    """Print basic propertis of graph g and draw figure with dustribution of degrees."""
    print(f'number of vertices: {g.number_of_nodes()}')
    print(f'number of edges: {g.number_of_edges()}')
    print(f'average degree: {2 * g.number_of_edges() / g.number_of_nodes()}')

    degree_sequence = sorted([d for n, d in g.degree()])
    degreeCount = collections.Counter(degree_sequence)
    degs = dict(degreeCount).keys()
    pvals = [k / g.number_of_nodes() for k in dict(degreeCount).values()]

    plt.stem(degs, pvals)
    plt.xlabel("degree $k$")
    plt.ylabel("$p_k$")
    plt.title("Degree distribution")
    plt.savefig("distribution")

def show(g :nx.Graph, path : str):
    """Draw figure of graph and save it in path."""
    nx.draw(g, with_labels = True)
    plt.savefig(f"{path}")
        