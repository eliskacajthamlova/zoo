# Popis programu
# Program počítá zvířata v zoo
# V zoo jsou tři druhy zvířat tygři, lvy a opice
# Program umožní uživateli provádět tři akce - přidat zvíře, odebrat zvíře a vypsat všechna zvířata
# Po jedné této akci se program automaticky zeptá jestli chce uživatel pokračovat


# Úkol
# Odkomentujte funkce
# Dopište funkce tak, aby fungoval celý program
# funkce pridej - má vstupní parametry zvire a počet - připočte k dané skupině tolik zvířat, kolik zadá uživatel(pocet)
# (pokud uživatel zadá neplatné zvíře vypíše se mu: "Neco si zadal špatně")
# funkce odeber - má vstupní parametry zvire a počet - odečte od dané skupiny tolik zvířat, kolik zadá uživatel(pocet)
# (pokud zadá neplatné zvíře, nebo bude chtít odbrat více zvířat než je aktuálně v zoo vypíše se mu: "Neco si zadal špatně")
# funkce vypis - vypíše všechna zvířata, která jsou aktuálně v zoo


# Tuto část dopiš
zoo = {"tygr": 0, "lev": 0, "opice": 0}

#def pridej(zvire, pocet):
def pridej(zvire, pocet):
    if zvire in zoo and pocet > 0 :
        zoo[zvire] += pocet
    else:
        print("neco je spatnee")
    
#def odeber(zvire, pocet):
def odeber(zvire, pocet):
    if zvire in zoo and 0 < pocet <= zoo[zvire]:
        zoo[zvire] -= pocet
    else:
        print("neco je opet spatne")
    
#def vypis():
def vypis():
    print("zvirata v zoo:")
    for zvire, pocet in zoo. items():
        print(f"{zvire}: {pocet}")

while True:
    print("n1 - pridat zvire n2 - odebrat zvire n3 - vypsat zvirata n4 - konec")
    volba = input("vvyber akci:")

if volba == "1":
    zvire = input("zadej zvire(tygr,lev,opice):")
    pocetzvirat = int(input("zadej pocet:"))
    pridej(zvire, pocet)

elif == volba "2":
    zvire = input("zadej zvire(tygr,lev,opice):").strip().lower()
    pocet = int(input("zadej pocet:"))
    odeber(zvire, pocet)

elif volba == "3":
    vypis()

elif volba == "4":
    print("ukoncuji program.")
    break

else:
    print("neplatna volba, zkus to znovu.")


    

# Tuto část nepřepisovat

# Počty zvířat v zoo
tygri = 0
lvy = 0
opice = 0

# informace pro cyklus zda se má opakovat či ne
opakovat = "ano"


while(opakovat=="ano"):

    # výpis akcí co lze provádět 
    print("Vyberte jednu z akcí(pište pouze číslo): ")
    print("1. přidat zvíře")
    print("2. odebrat zvíře")
    print("3. vypsat seznam zvířat")

    #načtení akce od uživatele
    cislo = int(input())
    
    #Jednotlivá načtení potřebných informací a volání funkce
    if cislo==1:
        zvire = input("Zadejte zvířata která chcete přidat(tygri,lvy,opice)")
        pocet = int(input("Zadejte počet těchto zvířat"))
        pridej(zvire,pocet)
    elif cislo==2:
        zvire = input("Zadejte zvířata která chcete přidat(tygri,lvy,opice)")
        pocet = int(input("Zadejte počet těchto zvířat"))
        odeber(zvire,pocet)
    elif cislo==3:
        vypis()

    # update proměnné opakovat, aby nedošlo k zacyklení programu
    opakovat = input("Chcete opakovat program?(ano/ne)")
