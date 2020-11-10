import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from docx import Document
from docx.shared import Inches


class DataModel(object):
    def __init__(self, e, i):
        self.entries = e
        self.items = i
        self.data = []
        self.activeEntry = ''
        self.income = 0.0
        self.outcome = 0.0
        self.pieData = {}

        self.incomeText = 'Prijem'

    def plotPie(self, dataIn):
        self.pieData = {key: val for key, val in dataIn.items() if val != 0.0}
        if self.incomeText in self.pieData:
            self.pieData[self.incomeText] = self.pieData[self.incomeText] - self.outcome

        _fig, ax = plt.subplots(figsize=(10, 4), subplot_kw=dict(aspect="equal"))
        data = list(self.pieData.values())
        keys = list(self.pieData.keys())
        wedges, _texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)
        labels = [x.split()[-1] for x in keys]

        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1) / 2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(keys[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                        horizontalalignment=horizontalalignment, **kw)

        ax.legend(wedges, labels, title='Type', loc='center left', bbox_to_anchor=(-1.0, 0, 0.5, 1))
        ax.set_title("Months summary", loc='left')
        return plt

    def setData(self, data):
        self.data = data

    def setActiveEntry(self, entry):
        self.activeEntry = entry

    def showGraph(self):
        inputData = self.preprocessDataForPie()
        graph = self.plotPie(inputData)
        graph.show()

    def printSummary(self):
        plt.clf()
        memfile = BytesIO()
        inputData = self.preprocessDataForPie()
        figure = self.plotPie(inputData)
        figure.savefig(memfile)

        document = Document()
        document.add_heading('Report', 0)
        document.add_picture(memfile, width=Inches(7.75))

        document.save('./reports/report.docx')
        memfile.close()
        pass

    def preprocessDataForPie(self):
        inputData = {}
        for item in self.items:
            inputData[item] = 0.0
        for item in self.data:
            if 'Price EUR' not in item:
                try:
                    inputData[item[0]] += float(item[2])
                except KeyError:
                    print('key not found')
        for key in inputData.keys():
            if self.incomeText not in key:
                self.outcome += inputData[key]
        return inputData

    def showSummary(self):
        pass

    def webMonth(self):
        pass

    def setIncomeText(self, text):
        self.incomeText = text

    def getIncomeText(self):
        return self.incomeText

    def testCreator(self):
        print(self.entries)
        print(self.items)

    def testData(self):
        print(self.data)
