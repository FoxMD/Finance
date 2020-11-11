class Encryption:
    inTab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    outTab ='NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678943210'

    def cryptHeader(self, header):
        newHeader = []
        for item in header:
            newItem = str(item).maketrans(self.inTab, self.outTab)
            newItem = item.translate(newItem)
            newHeader.append(newItem)
        return newHeader

    def cryptFile(self, line):
        keys = line.keys()
        items = line.values()
        newKeys = []
        newItems = []
        for key in keys:
            newKey = str(key).maketrans(self.inTab, self.outTab)
            newKey = key.translate(newKey)
            newKeys.append(newKey)

        for item in items:
            newItem = str(item).maketrans(self.inTab, self.outTab)
            newItem = item.translate(newItem)
            newItems.append(newItem)

        cline = dict(zip(newKeys, newItems))
        return cline

    def decryptFile(self, cline):
        dLine = []
        for item in cline:
            newItem = str(item).maketrans(self.outTab, self.inTab)
            newItem = item.translate(newItem)
            dLine.append(newItem)
        return dLine
