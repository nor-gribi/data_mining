# This Python file uses the following encoding: utf-8
import re
from time import time
from functools import reduce

debut = time()
# from BasicAlgorithms import *
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


def levenstein(chaine1, chaine2):
    longueur_chaine1, longueur_chaine2 = len(chaine1), len(chaine2)
    distances = [[0 for x in range(longueur_chaine2)] for y in range(longueur_chaine1)]

    for i in range(0, longueur_chaine1):
        distances[i][0] = i

    for i in range(0, longueur_chaine2):
        distances[0][i] = i

    for i in range(1, longueur_chaine1):
        for j in range(1, longueur_chaine2):
            if chaine1[i - 1] == chaine2[j - 1]:
                cout = 0
            else:
                cout = 1
            distances[i][j] = min(distances[i - 1][j] + 1, distances[i][j - 1] + 1, distances[i - 1][j - 1] + cout)

    return distances[longueur_chaine1 - 1][longueur_chaine2 - 1]


def agnes(data):
    taille_data = len(data)
    dict_clusters = {}
    dict_distances = {}
    # Initialize a cluster for each sequence
    for i in range(taille_data):
        dict_clusters[i] = list()  # The key represents the index of the sequence

    # Calculate distances between clusters
    for i in range(taille_data):
        for j in range(i + 1, taille_data):
            dict_distances[(i, j)] = levenstein(data[i], data[j])  # to save distances

    taille_dict = taille_data
    message = '***********  ******  AGNES  ******  ***********\n\n'
    print('# At start, each data point forms a cluster')
    message += str.format('Les {0} clusters de départ sont :\n{1}\n\n', taille_dict, dict_clusters)
    print(message)
    cpt = 0
    while taille_dict > 1:
        cpt += 1  # For iteration messages
        # Just getting the first occurance
        for d in dict_distances.items():
            distance_min = d
            break

        # Searching for the minimum distance
        for item_distance in dict_distances.items():
            if distance_min[1] > item_distance[1]:
                distance_min = item_distance

        # Jumeler the two clusters
        ## Get index of the cluster host
        index_host = distance_min[0][0]
        ## Get index of the cluster invite
        index_invite = distance_min[0][1]
        ## Appending the cluster itself
        dict_clusters[index_host].append(index_invite)
        ## Appending content of the cluster
        for c in dict_clusters[index_invite]:
            dict_clusters[index_host].append(c)

        # Take off the cluster invited
        del dict_clusters[index_invite]

        # Take off all items with the index invite
        for index in dict_clusters.keys():
            #
            if index > index_invite:
                del dict_distances[(index_invite, index)]
            else:
                del dict_distances[(index, index_invite)]

        # Change dict_clusters length
        taille_dict -= 1

        # Afficher message
        message_part = str.format('Apres {0} regroupment, les {1} clusters sont :\n{2}\n', cpt, taille_dict,
                                  dict_clusters)
        message += message_part
        print(message_part)
        print('# At the end, all data points are within a single cluster')
    return message


if __name__ == '__main__':


    data = Read_file("dataset.txt")

    agnes(data)

    fin = time()
    temps_de_reponse = fin - debut
    print(temps_de_reponse)
