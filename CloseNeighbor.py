#imports 
from Algorithm import Algorithm
from random import randint

class CloseNeighbor(Algorithm):
    """Représente un algorithme glouton du plus proche voisin"""

    def __init__(self, tour):
        Algorithm.__init__(self, tour)

    def execute(self):
        """ Exécute l'agorithme du plus proche voisin """
        #initialisation
        tour = []
        for city in self.tour:
            city.setVisit(False)
        #choix d'un point de départ aléatoire 
        s = self.tour[randint(0, len(self.tour)-1)]
        s.setVisit(True)
        tour.append(s)
        #tant que toutes les villes de la tournée ne sont pas visitées 
        while not self.allVisited():
            #choisis la ville la plus proche
            n = s.closestCityNotVisited(self.tour)
            n.setVisit(True)
            s = n
            #ajoute la ville dans la nouvelle tournée
            tour.append(s)
        #change la tournée par la nouvelle tournée
        self.tour = tour


