
import numpy as np

class GenGraph():
    def __init__(self, vertx):
        self.V = vertx
        self.plot_graph = [[0 for col in range(vertx)]
                           for row in range(vertx)]

    def Display_Solution(self, dist):
        print("Vertex \t: \tDistance from Source")
        for node in range(self.V):
            print("\t", node, "\t:\t", dist[node])

    # Find the vertex with minimum distance value
    # from the set of vertices not yet in shortest path
    def calc_min_distance(self, dist, spSet):
        min = np.inf  # default max distance
        min_idx = 1
        # look for not nearest vertex not in shortest path
        for v in range(self.V):
            if dist[v] < min and not spSet[v]:
                min = dist[v]
                min_idx = v
        return min_idx

    # Implementing Dijkstra's shortest path algorithm
    # using graph using adjacency matrix representation
    def dijkstra_algo(self, source):
        dist = [np.inf] * self.V
        dist[source] = 0
        spSet = [False] * self.V
        for cout in range(self.V):
            # Pick the minimum distance vertex
            # x is always equal to src in first iteration
            x = self.calc_min_distance(dist, spSet)

            # Put the min distance in the shortest path
            spSet[x] = True

            # Update dist value if distance is greater than new distance 
            # and the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.plot_graph[x][y] > 0 and spSet[y] == False and \
                        dist[y] > dist[x] + self.plot_graph[x][y]:
                    dist[y] = dist[x] + self.plot_graph[x][y]

        self.Display_Solution(dist)

if __name__ == "__main__":
    prb1 = GenGraph(6)
    prb1.plot_graph =[[0,4,4,0,0,0],
                      [4,0,2,0,0,0],
                      [4,2,0,3,1,6],
                      [0,0,3,0,0,2],
                      [0,0,1,0,0,3],
                      [0,0,6,2,3,0]]

    prb1.dijkstra_algo(0)