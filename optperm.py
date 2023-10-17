from itertools import *
#from sortedcontainers import SortedList
import math
import sys
def main():
   # n =int(sys.argv[1])
    n =11
    num = math.floor(n/2)
    unique_edges = []
    for i in range(2, n+1):
        l = list(range(2, n+1))
        perms = list(permutations(l))
        for perm in perms:
            perm = (1, ) + perm
            dist_vector = get_edge_vector(perm, n)
            if dist_vector not in unique_edges:
                unique_edges.append(dist_vector)
    print(unique_edges)
    print("Count: " + str(len(unique_edges)))

def get_edge_vector(l, n):
    edge_list = [0]*int(math.floor(n/2))
    for i in range(len(l) - 1):
        n1 = int(l[i])
        n2 = int(l[i+1])
        dist = abs(n1 - n2)
        if dist > math.floor(n/2):
            dist = n - dist
        edge_list[dist-1] += 1
    n1 = int(l[0])
    n2 = int(l[len(l) - 1])
    dist = abs(n1 - n2)
    if dist > math.floor(n/2):
        dist = n - dist
    edge_list[dist -1] += 1
    return  edge_list
main()

