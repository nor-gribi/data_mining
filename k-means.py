import numpy as np

###########################K-Means#####################################
#fonction de calcul des distances
def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros((size_x, size_y))
    for x in range(size_x):
        matrix[x, 0] = x
    for y in range(size_y):
        matrix[0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x - 1] == seq2[y - 1]:
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
    stem=matrix[size_x - 1, size_y - 1]
    return (stem)

def calcul_moy(liste):  # Pour calculer les nouvelles moyennes aprés chaque itération.
    stem = ""
    i = 0
    taille = len(liste[1])
    nb_a = nb_c = nb_g = nb_t = 0
    # we are calculating the occurence of each letter in each chain
    while len(stem) < taille and i < taille - 1:
        for chaine in liste:
            if chaine[i] == 'A' or 'a': nb_a += 1
            if chaine[i] == 'C' or 'c': nb_c += 1
            if chaine[i] == 'G' or 'g': nb_g += 1
            if chaine[i] == 'T' or 't': nb_t += 1
        # On calcule pour chaque colonne le Mod et on l'insére dans la chaine moyenne.
        # Le mod = la lettre ayant le plus apparrue dans la colonne.
        if nb_a == max(nb_a, nb_c, nb_g, nb_t):
            stem += 'A'
        elif nb_c == max(nb_a, nb_c, nb_g, nb_t):
            stem += 'C'
        elif nb_g == max(nb_a, nb_c, nb_g, nb_t):
            stem += 'G'
        elif nb_t == max(nb_a, nb_c, nb_g, nb_t):
            stem += 'T'
        nb_a = nb_c = nb_g = nb_t = 0
        i += 1
    return stem

# choose k objects from our data to be the initial centers
c1 = ["CCAGCTGCATCACAGGAGGCCAGCGAGCAGGTCTGTTCCAAGGGCCTTCGAGCCAGTCTG"]
c2 =["AGACCCGCCGGGAGGCGGAGGACCTGCAGGGTGAGCCCCACCGCCCCTCCGTGCCCCCGC"]  
c3 = ["GAGGTGAAGGACGTCCTTCCCCAGGAGCCGGTGAGAAGCGCAGTCGGGGGCACGGGGATG"]  

data = ["GGGCTGCGTTGCTGGTCACATTCCTGGCAGGTATGGGGCGGGGCTTGCTCGGTTTTCCCC",
        "GCTCAGCCCCCAGGTCACCCAGGAACTGACGTGAGTGTCCCCATCCCGGCCCTTGACCCT",
        "CAGACTGGGTGGACAACAAAACCTTCAGCGGTAAGAGAGGGCCAAGCTCAGAGACCACAG"]  
#m1 refers to moyenne
init_c1 = m1 = c1[0]
init_c2 = m2 = c2[0]  # Initialiser les moyennes de chaque Cluster par l'element
init_c3 = m3 = c3[0]  # qu'il contient

c1_check = c1
c2_check = c2  # Pour vérifier si les centres ont changé après chaque itération.
c3_check = c3
#to verify if there is any changes in the centers
while c1_check==c1 and c2_check==c2 and c3_check==c3:
    for chaine in data:
        similitude = max(levenshtein(chaine, m1), levenshtein(chaine, m2), levenshtein(chaine, m3))
        if similitude == levenshtein(chaine, m1):
            c1.append(chaine)
            if chaine in c2: c2.remove(chaine)
            elif chaine in c3: c3.remove(chaine)
        elif similitude == levenshtein(chaine, m2):
            c2.append(chaine)
            if chaine in c1: c1.remove(chaine)
            elif chaine in c3: c3.remove(chaine)
        else:
            c3.append(chaine)
            if chaine in c1: c1.remove(chaine)
            elif chaine in c2: c2.remove(chaine)
    if c1_check != c1 or c2_check != c2 or c3_check != c3:
        c1_check = c1
        c2_check = c2
        c3_check = c3
        m1 = calcul_moy(c1)
        m2 = calcul_moy(c2)
        m3 = calcul_moy(c3)
    else:
        print()
        print("===================== Données Initiales ======================")
        print("Chaines : " + str(data))
        print("====================== Centres Initiaux ======================")
        print("Centre 1: " + str(init_c1))
        print("Centre 2: " + str(init_c2))
        print("Centre 3: " + str(init_c3))
        print("======================= Resultat Final =======================")
        print("Cluster 1: " + str(c1))
        print("Cluster 2: " + str(c2))
        print("Cluster 3: " + str(c3))
        print("====================== Fin du programme ======================")
        exit(0)
