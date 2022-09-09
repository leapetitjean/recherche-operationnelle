# Recherche Opérationnelle - Voyageur de commerce

 Projet de deuxième année d'IUT essayant de résoudre un problème de voyageur de commerce sur une instance précise.
 Le projet dispose d'une visualisation, le fichier `main.py` sert à lancer l'interface.
 
 Plusieurs algorithmes de recherche de solution initiale sont disponibles :
 * aléatoire
 * plus proche voisin
 * insertion loin
 
 Plusieurs algorithmes d'amélioration, recherche locale :
 * 2-opt
 * échange de villes consécutives
 * échange des villes consécutives qui donne le meilleur coût
 * échange de villes non consécutives
 * échange de villes non consécutives qui donne le meilleur coût
 
 L'algorithme le plus conséquent est l'algorithme génétique. 
 Ce dernier dispose de plusieurs mécanisme de sélection de la population :
 * sélection aléatoire
 * sélection roulette (aléatoire avec des probabilités liées au coût)
 * sélection des meilleurs
 * sélection par tournois

# Operations Research - Travelling Salesman Problem

Second year project at the Institute of Technology that solves the travelling salesman problem on a specific instance. The project has an interface and the `main.py` file launches it. 

Several algorithms for finding the first solution are available :
* random
* closestNeighbors
* farthestInsertion

Several local search algortihms are available :
* 2-opt
* exchange of consecutive cities
* exchange of consecutive cities which gives the best cost
* exchange of non-consecutive cities
* exchange of non-consecutive cities which gives the best cost

The largest algorithm is the genetic algorithm.
It has several population selection mechanisms :
* random selection
* roulette selection
* best-of selection
* tournament selection
