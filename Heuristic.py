#imports
from City import City

class Heuristic():
    """Représente une heuristique"""
    def __init__(self, citiesPath, namesPath):
        """Initialise la tournée à partir du chemin des fichiers donnés"""
        #récupération et initalisation des villes
        self.cities = []
        with open(citiesPath, "r") as file:
            for line in file.readlines():
                parts = line.split(" ")
                self.cities.append(City(int(parts[0]), float(parts[1]), float(parts[2])))
        file.close()

        #récupération du nom des villes
        names = []
        with open(namesPath, "r") as file:
            for line in file.readlines():
                parts = line.split(" ")
                names.append(parts[1])
        file.close()

        #ajout du nom aux villes existantes
        for i in range(0, len(self.cities)):
            self.cities[i].setName(names[i])

    def getTour(self):
        """Retourne la tournée obtenue à partir des fichiers"""
        return self.cities