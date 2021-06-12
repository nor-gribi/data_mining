from functools import reduce
import numpy as np
def ver_chaine(a):
    return reduce(lambda x, y: x and y, map(lambda x: x == 'A' or x == 'C' or x == 'T' or x == 'G', a.upper()))

def Read_file(file_name):
    chaines = []
    with open(file_name) as l:
        line = l.readline()
        while line:
            if ver_chaine(line.rstrip('\n').upper()):
                chaines.append(line.rstrip('\n').upper())

            line = l.readline()
    return chaines

def notre_dis(chaine1, chaine2):
    score = 0
    size_x = len(chaine1) + 1
    size_y = len(chaine2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if chaine1[x - 1] == chaine2[y - 1]:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1],
                    matrix[x, y - 1] + 1
                )
            else:
                matrix[x, y] = min(
                    matrix[x - 1, y] + 1,
                    matrix[x - 1, y - 1] + 1,
                    matrix[x, y - 1] + 1
                )
        score = matrix[size_x - 1, size_y - 1]
    return score

def voisinage(chaines, p, e):
    v = []
    for k in chaines:
        if notre_dis(p, k) <= int(e):
            v.append(k)
    return v

def core(x):
    v = voisinage(chaines, x, e)
    if len(v) < int(p_min):
        return "false"
    else:
        return "true"

def agrandir_cluster(cluster, v, visited):
    for u in v:
        if u not in visited:
            vs = voisinage(chaines, u, e)
            if core(u) == "true":
                v.append(vs)
                if u not in cluster:
                    cluster.append(u)
        return cluster

# programme principal
bruit = []
visited = []
clusters = [[]]
clust = []
chaines = Read_file("dataset.txt")
print(chaines)
#e = input("Entrez la valeur de epsilon : ")
e =input('enter epsilon : ')
#p_min = input("Entrez le nombre min de points: ")
p_min = input('enter min number of points : ')
for i in range(0, len(chaines)):
    if chaines[i] not in visited:
        v = voisinage(chaines, chaines[i], e)
        if core(chaines[i]) == "false":
            bruit.append(chaines[i])
        else:
            clust = agrandir_cluster(clust, v, visited)
            clusters.append(chaines[i])
            visited.append(clust)

print( "Les clus sont: ")
print(clusters)
print('estimated number of clusters : ',len(clusters))
print('estimated number of noise points : ',len(bruit))
print( "\n")
