class Encryption:
    intab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    outtab ='NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

    def cryptHeader(self, header):
        newheader = []
        for item in header:
            newitem = str(item).maketrans(self.intab, self.outtab)
            newitem = item.translate(newitem)
            newheader.append(newitem)
        return newheader

    def cryptFile(self, line):
        keys = line.keys()
        items = line.values()
        newkeys = []
        newitems = []
        for key in keys:
            newkey = str(key).maketrans(self.intab, self.outtab)
            newkey = key.translate(newkey)
            newkeys.append(newkey)

        for item in items:
            newitem = str(item).maketrans(self.intab, self.outtab)
            newitem = item.translate(newitem)
            newitems.append(newitem)

        cline = dict(zip(newkeys, newitems))
        print(cline)
        return cline

    def decryptFile(self, cline):
        trantab = cline.maketrans(self.outtab, self.intab)
        dline = cline.translate(trantab)
        return dline
