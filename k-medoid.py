import distance

from pyclustering.cluster.kmedoids import kmedoids
import Pycluster as cp

words = ['CCAGCTGCATCACAGGAGGCCAGCGAGCAGGTCTGTTCCAAGGGCCTTCGAGCCAGTCTG',
         'AGACCCGCCGGGAGGCGGAGGACCTGCAGGGTGAGCCCCACCGCCCCTCCGTGCCCCCGC',
         'GAGGTGAAGGACGTCCTTCCCCAGGAGCCGGTGAGAAGCGCAGTCGGGGGCACGGGGATG',
         'GGGCTGCGTTGCTGGTCACATTCCTGGCAGGTATGGGGCGGGGCTTGCTCGGTTTTCCCC',
         'GCTCAGCCCCCAGGTCACCCAGGAACTGACGTGAGTGTCCCCATCCCGGCCCTTGACCCT',
         'CAGACTGGGTGGACAACAAAACCTTCAGCGGTAAGAGAGGGCCAAGCTCAGAGACCACAG']

dist = [distance.levenshtein(words[i], words[j])
        for i in range(1, len(words))
        for j in range(0, i)]
i = 1
labels, error, nfound = cp.kmedoids(dist,nclusters=3)
cluster = dict()
for word, label in zip(words, labels):
    cluster.setdefault(label, []).append(word)
for label, grp in cluster.items():
    print('cluster',i,' : ',grp)
    i += 1
