from collections import defaultdict
import queue

#Undirected graph data structure
class Graph(object):

    ##._graph = Dictionary of Sets(ConnectedVert, Speed, bestRatio)
    ##._queue = Queue of cities/vertex we need to visit

    def __init__(self):
        self._graph = defaultdict(list)
        self._queue = queue.Queue()

    def addEdges(self, vert1, vert2, speed):
        self._graph[vert1].append((vert2,speed))
        self._graph[vert2].append((vert1,speed))

    def addRatio(self, vert, ratio):
        self._graph[vert].append([ratio, ratio])

    def getVertex(self, id):
        return self._graph[id]

    def setRatio(self, vert, speed):
        if (self._graph[vert][0][0] == 0):
            self._graph[vert][0][0] = speed
            self._graph[vert][0][1] = speed
        #if it is bigger than the MAX
        elif (speed > self._graph[vert][0][0]):
            self._graph[vert][0][0] = speed
        #if it is smalles than the MIN
        elif (speed < self._graph[vert][0][1]):
            self._graph[vert][0][1] = speed
        else:
            None

    def findSmoothestPath(self, id1, id2):
        vert1 = self.getVertex(id1)
        vert2 = self.getVertex(id2)
        #Move along all edges of vert1 
        print(vert1)
        while(true):
            for edges in vert1[1:]:
                #From id1 to edges[0] in edges[1] speed
                print("From " + str(id1) + " to " + str(edges[0]) + " in speed: " + str(edges[1]))

                #Check if current Ratio is better than the ratio the city has
                self.setRatio(edges[0], edges[1])
                print(self.getVertex(edges[0]))

                #Enqueue the vertex we need to visit in our queue
                self._queue.put(edges[0])
        #Check queue to see if there are more vertices to Check
    	try:
    		next = self._queue.get()
    	except:
    		#No more vertices to look at
    		break;
        
        #If there are more vertices

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
        myGraph.addRatio(i, 0)

    #Get road connections
    for i in range(0, M):
        road = [int(x) for x in list(f.readline().split(" "))]
        myGraph.addEdges(road[0], road[1], road[2])

    #Get the roads we want to find the smoother connection from
    endGoal = [int(x) for x in list(f.readline().split(" "))]
    
    myGraph.findSmoothestPath(1, 6)


#If called not as a module
if __name__ == "__main__":
    main()