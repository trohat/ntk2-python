
def vypocet_dane(prijmy, vydaje, sazba):
    dan = (prijmy - vydaje) * sazba / 100
    return dan



print(vypocet_dane(70000, 30000, 15))

vypocitana_dan = vypocet_dane(1000000, 700000, 15)
