#imports
import random
import copy
from Algorithm import Algorithm
from CloseNeighbor import CloseNeighbor
from NearInsertion import NearInsertion
from FarInsertion import FarInsertion

class Genetic(Algorithm):
    """ Représente un algorithme génétique """

    def __init__(self, tour):
        """ Initialise l'algorithme """
        Algorithm.__init__(self, tour)

    def execute(self):
        """ Exécute l'algorithme génétique return la meilleure tournée trouvée"""
        # -- déclaration de variables --
        #génération courante
        generation = 0
        #nombre d'individus dans une population
        n = 150#meilleure solution trouvée avec 150
        #nombre d'individu généré au début
        x = 800
        #nombre de générations maximum
        nGeneration = 100 #100 meilleure solution trouvée
        #nombre de mutations des enfants
        y = 65  #meilleure solution trouvée avec 80
        #point de croisement des deux tournées pour faire des enfants
        cross = 20

        # -- algorithme génétique --
        #initialisation de la population
        population = self.initPopulation(x)

        while generation < nGeneration:
            #première génération avec une population de x individus
            if generation == 0:
                population = self.removeDuplicate(population)
                parents = self.selectionRandom(population, n)
            else:
                parents = population
            #création des enfants
            childs = []
            for i in range(0, len(parents)):
                #croisement des parents
                c = self.crossTour(parents[i].getTour(), parents[len(parents)-1-i].getTour(), cross)
                childs = childs + c
            #mutation de y enfants
            childs = self.mutation(childs, y)  
            #sélection de n enfants 
            childs = self.selectionBetter(childs, n)
            #nouvelle population de parents et d'enfants
            newPopulation = parents + childs
            #sélection de n individus de la nouvelle population
            population = self.selectionTournament(newPopulation, n)
            generation += 1
            print(generation)
            print(Algorithm(self.bestTour(population)).__str__())
        #retourne la meilleure tournée
        self.tour = self.bestTour(population)
        
    def bestTour(self, population):
        """ Retourne la meilleure tournée """
        #initialisation
        costs = []
        tours = []
        #ajoute dans sa liste respective la tournée et le coût de l'algorithme
        for a in population:
            costs.append(a.cost())
            tours.append(a.getTour())
        #retourne la tournée avec le coût minimum
        return tours[costs.index(min(costs))]

    def initPopulation(self, x):
        """ Initialise la population en choisissant l'algorithme et en l'exécutant """
        #initialise la population
        population = []
        #pour avoir x individus
        for i in range(0, x):
            #pour choisir quel algorithme exécuter
            j = random.randint(0, 3)
            if j == 0:
                a = CloseNeighbor(self.tour)
            elif j == 1:
                a = NearInsertion(self.tour)
            elif j == 2:
                a = FarInsertion(self.tour)
            else:
                a = Algorithm(self.tour)
            #exécution
            a.execute()
            #ajout de l'algorithme exécuté à la population
            population.append(a)
        return population

    def selectionRandom(self, population, n):
        """ Sélectionne totalement aléatoirement des individus """
        #initialisation
        ordre = []
        #ajout de nombre aléatoire correspondant aux indices de population
        for i in range(0, len(population)):
            ordre.append(i)
        #mélange de la liste
        random.shuffle(ordre)
        newPopulation = []
        #ajouter les n premiers individus avec les indices de la liste ordre
        for i in range(0, n):
            newPopulation.append(population[ordre[i]])
        return newPopulation

    def selectionRoulette(self, population, n):
        """ Sélectionne aléatoirement en fonction de probabilités liés au coût """
        #initialisation
        proba = []
        newPopulation = []
        #calcul de probabilité d'être choisi en fonction de leur coût
        for a in population:
            proba.append((1/a.cost())*100)
        #tant que la nouvelle population n'a pas la longueur n souhaitée
        while len(newPopulation) < n:
            for i in range(0, n-1):
                #random choisissant la chance d'être choisi
                j = random.random()
                #ajout dans la nouvelle population si la chance est inférieure à la probabilité
                if j < proba[i]:
                    newPopulation.append(population[i])
        return newPopulation

    def selectionBetter(self, population, n):
        """ Garde les meilleurs individus """
        #trie la population en fonction de leur coût
        newPopulation  = sorted(population, key=lambda i: i.cost())
        #retourne la population triée jusqu'à n 
        return newPopulation[:n]

    def removeDuplicate(self, population):
        """ Enlève les individus de même coût """
        #initialisation
        newPopulation = []
        for i in range(1, len(population)-1):
            #regarde si les tournées adjacentes n'ont le même coût
            if population[i-1].cost() != population[i].cost() and population[i].cost() != population[i+1].cost():
                newPopulation.append(population[i])
        return newPopulation
    
    def selectionTournament(self, population, n):
        """ Sélection en tournoi de n individus attention il faut grande une population de 2n minimum"""
        #initialisation
        ordre = []
        for i in range(0, len(population)):
            ordre.append(i)
        #mélange
        random.shuffle(ordre)
        newPopulation = []
        #pour tous les i et i+1 des indices dans la liste ordre regarde quel algo à le meilleur coût et le garde
        for i in range(0, 2*n-1, 2):
            a1 = population[ordre[i]]
            a2 = population[ordre[i+1]]
            if a1.cost() < a2.cost():
                newPopulation.append(a1)
            else:
                newPopulation.append(a2)
        return newPopulation
    
    def mutation(self, childs, y):
        """ Effectue la mutation de y enfants """
        #initialisation
        ordre = []
        for i in range(0, len(childs)):
            ordre.append(i)
        #mélange
        random.shuffle(ordre)
        #effectue la mutation pour les y premiers individus d'indices de la liste ordre
        for i in range(0, y):
            #application d'une recherche locale
            childs[ordre[i]].amelioration2opt()
        return childs

    def crossTour(self, t1, t2, cross):
        """ Retourne une liste d'enfants créés à partir de deux tournées et un point de croisement """
        #coupe les tournées
        child1 = t1[:cross]
        child2 = t2[:cross]

        #initialisation
        childs = []
        i = cross
        for i in range(len(t1)):
            if t2[i] not in child1:
                child1.append(t2[i])
            if t1[i] not in child2:
                child2.append(t1[i])

        i = cross
        for i in range(len(t1)):
            if t1[i] not in child1:
                child1.append(t1[i])
            if t2[i] not in child2:
                child2.append(t2[i])

        #créer des algorithmes à partir des tournées créées
        a1 = Algorithm(child1)
        a2 = Algorithm(child2)
        #ajoute les algorithmes dans la liste des enfants
        childs.append(a1)
        childs.append(a2)
        #retourne la liste d'enfants
        return childs