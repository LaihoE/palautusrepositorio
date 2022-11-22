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
        return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        if lisattava.nimi() not in self.kaikki_ostokset:
            self.kaikki_ostokset[lisattava.nimi()] = ostos
        else:
            self.kaikki_ostokset[lisattava.nimi()].muuta_lukumaaraa(1)


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse
        #   JA kuinka monta kappaletta kyseistä tuotetta korissa on