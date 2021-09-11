tafelVan = input("Welke tafel wilt u? ")
hoeveelheid = input("Tot welk cijfer moet die tafel gaan? ")

for x in range(1, int(hoeveelheid) + 1):
    print(tafelVan + " * " + str(x) + " = " + str(int(tafelVan) * x))
