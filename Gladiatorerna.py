import random

class Gladiator:
    def __init__(self, namn, hälsa, styrka, snabbhet):
        self.namn = namn
        self.hälsa = hälsa
        self.styrka = styrka
        self.snabbhet = snabbhet
    
    def visa_namn(self):
        return self.namn

    def visa_hälsa(self):
        return self.hälsa
    
    def visa_styrka(self):
        return self.hälsa   
    
    def visa_snabbhet(self):
        return self.hälsa
    
Flamma = Gladiator("Flamma", 4, 8, 8)
Titus = Gladiator("Titus", 12, 3, 1)
Gaius = Gladiator("Gaius", 1, 20, 3, 100)
Gelidus = Gladiator("Gelidus", 20, 1, 1)
General = Gladiator("General", 100, 10, 1)
Fiende = Gladiator("Fiende", 100, 10, 1)


print(Flamma.visa_hälsa())

strid = True

while strid == True:
    attack = int(input("(1)Slå (2)Sparka (3)Kasta: "))
    if attack == 1:
        Fiende.hälsa -= General.styrka * random.randint(1, 1.5)
    
    print(Fiende.visa_hälsa)

strid = False

    


