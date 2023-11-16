class Szoba:
    def __init__(self,szobaszam:int,agyszam,ar: int,foglalt=False, extrak=[]):
        self.szobaszam=szobaszam
        self.agyszam=agyszam
        self.ar=ar
        self.foglalt=foglalt
        self.extrak=extrak

class Szalloda:
    def __init__(self):
        self.szobak=[]

    def adatok_feltoltese(self):
        # Példa adatfeltöltés
        self.szobak.append(Szoba(szobaszam=101,agyszam=1, ar=100, extrak=['TV', 'Wifi']))
        self.szobak.append(Szoba(szobaszam=102,agyszam=2, ar=120, extrak=['Reggeli', 'Légkondi']))
        self.szobak.append(Szoba(szobaszam=201,agyszam=3, ar=150, extrak=['Jacuzzi', 'Wifi']))
        self.szobak.append(Szoba(szobaszam=201, agyszam="Lakosztály", ar=150, extrak=['Jacuzzi', 'Wifi']))

    def foglalas_leadasa(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam and not szoba.foglalt:
                szoba.foglalt = True
                print(f"Sikeres foglalás a(z) {szobaszam}. szobára.")
                return
        print(f"A(z) {szobaszam}. szoba már foglalt vagy nem létezik.")

    def arak_lekerdezese(self):
        for szoba in self.szobak:
            print(f"{szoba.szobaszam}. ágyszám { szoba.agyszam} szoba ára: {szoba.ar} Ft/éjszaka")

szalloda = Szalloda()
szalloda.adatok_feltoltese()

while True:
    print("\n1. Foglalás leadása")
    print("2. Árak lekérdezése")
    print("0. Kilépés")

    valasztas = input("Válassz egy menüpontot: ")

    if valasztas == "1":
        szobaszam = int(input("Add meg a foglalni kívánt szoba számát: "))
        szalloda.foglalas_leadasa(szobaszam)
    elif valasztas == "2":
        szalloda.arak_lekerdezese()
    elif valasztas == "0":
        break
    else:
        print("Érvénytelen választás. Kérlek, válassz újra.")