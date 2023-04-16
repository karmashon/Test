# One of the ways of traversing a Graph is Depth-First Search (DFS)
# It is implemented using recursion.
class Graph:
    
    def __init__(self,vertexCount):
        self.vertexCount = vertexCount
        self.matrix = [[0 for i in range(vertexCount)] for j in range(vertexCount)]


    def addEdge(self,v1,v2):

        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1


    def removeEdge(self,v1,v2):

        if self.containsEdge(v1,v2):

            self.matrix[v1][v2] = 0
            self.matrix[v2][v1] = 0

        else:
            return


    def containsEdge(self,v1,v2):

        if self.matrix[v1][v2] == 1:
            return True
        else:
            return False


    # This function calls on a helper function to perform Depth First Search
    def DFS(self):

        # Exclude graphs with 0 vertices
        if self.vertexCount == 0:
            return

        # Create an array that stores 1 if a vertex has been visited, and 0 otherwise.
        # This prevents the search from going back to a previously visited vertex.
        visited = [False for i in range(self.vertexCount)]

        # Traverse through each verterx and perform DFS for them one by one.
        # This allows printing even vertices that are disconnected from the initial vertex(0).
        for i in range(self.vertexCount):

            # If the vertex is not visited yet, perform DFS on it
            if not visited[i]:
                self.DFSHelper(i,visited)
        
    # Depth First Search will start from the initial vertex(0), and traverse one adjacent vertex at a time.
    # After one vertex is complete, the next one is called.
    # Repeated calls are avoided using an array to store the status of visiting a vertex.
    def DFSHelper(self,startVertex,visited):

            # Mark the vertex as visited and print it.
            visited[startVertex] = True
            print(startVertex,end=' ')

            # Go through each of the vertices in the graph
            for i in range(self.vertexCount):
                
                # Check if the vertex is adjacent to the current vertex and not visited previously
                if self.matrix[startVertex][i] == 1 and not visited[i]:
                    self.DFSHelper(i,visited)
 
g = Graph(6)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(3,4)

g.DFS()
