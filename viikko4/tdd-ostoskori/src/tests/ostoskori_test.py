import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_jalkeen_hinta_sama_kun_tuotteen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisaaminen_kaksi_tuotetta_korissa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        maito = Tuote("banaani", 2)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        maito = Tuote("banaani", 2)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 5)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostokset_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_ostokset_oikea_nimi_ja_n_yksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].tuote.nimi(), "Maito")
        self.assertEqual(len(ostokset), 1)

    def test_kahden_eri_tuotteen_lisaaminen_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        maito = Tuote("banaani", 2)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 2)
    
    def test_ostos_maara_pysyy_yksi_kun_kaksi_samaa_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_sama_nimi_ja_n_2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.ostokset()[0].tuote.nimi(), "Maito")
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        

    def test_kaksi_samaa_tuotetta_poista_yksi_tuotteita_yksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
