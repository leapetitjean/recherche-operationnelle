# Recherche Opérationnelle - Voyageur de commerce

 Projet de deuxième année d'IUT essayant de résoudre un problème de voyageur de commerce sur une instance précise.
 Le projet dispose d'une visualisation, le fichier `main.py` sert à lancer l'interface.
 
 Plusieurs algorithmes de recherche de solution initiale sont disponibles :
 * plus proche voisin
 * insertion loin
 * 
 
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
