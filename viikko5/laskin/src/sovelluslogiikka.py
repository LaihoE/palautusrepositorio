class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.viime_tulos = 0

    def miinus(self, arvo):
        self.viime_tulos = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.viime_tulos = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.viime_tulos = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.viime_tulos = self.tulos
        self.tulos = arvo

    def kumoa(self):
        self.tulos = self.viime_tulos