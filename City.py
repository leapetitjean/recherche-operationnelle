#imports
import math

class City:
    """Représente une ville avec son numéro, son nom et ses coordonnées"""
    
    def __init__(self, num, x, y): 
        self.num = num
        self.name = num
        self.x = x
        self.y = y
        self.visit = False

    def __str__(self):
        return str(self.num) + " " + str(self.name) + " " + str(self.x) + " " + str(self.y)

    def setName(self, name):
        self.name = name

    def setVisit(self, value):
        self.visit = value
    
    def getNum(self):
        return self.num
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getVisit(self):
        return self.visit

    def getName(self):
        return self.name

    def distance(self, city):
        """Retourne la distance avec la deuxième ville"""
        return 100 * math.sqrt(((city.getX()-self.getX())**2)+((city.getY()-self.getY())**2))

    def closestCityNotVisited(self, cities):
        """Retourne la ville non visitée la plus proche"""
        distances = []
        citiesNotVisited = []

        for city in cities:
            if city.getVisit() == False:
                distances.append(self.distance(city))
                citiesNotVisited.append(city)

        return citiesNotVisited[distances.index(min(distances))]
    
    def closestCityBetween(self, anotherCity, cities):
        """Retourne la ville non visitée la moins loin des deux villes"""
        distances = []
        citiesNotVisited = []
        for city in cities:
            if city.getVisit() == False:
                distances.append(min(self.distance(city),anotherCity.distance(city)))
                citiesNotVisited.append(city)
        return citiesNotVisited[distances.index(min(distances))]

    def farthestCityNotVisited(self, cities):
        """Retourne la ville non visitée la plus loin"""
        distances = []
        citiesNotVisited = []
       
        for city in cities:
            if city.getVisit() == False:
                distances.append(self.distance(city))
                citiesNotVisited.append(city)
                
        return citiesNotVisited[distances.index(max(distances))]

    def farthestCityBetween(self, anotherCity, cities):
        """Retourne la ville non visitée la moins loin des deux villes"""
        distances = []
        citiesNotVisited = []

        for city in cities:
            if city.getVisit() == False:
                distances.append(self.distance(city)+anotherCity.distance(city))
                citiesNotVisited.append(city)
        
        return citiesNotVisited[distances.index(max(distances))]