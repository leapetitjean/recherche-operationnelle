#imports 
import random
import copy

class Algorithm():
    """Représente un algorithme avec une tournée de villes"""

    def __init__(self, tour):
        """Initialise l'algorithme avec une tournée"""
        self.tour = tour

    def execute(self):
        """Mélange aléatoirement la tournée"""
        random.shuffle(self.tour)

    def __str__(self):
        """Retourne la tournée en str et son coût"""
        result = "["
        for i in range(0, len(self.getTour())-1):
            result += (str(self.getTour()[i].getNum()) + ',')
        result += (str(self.getTour()[len(self.getTour())-1].getNum())+"]\nCoût : " + str(self.cost()))
        return result

    def setTour(self, tour):
        """Change la tournée"""
        self.tour = tour

    def getTour(self):
        """Retourne la tournée"""
        return self.tour

    def cost(self):
        """ Retourne le coût de la tournée"""
        cost = 0
        for i in range(0, len(self.tour)-1):
                cost += self.tour[i].distance(self.tour[i+1])
        cost += self.tour[0].distance(self.tour[len(self.tour)-1])
        return cost

    def allVisited(self):
        """ Vérifie si toutes les villes de la tournée sont visitées """
        #initialisation
        result = True
        sortie = False
        i = 0
        #tant qu'une condition de sortie n'est pas remplie
        while sortie == False:
            #si toutes les villes sont visitées
            if i > len(self.tour)-1:
                sortie = True
            #si une ville n'est pas encore visitée
            elif self.tour[i].getVisit() == False:
                sortie = True
                result = False
            else:
                i += 1
        return result

    def consecutiveNeighborhood(self):
        """ Echange deux villes consécutives si le coût de la tournée est inférieur """
        #initialisation
        amelioration = False
        better = True
        #tant qu'une meilleure solution est trouvée
        while better:
            better = False
            for i in range(0, len(self.tour)-1):
                tour = copy.copy(self.tour)
                #échange les villes i et i+1
                temp = tour[i]
                tour[i] = tour[i+1]
                tour[i+1] = temp
                #créer un algo avec la nouvelle tournée
                algo = Algorithm(tour)
                #vérifie si le coût de la nouvelle tournée est inférieur au coût de la tournée actuelle
                if algo.cost() < self.cost():
                    #remplace la tournée actuelle par la nouvelle tournée
                    self.tour = tour
                    better = True
                    amelioration = True
            #vérifie la même chose mais pour l'échange entre la première et la dernière ville
            tour = copy.copy(self.tour)
            temp = tour[0]
            tour[0] = tour[len(tour)-1]
            tour[len(tour)-1] = temp
            algo = Algorithm(tour)
            if algo.cost() < self.cost():
                self.tour = tour
                better = True
                amelioration = True
        #retourne si l'algorithme a effectué une amélioration ou non
        return amelioration

    def betterConsecutiveNeighborhood(self):
        """ Echange les villes consécutives qui donne le meilleur coût """
        #initialisation
        amelioration = False
        better = True
        while better:
            better = False
            for i in range(0, len(self.tour)-1):
                tour = copy.copy(self.tour)
                temp = tour[i]
                tour[i] = tour[i+1]
                tour[i+1] = temp
                if i==0:
                    best = self
                algo = Algorithm(tour)
                #regarde si le nouvel algo a un coût inférieur au meilleur pour l'instant
                if algo.cost() < best.cost():
                    best = algo
                    better = True
                    amelioration = True
            #pareil mais pour la première et dernière ville
            tour = copy.copy(self.tour)
            temp = tour[0]
            tour[0] = tour[len(tour)-1]
            tour[len(tour)-1] = temp
            algo = Algorithm(tour)
            if algo.cost() < best.cost():
                best = algo
                better = True
                amelioration = True

            self.tour = best.getTour()
        #retourne si l'algorithme a effectué une amélioration ou non
        return amelioration

    def nonConsecutiveNeighborhood(self):
        """ Echange des villes non consécutives si le coût est inférieur """
        amelioration = False
        self.consecutiveNeighborhood()
        for i in range(0, len(self.tour)):
            for j in range(0, len(self.tour)):
                #échange les villes i et j
                tour = copy.copy(self.tour)
                temp = tour[i]
                tour[i] = tour[j]
                tour[j] = temp
                #créer un algorithme
                algo = Algorithm(tour)
                #vérifie si le coût est inférieur 
                if algo.cost() < self.cost():
                    self.tour = tour
                    amelioration = True
             #retourne si l'algorithme a effectué une amélioration ou non
            return amelioration
    
    def betterNonConsecutiveNeighborhood(self):
        """ Echange les villes non consécutives qui donne le meilleur coût """
        #initialisation
        amelioration = False
        better = True
        while better:
            better = False
            for i in range(0, len(self.tour)):
                for j in range(0, len(self.tour)):
                    tour = copy.copy(self.tour)
                    temp = tour[i]
                    tour[i] = tour[j]
                    tour[j] = temp
                    if i==0 and j==0:
                        best = self
                    algo = Algorithm(tour)
                    if algo.cost() < best.cost():
                        best = algo
                        better = True
                        amelioration = True
            #échange la tournée par la meilleure tournée
            self.tour = best.getTour()
        #retourne si l'algorithme a effectué une amélioration ou non
        return amelioration

    def localResearch(self):
        """ Alterne les voisinages pour trouver la meilleure tournée """
        better = True
        while better:
            better = False
            if self.consecutiveNeighborhood(): 
                better = True
            elif self.betterConsecutiveNeighborhood():
                better = True
            elif self.nonConsecutiveNeighborhood():
                better = True
            elif self.betterNonConsecutiveNeighborhood():
                better = True
            elif self.amelioration2opt():
                better = True
                

    def amelioration2opt(self):
        """ Démèle les noeuds pour réduire le coût de la tournée """
        #initialisation
        amelioration = False
        better = True
        self.nonConsecutiveNeighborhood()
        while better:
            better = False
            n = len(self.tour)
            for i in range(0, n):
                for j in range(i+2, n):
                    #copie la tournée actuelle
                    tour = copy.copy(self.tour)
                    #si il y a des noeuds
                    if tour[i%n].distance(tour[j%n]) + tour[(i+1)%n].distance(tour[(j+1)%n]) < tour[i%n].distance(tour[(i+1)%n]) + tour[j%n].distance(tour[(j+1)%n]):
                        #échange
                        temp = tour[(i+1)%n]
                        tour[(i+1)%n] = tour[j%n]
                        tour[j%n] = temp
                        self.tour = tour
                        better = True
                        amelioration = True
        #retourne si l'algorithme a effectué une amélioration ou non
        return amelioration
