# Run me in Python 3.5

import math
import sys
import string

class City:

    distances = {}
    cities = 0

    # Preprocess the distances between cities to save computation time
    def init(cities):
        City.distances = {}
        City.cities = cities
        for city1 in cities:
            for city2 in cities:
                if city1.id not in City.distances:
                    City.distances[city1.id] = {}
                if city2.id not in City.distances:
                    City.distances[city2.id] = {}
                # Use Euclidean Distances
                dist = math.sqrt(math.pow(city1.x - city2.x , 2) + math.pow(city1.y - city2.y, 2))
                City.distances[city1.id][city2.id] = dist
                City.distances[city2.id][city1.id] = dist


    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.h = math.inf
        self.f = math.inf

    def clone(self):
        return City(self.id, self.x, self.y)

    def dist(self, other):
        return City.distances[self.id][other.id]

# We define paths as our states
class Path:

    # define a way to deep copy a path
    def __init__(self, path = False):
        if path:
            self.cities = list(path.cities)
            self.totalDistance = path.totalDistance
        else:
            self.cities = []
            self.totalDistance = 0
        self.weight = -1

    # add a city to the path, increment the total distance
    def addCity(self, city):
        self.totalDistance = self.totalDistance + self.dist(city)
        # signal weight recalculation
        self.weight = -1
        self.cities.append(city)

    # the distance from the current city to the next
    def dist(self, city):
        if len(self.cities) > 0:
            currentCity = self.cities[-1]
            return currentCity.dist(city)
        return 0

    # list of the cities not in the path
    def unvisitedCities(self, cities, origin):
        unvisitedCities = [city for city in cities if city not in self.cities]
        if len(unvisitedCities) == 0 and self.cities.count(origin) != 2:
            unvisitedCities.append(origin)
        return unvisitedCities

    def toString(self):
        stuff = ""
        for city in self.cities:
            stuff = str(list(string.ascii_uppercase).index(city.id)) + " " + stuff
        stuff = stuff + str(self.totalDistance)
        return stuff

    # g is the total distance of the path
    def g(self):
        return self.totalDistance

    # h is the total distance of the minimum spanning tree containing
    # of all of the unvisited cities + the current city in the path
    # we calculate it with prim's algorithm
    def h(self):
        if self.weight >= 0:
            return self.weight
        unvisited_cities = [city for city in City.cities if city not in self.cities]
        # if we visited every node: end
        if len(unvisited_cities) == 0:
            return 0;
        # we begin with the current city of the path
        tree_cities = [self.cities[-1]]
        value = 0
        while len(unvisited_cities) > 0:
            min_dist = math.inf
            min_city = 0
            for unvisited_city in unvisited_cities:
                for tree_city in tree_cities:
                    dist = tree_city.dist(unvisited_city)
                    # Add the edge  of an unvisited city
                    # with the smallest distance from your constructed tree
                    if dist < min_dist:
                        min_dist = dist
                        min_city = unvisited_city
            value = value + min_dist
            tree_cities.append(min_city)
            unvisited_cities.remove(min_city)
        self.weight = value
        return value

    def f(self):
        return self.g() + self.h()

# calculate for 11 lengths, 10 files each
for i in range(10,11):
    total_distances = 0
    print( "LENG\tFILE\tDIST\tNSUC" )
    for j in range(10):
        fileName = "randTSP/" + str(i + 1) + "/instance_" + str(j + 1) + ".txt"
        inputFile = open(fileName, "r")
        lineNumber = 0
        cities = []
        origin = False

        # basic IO to read the file
        for line in inputFile:
            lineNumber = lineNumber + 1
            if lineNumber == 1:
                continue
            info = line.split(" ")
            city = City(info[0], int(info[1]), int(info[2]))
            cities.append(city)
            if city.id == 'A' and not origin:
                origin = city

        if not origin:
            print("No origin city of id A was found")
            sys.exit(1)

        City.init(cities)
        originPath = Path()
        originPath.addCity(origin)
        queue = [originPath]

        # maintain a priority queue that's ordered by total distance of the paths
        # insertion is done through binary search
        def binSearchAdd(paths, path):
            lo = 0
            hi = len(paths)
            while lo < hi:
                mid = int((lo + hi) / 2)
                if paths[mid].f() < path.f():
                    lo = mid + 1
                else:
                    hi = mid
            paths.insert(lo, path)

        bestPath = 0;
        successorsCount = 1;

        # recursive A* search
        while len(queue) > 0:
            path = queue[0]
            queue = queue[1:]
            unvisitedCities = path.unvisitedCities(cities, origin);
            # If the path contains all the cities: end
            if len(unvisitedCities) == 0:
                bestPath = path;
                break;
            # for each unvisited city, expand and add them in order to the the queue
            # like A* search
            # cities are alphabetically ordered since they are parsed in the order
            # that they appear in the text file
            for city in unvisitedCities:
                newPath = Path(path)
                newPath.addCity(city)
                binSearchAdd(queue, newPath)
                # we count nodes as they are generated as successors
                successorsCount = successorsCount + 1

        if bestPath != 0:
            print( str(i+1) + "\t" + str(j+1) + "\t" + str(int(path.totalDistance)) + "\t" + str(successorsCount) )
            total_distances = total_distances + successorsCount
        inputFile.close()
    print()
    print("*********************************************")
    print("Average # of successors for length " + str(i+1) + " : " + str(int(total_distances / 10)))
    print("*********************************************")
    print()