import random

# skapar klassen Gladiator

class Gladiator:
    def __init__(self, namn, hälsa, styrka, snabbhet):
        #Namn, hälsa, styrka och snabbhet
        self.namn = namn
        self.hälsa = hälsa
        self.styrka = styrka
        self.snabbhet = snabbhet
    # metod som ger namnet
    def visa_namn(self):
        return self.namn

    # metod som ger hälsan
    def visa_hälsa(self):
        return self.hälsa
    
    # metod som ger styrkan
    def visa_styrka(self):
        return self.styrka   

    # metod som ger skadan
    def ta_skada(self, skada):
        self.hälsa -= skada

    # metod som ger snabbheten
    def visa_snabbhet(self):
        return self.snabbhet
Gladiator1 = Gladiator("Kämpe", 100, 10, 10)
Gladiator2 = Gladiator("Fiende", 100, 10, 10)

strid = True

while strid == True:
    attack = input("(1)Slå (2)Sparka (3)Kasta: ")
    fiende_attack = str(random.randint(1,3))


    if attack == "1":
        Gladiator2.ta_skada(Gladiator1.styrka)
        print(f"Du attackerar fienden med ett slag och den tar " + str(Gladiator1.visa_styrka()) + " skada ")
        print(f"Fienden har nu " + str(Gladiator2.visa_hälsa()) + " kvar.")
        print(Gladiator2.visa_hälsa())

    elif attack == "2":
        Gladiator2.ta_skada(Gladiator1.styrka)
        print(f"Du attackerar fienden med en spark och den tar " + str(Gladiator1.visa_styrka()) + " skada ")
        print(f"Fienden har nu " + str(Gladiator2.visa_hälsa()) + " kvar.")
        print(Gladiator2.visa_hälsa())
    
    elif attack == "3":
        Gladiator2.ta_skada(Gladiator1.styrka)
        print(f"Du attackerar fienden med ett kast och den tar " + str(Gladiator1.visa_styrka()) + " skada ")
        print(f"Fienden har nu " + str(Gladiator2.visa_hälsa()) + " hälsa kvar.")
        print(Gladiator2.visa_hälsa())
    else:
        print("Du skrev fel, gå vidare till nästa runda")
        continue
    
    if fiende_attack == "1":
        Gladiator1.ta_skada(Gladiator2.styrka)
        print(f"Fienden attackerar dig med ett slag och du tar " + str(Gladiator2.visa_styrka()) + " skada ")
        print(f"Fienden har nu " + str(Gladiator1.visa_hälsa()) + " kvar.")
        print(Gladiator1.visa_hälsa())

    elif fiende_attack == "2":
        Gladiator1.ta_skada(Gladiator2.styrka)
        print(f"Fienden attackerar dig med en spark och du tar " + str(Gladiator1.visa_styrka()) + " skada ")
        print(f"Du har nu " + str(Gladiator1.visa_hälsa()) + " kvar.")
        print(Gladiator1.visa_hälsa())
    
    elif fiende_attack == "3":
        Gladiator1.ta_skada(Gladiator2.styrka)
        print(f"Fienden attackerar dig med ett kast och du tar " + str(Gladiator1.visa_styrka()) + " skada ")
        print(f"Du har nu " + str(Gladiator1.visa_hälsa()) + " hälsa kvar.")
        print(Gladiator1.visa_hälsa())



    if Gladiator2.visa_hälsa() <= 0:
        print("Du vann!!")
        strid = False
    elif Gladiator1.visa_hälsa() <= 0:
        print("Du förlorade!!")
        strid = False
    


