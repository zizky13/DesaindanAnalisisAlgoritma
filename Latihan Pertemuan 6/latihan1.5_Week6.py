import matplotlib
import matplotlib.pyplot as plt
import random
import time
import itertools


def exact_TSP(cities):
    "Generate all possible tours of the cities and choose the shortest one"
    return shortest(alltours(cities))


def shortest(tours):
    "Return the tour with the minimum total distance"
    return min(tours, key=total_distance)


alltours = itertools.permutations  # permutation function is already defined inside itertools function

cities = {1, 2, 3}

list(alltours(cities))

def total_distance(tour):
    return sum(distance(tour[i],tour[i-1]) for i in range (len(tour)))

def distance(A,B):
    return abs(A-B)

City = complex

A = City(300, 0)
B = City(0, 400)
distance(A,B)

def Cities(n):
    return set(City(random.randrange(10,890),random.randrange(10,590)) for c in range (n))

random.seed('seed')
cities8,cities10,cities100,cities1000 = Cities(8), Cities(10), Cities(100), Cities(1000)
cities8

tour = exact_TSP(cities8)

print(tour)
print(total_distance(tour))

def alltours(Cities):
    start = first(Cities)
    return [[start] + list(tour)
            for tour in itertools.permutations(Cities - {start})]

def first(collection):
    for x in collection: return x

alltours({1,2,3})
alltours({1,2,3,4})

tour = exact_TSP(cities8)
print(tour)
print(total_distance(tour))

import time
def plot_tour(algorithm, cities):
      t0 = time.time()
      tour = algorithm(cities)
      t1 = time.time()
      plotline(list(tour) + [tour[0]])
      plotline([tour[0]], 'rs')
      plt.show()
      print("{} citiy tour; total distance = {:.1f}, time = {:.3f} secs for{}".format(len (tour), total_distance(tour), t1-t0, algorithm.__name__))

def plotline(points, style='bo-'):
  X, Y = XY(points)
  plt.plot(X, Y, style)

def XY(points):
  return[p.real for p in points], [p.imag for p in points]

plot_tour(exact_TSP, cities8)
plot_tour(exact_TSP, cities10)

def greedy_TSP(cities):
  start = first(cities)
  tour = [start]
  unvisited = cities - {start}
  while unvisited:
    C = nearest_neighbor(tour[-1], unvisited)
    tour.append(C)
    unvisited.remove(C)
  return tour

def nearest_neighbor(A, cities):
  return min(cities, key=lambda x: distance(x,A))

cities = Cities(9)
plot_tour(exact_TSP, cities)
plot_tour(greedy_TSP, cities)

def greedy_TSP(cities):
  start = first(cities)
  tour = [start]
  unvisited = cities - {start}
  while unvisited:
    C = nearest_neighbor(tour[-1], unvisited)
    tour.append(C)
    unvisited.remove(C)
  return tour

def nearest_neighbor(A, cities):
  return min(cities, key=lambda x: distance(x,A))

cities = Cities(9)
plot_tour(exact_TSP, cities)
plot_tour(greedy_TSP, cities)
plot_tour(greedy_TSP, cities100)
plot_tour(greedy_TSP, cities1000)


def all_greedy_TSP(cities):
    """Try the greedy algorithm from each of the starting cities; return the shortest tour."""
    return shortest(greedy_TSP(cities, start=c) for c in cities)

def greedy_TSP(cities, start=None):
    """At each step, visit the nearest neighbor that is still unvisited."""

    if start is None:
        start = first(cities)

    tour = [start]
    unvisited_cities = cities - {start}

    while unvisited_cities:
        C = nearest_neighbor(tour[-1], unvisited_cities)
        tour.append(C)
        unvisited_cities.remove(C)

    return tour
plot_tour(greedy_TSP, cities100)
plot_tour(all_greedy_TSP, cities100)


import itertools

def greedy_exact_end_TSP(cities, start=None, end_size=8):
    """
    At each step, visit the nearest neighbor that is still unvisited until there are k_end cities left;
    then choose the best of all possible endings.
    """

    if start is None:
        start = first(cities)
    tour = [start]

    unvisited_cities = cities - {start}

    # Use greedy algorithm for all but the last end_size cities
    while len(unvisited_cities) > end_size:
        C = nearest_neighbor(tour[-1], unvisited_cities)
        tour.append(C)
        unvisited_cities.remove(C)

    # Consider all permutations of possible ends to the tour, and choose the best one
    ends = map(list, itertools.permutations(unvisited_cities))

    best = shortest([tour[0], tour[-1]] + end for end in ends)

    return tour + best[2:]

plot_tour(greedy_exact_end_TSP, cities100)
plot_tour(greedy_exact_end_TSP, cities1000)

import random

def greedy_bi_TSP(cities, start_size=12, end_size=6):
    """
    At each step, visit the nearest neighbor that is still unvisited.
    """

    starts = random.sample(cities, min(len(cities), start_size))

    return shortest(greedy_exact_end_TSP(cities, start, end_size) for start in starts)
random.seed('bi')
plot_tour(greedy_bi_TSP, cities100)
plot_tour(greedy_bi_TSP, cities1000)

def compare_algorithms(algorithms, maps):
    """
    Apply each algorithm to each map and plot results.
    """
    for algorithm in algorithms:
        ti = time.time()
        results = [total_distance(algorithm(m)) for m in maps]
        te = time.time()
        avg = sum(results) / len(results)
        print('{:.0f} x {:.1f}s: {}'.format(avg, te - ti, algorithm.__name__))
        plt.plot(sorted(results), label=algorithm.__name__)

    plt.legend(loc=2)
    plt.show()
    print('{} x {}-city maps'.format(len(maps), len(maps[0])))

def Maps(M, N):
    """
    Return a list of M maps, each consisting of a set of N cities.
    """
    return [Cities(N) for m in range(M)]
compare_algorithms([greedy_TSP, greedy_exact_end_TSP, all_greedy_TSP], Maps(100,50))

def bi_10_6(cities):
    return greedy_bi_TSP(cities, 10, 6)

def bi_20_5(cities):
    return greedy_bi_TSP(cities, 20, 5)

def bi_40_4(cities):
    return greedy_bi_TSP(cities, 40, 4)

def bi_80_2(cities):
    return greedy_bi_TSP(cities, 80, 2)

def bi_160_1(cities):
    return greedy_bi_TSP(cities, 160, 1)

algorithms = [bi_10_6, bi_20_5, bi_40_4, bi_80_2, bi_160_1]
compare_algorithms(algorithms, Maps(100,50))
compare_algorithms(algorithms, Maps(50,100))
compare_algorithms(algorithms, Maps(25,160))
