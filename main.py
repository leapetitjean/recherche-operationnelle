#imports
from Heuristic import Heuristic
from Algorithm import Algorithm
from Application import Application
from CloseNeighbor import CloseNeighbor
from NearInsertion import NearInsertion
from FarInsertion import FarInsertion
from Genetic import Genetic
import random
import os

#__main__

#récupération du chemin absolu pour le nom de fichier
folder = os.path.dirname(os.path.abspath(__file__))
citiesPath = os.path.join(folder, 'files/villes.tsp')
namesPath = os.path.join(folder, 'files/noms.csv')
#imagePath = os.path.join(folder, 'images/carte-cote-d-or.png')

#création de la première tournée (de 0 à 66)
t0 = Heuristic(citiesPath, namesPath).getTour()

#test distance entre ville 1 et ville 2
print("Distance entre la ville 1 et 2")
print(t0[0].distance(t0[1]))

#création d'un algorithme
algo = Algorithm(t0)

#affichage coût tournée 0
print("Tournée croissante")
print(algo.__str__())

t1 = list(t0)

#création d'une autre tournée (aléatoire)
algo.execute()
#affichage test
#for city in t1:
#    print(city.__str__())

#affichage du coût
print("Tournée aléatoire")
print(algo.__str__())

close = CloseNeighbor(t1)
near = NearInsertion(t1)
far = FarInsertion(t1)
genetic = Genetic(t1)

#CloseNeighbor
print("Tournée avec l'algorithme du proche voisin")
close.execute()
print(close.__str__())

#NearInsertion
print("Tournée avec l'algorithme de l'insertion proche")
near.execute()
print(near.__str__())

#FarInsertion
print("Tournée avec l'algorithme de l'insertion loin")
far.execute()
print(far.__str__())

#Algo génétique
print("Tournée avec l'algorithme génétique")
genetic.execute()
print(genetic.__str__())

#Application graphique
window = Application(t1)