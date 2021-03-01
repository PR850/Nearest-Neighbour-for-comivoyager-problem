import pandas as pd
import math
import os


class PrepareCitiesData:

    cities = pd.read_csv('cities.txt', sep=" ", header=0)
    citiesIndex = cities.index
    totalRows = len(citiesIndex)  # ilosc miast
    allDistances = {}  # dict ze wszystkimi miastami

    def calculateDistance(self, city, cityX, cityY, totalRows, cities):

        cityDistancesDict = {}
        for i in range(totalRows):
            if city != cities.at[i, 'city']:
                distance = math.sqrt(math.pow(cityX - float(
                    cities.at[i, 'x']), 2)+math.pow(cityY - float(
                        cities.at[i, 'y']), 2))
                cityDistancesDict[str(cities.at[i, 'city'])] = distance
        return cityDistancesDict

    def putAllInstancesIntoDict(self):
        for k in range(self.totalRows):
            distance = self.calculateDistance(str(self.cities.at[k, 'city']), float(
                self.cities.at[k, 'x']), float(self.cities.at[k, 'y']), self.totalRows, self.cities)
            self.allDistances[str(self.cities.at[k, 'city'])] = distance


class Dijkstry:
    path = []
    pathLength = 0.0

    def __init__(self, start, preparedCitiesData):
        self.start = start
        self.preparedCitiesData = preparedCitiesData

    def shortestPath(self):
        for i in range(preparedCitiesData.totalRows-1):
            shortestPath = min(
                preparedCitiesData.allDistances[self.start], key=preparedCitiesData.allDistances[self.start].get)
            preparedCitiesData.allDistances[self.start]
            self.pathLength = self.pathLength + \
                preparedCitiesData.allDistances[self.start][shortestPath]
            self.path.append(shortestPath)

            for key in preparedCitiesData.allDistances:
                preparedCitiesData.allDistances[key].pop(self.start, None)
            self.start = shortestPath


while True:
    try:
        preparedCitiesData = PrepareCitiesData()
        preparedCitiesData.putAllInstancesIntoDict()
        preparedCitiesDataCopy = preparedCitiesData.allDistances.copy()
        citiesList = preparedCitiesData.cities["city"].tolist()

        print("      ***      Nearest Neighbour for comivoyager problem      ***  ")
        print("Available cities: ", citiesList)
        startingPoint = input("Starting city: ")

        if startingPoint not in citiesList:
            while startingPoint not in citiesList:
                startingPoint = input(
                    "Wrong city name, input right city name: ")

        travel = Dijkstry(startingPoint, preparedCitiesDataCopy)
        travel.path.append(startingPoint)
        travel.shortestPath()

        travel.pathLength = travel.pathLength + \
            preparedCitiesData.allDistances[startingPoint][travel.path[-1]]
        travel.path.append(startingPoint)

        print("\nOrder of visits: ", travel.path)
        print("Length of path: ", travel.pathLength)
        input("\nClick Enter to finish...")
        break
    except:
        a = input("Wrong cities data\n\nInput cities to open cities.txt\nInput readme to open Readme wprowadz: readme\nClick Enter to finish program\n")
        if a == 'cities':
            os.system('cities.txt')
            break
        elif a == 'readme':
            os.system('Readme.txt')
            break
        else:
            break
