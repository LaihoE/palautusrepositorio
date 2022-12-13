from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from tekoaly import Tekoaly


class KiviPaperiSakset:
    def __init__(self, kps_tyyppi) -> None:
        self.kps_tyyppi = kps_tyyppi
        self.tuomari = Tuomari()
        if self.kps_tyyppi == "b":
            self.tekoaly = Tekoaly()
        elif self.kps_tyyppi == "c":
            self.tekoaly = TekoalyParannettu(10)
        else:
            self.tekoaly = None

    def pelaa(self):
        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)
            if not (self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto)):
                break
            else:
                self.tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
                print(self.tuomari)
        print("Kiitos!")
        print(self.tuomari)

    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    def _toisen_siirto(self, ensimmaisen_siirto):
        if self.kps_tyyppi == "a":
            return input("Toisen pelaajan siirto: ")
        elif self.kps_tyyppi == "b":
            return self.tekoaly.anna_siirto()
        elif self.kps_tyyppi == "c":
            return self.tekoaly.anna_siirto(ensimmaisen_siirto)
        else:
            return False

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
