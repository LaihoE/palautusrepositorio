import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

    
    def test_lisaa_tuotteita_koriin(self):
        t = Tuote("banaani", 69)
        self.kori.lisaa_tuote(t)
        self.assertAlmostEqual(self.kori.kaikki_ostokset["banaani"].lukumaara(), 1)

    def test_poista_korista(self):
        t = Tuote("banaani", 69)
        self.kori.lisaa_tuote(t)
        self.kori.poista_tuote(t)
        self.assertAlmostEqual(len(self.kori.kaikki_ostokset), 0)

 