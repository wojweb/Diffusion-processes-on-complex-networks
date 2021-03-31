from mygraph.graph import Graph

g = Graph()



contacts = [("Alice", "Bob"), ("Carl", "Alice"), ("Alice", "David"), ("Alice", "Ernst"), ("Alice","Frank"),
            ("Bob", "Gail"), ("Gail", "Harry"), ("Harry", "Jen"), ("Jen", "Gail"), ("Harry", "Irene"),
            ("Irene", "Gail"),("Irene", "Jan"), ("Ernst", "Frank"), ("David", "Carl"), ("Carl", "Frank")]

g.addEdgesFromList(contacts)

g.saveGraph("./file.txt")

# print(g.getEdges())
# print(g)

# g.addVertex("Ola")
# g.addVerticesFromList(["Ania", "Kasia"])
# g.addEdge("Ola", "Kasia")


# g.saveGraph("path")

# print(g.getVertices())

print(g.getShortestPaths("David"))