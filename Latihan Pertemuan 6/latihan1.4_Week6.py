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