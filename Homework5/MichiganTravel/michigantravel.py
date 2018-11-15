from collections import defaultdict
import queue

#Undirected graph data structure
class Graph(object):

    ##._graph = Dictionary of Sets(ConnectedVert, Speed, bestRatio)
    ##._queue = Queue of cities/vertex we need to visit
    ##._visited = List of cities we've already visited

    def __init__(self):
        self._graph = defaultdict(list)
        self._queue = queue.Queue()
        self._visited = []

    def startVertex(self, vert, ratio):
        #Ratio
        self._graph[vert].append([])
        #Edges
        self._graph[vert].append([])

    def addEdges(self, vert1, vert2, speed):
        self._graph[vert1][1].append((vert2,speed))
        self._graph[vert2][1].append((vert1,speed))

    def addRatio(self, vert, max, min):
        if ([max, min] not in self._graph[vert][0]):
            self._graph[vert][0].append([max, min])

    def setRatio(self, vert, vert2, speed):
        #print(self._graph[vert][0][0])

        #If minimum is bigger than speed...
        if (self._graph[vert2][0][0][1] > speed):
            self.addRatio(vert, self._graph[vert2][0][0][0], speed)
        #If the maximum is smaller than speed...
        elif (self._graph[vert2][0][0][0] < speed):
            self.addRatio(vert, speed, self._graph[vert2][0][0][1])
        else:
            self.addRatio(vert, self._graph[vert2][0][0][0], self._graph[vert2][0][0][1])

    def getVertex(self, id):
        return self._graph[id]

    def checkSourceChildren(self, source, end, second):
        for vert in self._visited:
            #Look for all vertices next to this vertex.
            #For those that do not have a path to Source, add them to the queue if second round
            #For those that have a path to Source, calculate Ratios
            for edges in self._graph[vert][1]:
                if (edges[0] in self._visited):
                    #print(vert, " has ", edges[0])
                    self.setRatio(vert, edges[0], edges[1])
                else:
                    if (second and edges[0] != source and edges[0] != end):
                        self._queue.put(edges[0])

    def checkOtherVertices(self, vert, end):
        for edges in self._graph[vert][1]:
            #If the vertex at the end of the edge have paths to the source...
            allPaths = self._graph[edges[0]][0]
            if (len(allPaths) > 0):
                #Get the best path considering the speed we go to given vertex
                bestRatio = [30001, 1]
                for ratio in allPaths:
                    #First change min/max respectively
                    if (ratio[0] < edges[1]):
                        ratio = [edges[1], ratio[1]]
                    elif (ratio[1] > edges[1]):
                        ratio = [ratio[0], edges[1]]

                    if (ratio[0]/ratio[1] < bestRatio[0]/bestRatio[1]):
                        bestRatio = ratio

                #print(bestRatio)
                self.addRatio(vert, bestRatio[0], bestRatio[1])

    def findFromEnd(self, end):
        answer = [30001, 1]
        for edges in self._graph[end][1]:
            allPaths = self._graph[edges[0]][0]
            #Get the best path considering the speed we go to given vertex
            bestRatio = [30001, 1]
            for ratio in allPaths:
                #First change min/max respectively
                if (ratio[0] < edges[1]):
                    ratio = [edges[1], ratio[1]]
                elif (ratio[1] > edges[1]):
                    ratio = [ratio[0], edges[1]]

                if (ratio[0]/ratio[1] < bestRatio[0]/bestRatio[1]):
                    bestRatio = ratio

            if (bestRatio[0]/bestRatio[1] < answer[0]/answer[1]):
                    answer = bestRatio

        return answer

    def findSmoothestPath(self, id1, id2):
        #Look at all vertices directly attached to the Source
        for i in self.getVertex(id1)[1]:
            self.addRatio(i[0], i[1], i[1])
            self._visited.append(i[0])
            #self._queue.put(i[0])

        #Look at each of those vertices and look for routes that will end up going to the Source
        #DO THIS TWICE
        self.checkSourceChildren(id1, id2, False)
        self.checkSourceChildren(id1, id2, True)
        
        #As long as there are vertices to check...
        while (self._queue.qsize()):
            try:
                vert = self._queue.get()
                self.checkOtherVertices(vert, id2)
            except:
                break

        #Once all the vertices have been checked, find the smoothest path from vertices adjacent to the end city
        return self.findFromEnd(id2)

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

    #Add empty ratio to the cities
    for i in range(1, N+1):
        myGraph.startVertex(i, 0)

    #Get road connections
    for i in range(0, M):
        road = [int(x) for x in list(f.readline().split(" "))]
        myGraph.addEdges(road[0], road[1], road[2])

    #Get the roads we want to find the smoother connection from
    endGoal = [int(x) for x in list(f.readline().split(" "))]
    
    #print(myGraph._graph)
    result = myGraph.findSmoothestPath(endGoal[0], endGoal[1])
    if (result[0] == 30001):
        print("IMPOSSIBLE")
    else:
        print(result[0], "/", result[1])


#If called not as a module
if __name__ == "__main__":
    main()