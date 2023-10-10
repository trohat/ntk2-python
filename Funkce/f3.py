# není fajn, funkce dělá dvě věci zároveň (výpočet a tisk)

def vypocet_dane(prijmy, vydaje, sazba):
    dan = (prijmy - vydaje) * sazba / 100
    print("Vypočítaná daň je " + str(dan) + ".")

vypocet_dane(70000, 30000, 15)


