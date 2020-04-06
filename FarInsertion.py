#imports 
from Algorithm import Algorithm
from random import randint

class FarInsertion(Algorithm):
    """Représente un algorithme glouton d'insertion loin"""

    def __init__(self, tour):
        Algorithm.__init__(self, tour)

    def execute(self):
        #initialisation
        tour = []
        for city in self.tour:
            city.setVisit(False)
        #choix d'un point de départ aléatoire 
        c1 = self.tour[randint(0,len(self.tour)-1)]
        c1.setVisit(True)
        tour.append(c1)
        #ville la plus éloignée
        c2 = c1.farthestCityNotVisited(self.tour)
        c2.setVisit(True)
        tour.append(c2)
        #tant que toutes les villes ne sont pas visités
        while not self.allVisited():            
            for i in range(0, len(tour)):
                #choisi la ville la plus loin
                c = tour[i].farthestCityNotVisited(self.tour)
                d = tour[i].distance(c)
                #si c'est la première itération
                if i == 0:
                    n = c
                    dMax = tour[i].distance(c)
                    j = i+1
                else:
                    #si la distance est supérieure à la distance max
                    if d > dMax:
                        n = c
                        dMax = tour[i].distance(c)
                        j = i+1

            n.setVisit(True)
            #insérer j dans la tournée
            tour.insert(j, n)

        self.tour = tour