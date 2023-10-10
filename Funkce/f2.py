print("Ahoj světe")

def privitani_zakaznika(jmeno, vek):
    print()
    print("Vítám vás u nás v knihovně.")
    print("Jmenujete se " + jmeno + ", že?")
    print("Máte už naši průkazku?")
    if (vek > 17):
        print("Knihy pro dospělé jsou nahoře.")
    else:
        print("Knihy pro děti jsou dole.")
    print("Věšák na kabáty je vlevo.")

privitani_zakaznika("Novák", 25)
privitani_zakaznika("Červená", 12)
print("Vaše rezervace je připravena.")
privitani_zakaznika("Svoboda", 17)
privitani_zakaznika("Modrá", 44)

