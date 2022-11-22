from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kaikki_ostokset = {}

    def tavaroita_korissa(self):
        total = 0
        for _, v in self.kaikki_ostokset.items():
            total += v.lukumaara()
        return total

    def hinta(self):
        total = 0
        for _, v in self.kaikki_ostokset.items():
            total += v.hinta()
        return total

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        if lisattava.nimi() not in self.kaikki_ostokset:
            self.kaikki_ostokset[lisattava.nimi()] = ostos
        else:
            self.kaikki_ostokset[lisattava.nimi()].muuta_lukumaaraa(1)


    def poista_tuote(self, poistettava: Tuote):
        ostos = self.kaikki_ostokset[poistettava.nimi()]
        ostos.muuta_lukumaaraa(-1)            

    def tyhjenna(self):
        self.kaikki_ostokset = {}

    def ostokset(self):
        kaikki = []
        for k,v in self.kaikki_ostokset.items():
            kaikki.append(v)
        return kaikki