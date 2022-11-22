import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def test_kortti_init_ok(self):
        m = Maksukortti(213)
        self.assertAlmostEqual(m.saldo, 213)

    def test_lataa_kortille(self):
        m = Maksukortti(213)
        m.lataa(5)
        self.assertAlmostEqual(m.saldo, 218)
    
    def test_osta_kortilla(self):
        m = Maksukortti(213)
        m.osta(5)
        self.assertAlmostEqual(m.saldo, 208)