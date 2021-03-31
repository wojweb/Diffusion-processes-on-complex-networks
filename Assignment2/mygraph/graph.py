

class Graph:
    
    def __init__(self):
        """Constructor of Graph class"""
        self.vertices = {}
        self.edges = []

    def addVertex(self, v):
        """add v vertex to graph, v can be of any type"""
        if v not in self.vertices:
            self.vertices[v] = len(self.edges)
            self.edges.append({})

    def addVerticesFromList(self, verticesList):
        """add list of vertices to graph, each vertex can be any type"""
        for v in verticesList:
            self.addVertex(v)

    def addEdge(self, v1, v2, weight = 1.):
        """ add list between vertices v1 and v2 with given weight""" 
        self.addVertex(v1)
        self.addVertex(v2)

        self.edges[self.vertices[v1]][self.vertices[v2]] = weight
        self.edges[self.vertices[v2]][self.vertices[v1]] = weight

    def addEdgesFromList(self, edgesList):
        """add list of edges, each edge is represent by trile (v1, v2, weight) or pair (v1, v2)"""
        for t in edgesList:
            if len(t) == 3:
                self.addEdge(t[0], t[1], t[2])
            if len(t) == 2:
                self.addEdge(t[0], t[1])

    def getEdges(self):
        """get edges as a list of pairs"""
        result = []
        for v1 in self.vertices.values():
            for v2, weight in self.edges[v1].items():
                if v2 >= v1:
                    for name, v in self.vertices.items():
                        if v == v1:
                            name1 = name
                        if v == v2:
                            name2 = name
                    result.append((name1, name2, weight))
        return result

    def getNeighbors(self, v1):
        """get neighbors vertices as a list"""
        result = []
        for v2, weight in self.edges[self.vertices[v1]].items():
            for name, v in self.vertices.items():
                if v == v2:
                    result.append(name)
        return result


    def __contains__(self, v):
        """it provides in operator for graph container"""
        return v in self.vertices.keys()

    def isIn(self, v):
        """implementation of my in operator - deprecated"""
        return v in self.vertices.keys()
        

    def saveGraph(self, path):
        """save graph in path using dot format """
        dot = 'graph {\n'
        for v in self.vertices.keys():
            dot += str(v) + ';\n'
        for e in self.getEdges():
            dot += str(e[0]) + ' -- ' + str(e[1]) + ';\n'
        dot += '}'

        with open(path, "w") as output_file:
            output_file.write(dot)

    def getShortestPaths(self, v):
        """get list of shortest paths from vertex v to the others"""
        result = []
        v1 = self.vertices[v]
        for name, v2 in self.vertices.items():

            length = 0
            buffer = []
            reached_vertices = []
            reached_vertices.append(v1)
            buffer.append(v1)
            notFound = True
            
            while len(buffer) != 0 and notFound:
                stageBuffer = buffer
                buffer = []

                while len(stageBuffer) != 0 and notFound:
                    v = stageBuffer.pop()
                    if v == v2:
                        result.append((name, length))
                        notFound = False
                    else:
                        for otherV in self.edges[v].keys():
                            if otherV not in reached_vertices:
                                buffer.append(otherV)
                                reached_vertices.append(otherV)
                                
                length += 1 


            if notFound:
                result.append((name, -1))

        return result


    def __str__(self):
        return 'vertices: {self.vertices}'.format(self = self)
