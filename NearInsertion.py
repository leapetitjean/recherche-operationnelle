#imports 
from Algorithm import Algorithm
from random import randint
from City import City

class NearInsertion(Algorithm):
    """Représente un algorithme glouton d'insertion proche"""

    def __init__(self, tour):
        Algorithm.__init__(self, tour)

    def execute(self):
        tour = []

        for city in self.tour:
            city.setVisit(False)
            
        #choix du point de départ aléatoire 
        c1 = self.tour[randint(0,len(self.tour)-1)]
        c1.setVisit(True)
        tour.append(c1)
    
        c2 = c1.farthestCityNotVisited(self.tour)
        c2.setVisit(True)
        tour.append(c2)
        
        while not self.allVisited():            
            for i in range(0, len(tour)):
                c = tour[i].closestCityNotVisited(self.tour)
                d = tour[i].distance(c)
                if i == 0:
                    n = c
                    dMin = tour[i].distance(c)
                    j = i+1
                else:
                    if d < dMin:
                        n = c
                        dMin = tour[i].distance(c)
                        j = i+1

            n.setVisit(True)
            tour.insert(j, n)

        self.tour = tour
