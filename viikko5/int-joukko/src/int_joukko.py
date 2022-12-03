KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkioiden_lkm = 0
        self.luvut = set()

    def kuuluu(self, n):
        return n in self.luvut

    def lisaa(self, n):
        if n not in self.luvut:
            self.alkioiden_lkm += 1
        self.luvut.add(n)

    def poista(self, n):
        self.luvut.remove(n)
        self.alkioiden_lkm -= 1

    def kopioi_taulukko(self, a, b):
        a = list(self.luvut)
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return list(self.luvut)

    @staticmethod
    def yhdiste(a, b):
        ij = IntJoukko()
        ij.luvut = a.luvut.union(b.luvut)
        return ij

    @staticmethod
    def leikkaus(a, b):
        ij = IntJoukko()
        ij.luvut = a.luvut.intersection(b.luvut)
        return ij

    @staticmethod
    def erotus(a, b):
        ij = IntJoukko()   
        ij.luvut = a.luvut - b.luvut
        return ij

    def __str__(self):
        if len(self.luvut) == 0:
            return "{}"
        return str(self.luvut)
