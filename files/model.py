import pandas as pd
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
        pass

    def webMonth(self):
        pass

    def testCreator(self):
        print(self.entries)
        print(self.items)

    def testData(self):
        print(self.data)
