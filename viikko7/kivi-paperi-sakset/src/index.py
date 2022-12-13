from kps import KiviPaperiSakset

def main():
    ok = ["a", "b", "c"]
    while True:
        vastaus = input("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan\n"
              )
        if vastaus in ok:
            kps = KiviPaperiSakset(vastaus)
            kps.pelaa()
        else:
            break

if __name__ == "__main__":
    main()
