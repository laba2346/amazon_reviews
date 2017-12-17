class Word:
    #See documentation (mrc2.doc) for more information regarding each score
    def __init__(self, nlet, nphon, nsyl, kffreq, kfcats, kfsamps, tlfreq, bfreq,
    fam, conc, imag, meanc, meanp, aoa):
        self.nlet = nlet
        self.nphon = nphon
        self.nsyl = nsyl
        self.kffreq = kffreq
        self.kfcats = kfcats
        self.kfsamps = kfsamps
        self.tlfreq = tlfreq
        self.bfreq = bfreq
        self.fam = fam
        self.conc = conc
        self.imag = imag
        self.meanc = meanc
        self.meanp = meanp
        self.aoa = aoa

    def printAll(self):
        print("{} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.nlet,
            self.nphon, self.nsyl, self.kffreq, self.kfcats,
            self.kfsamps, self.tlfreq, self.bfreq, self.fam, self.conc,
            self.imag, self.meanc, self.meanp, self.aoa))
