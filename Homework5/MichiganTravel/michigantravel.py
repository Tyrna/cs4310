from collections import defaultdict

#Undirected graph data structure
class Graph(object):

    def __init__(self):
        self._graph = defaultdict(set)

    def add(self, vert1, vert2):
        self._graph[vert1].add(vert2)
        self._graph[vert2].add(vert1)

    #For printing purposes
    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


def main():
    #f = open(input("Please provide the name of the input file. Example: input.txt\n"), "r+")
    f = open("input.txt", "r+")
    myGraph = Graph()

    #Get N (number of cities/vertices) and M (number of roads/edges)
    graphVal = [int(x) for x in list(f.readline().split(" "))]
    N = graphVal[0]
    M = graphVal[1]

    #Get road connections
    for i in range(0, M):
        road = [int(x) for x in list(f.readline().split(" "))]
        myGraph.add(road[0], road[1])
        

    #Get the roads we want to find the smoother connection from
    endGoal = [int(x) for x in list(f.readline().split(" "))]


    
    print(myGraph._graph)

#If called not as a module
if __name__ == "__main__":
    main()