"""teplota1 = 19
teplota2 = 18
teplota3 = 20
teplota4 = 15
teplota5 = 15
teplota6 = 14"""

teploty = [19, 18, 20, 15, 15, 14]
teploty.append(16)
teploty.append(17)

autori = ["Tolkien", "Herbert", "Sapkowski", "Pratchett", "May"]
autori[2]

autori[1:5]
autori[:3]
autori[1:5:2]
# funguje to takhle: (start:stop:step)

autori[::-1]
teploty.count(15)
autori.index("May")


for spisovatel in autori:
    print("V naší knihovně máme knihy od autora jménem " + spisovatel)
    print("Chcete si od něj něco přečíst?")
    print()



