import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class DataModel(object):
    def __init__(self, e, i):
        self.entries = e
        self.items = i
        self.data = []
        self.activeEntry = ''
        self.income = 0.0
        self.outcome = 0.0

    def setData(self, data):
        self.data = data
        print(self.data)

    def setActiveEntry(self, entry):
        self.activeEntry = entry
        print(entry)

    def showGraph(self):
        pass

    def printSummary(self):
        pass

    def showSummary(self):
        inputData = {}
        for item in self.items:
            inputData[item] = 0.0
        print(inputData)
        for item in self.data:
            print(item)
            if 'Price EUR' not in item:
                print(item)
                try:
                    inputData[item[0]] += float(item[2])
                except KeyError:
                    print("Key doesnt exist")
        print(inputData)
        self.income = inputData['Prijem']
        for key in inputData.keys():
            if 'Prijem' not in key:
                self.outcome += inputData[key]
        print(self.income)
        print(self.outcome)
        labels = inputData.keys()
        sizes = inputData.values()
        plt.pie(sizes, labels=labels)
        plt.show()

    def webMonth(self):
        pass

    def testCreator(self):
        print(self.entries)
        print(self.items)

    def testData(self):
        print(self.data)
