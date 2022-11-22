# testikoodi tänne jos tarvetta
from ostoskori import Ostoskori
from tuote import Tuote


o = Ostoskori()
t = Tuote("banaani", 69)
o.lisaa_tuote(t)
print(o.kaikki_ostokset["banaani"])
