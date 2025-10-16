import random
import colorama
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
    def __str__(self):
        return self.namn

def nytt_namn():
    namn = input("Ange ditt gladiator namn: ")
    return namn

def attackera(attack, attackerare, offer):
    skada = random.randint(7, 13)
    offer.ta_skada(skada)
    if offer.visa_hälsa() < 0:
        print(f"{colorama.Fore.RED}{attackerare} {colorama.Fore.RESET}attackerar {colorama.Fore.BLUE}{offer} {colorama.Fore.RESET}med {colorama.Fore.MAGENTA}{attack} {colorama.Fore.RESET}och {colorama.Fore.BLUE}{offer} {colorama.Fore.RESET}tar {colorama.Fore.WHITE}{skada} {colorama.Fore.RESET}skada ")
        print(f"{colorama.Fore.BLUE}{offer} {colorama.Fore.RESET}har nu {colorama.Fore.GREEN}{0} {colorama.Fore.RESET}hälsopoäng kvar")
    else:
        print(f"{colorama.Fore.RED}{attackerare} {colorama.Fore.RESET}attackerar {colorama.Fore.BLUE}{offer} {colorama.Fore.RESET}med {colorama.Fore.MAGENTA}{attack} {colorama.Fore.RESET}och {colorama.Fore.BLUE}{offer} {colorama.Fore.RESET}tar {colorama.Fore.WHITE}{skada} {colorama.Fore.RESET}skada ")
        print(f"{colorama.Fore.BLUE}{offer} {colorama.Fore.RESET}har nu {colorama.Fore.GREEN}{offer.visa_hälsa()} {colorama.Fore.RESET}hälsopoäng kvar")

    

fiende_lista = ["Maximus", "Gandalf", "Muskkkk"]
fiende_attack = ["Kast, Slag, Spark"]
strid = False

menu = True

while menu == True:
    print("Välkommen till Gladiatorerna!")
    spelar_namn = nytt_namn()
    fiende_namn = random.choice(fiende_lista)
    Gladiator1 = Gladiator(spelar_namn, 35, 10, 10)
    Gladiator2 = Gladiator(fiende_namn, 35, 10, 10)
    strid = True
    print("Striden har nu påbörjats!")
    print("")
    menu = False
    
while strid == True:
    print("Det är nu din tur!")
    print("")
    attack_typ = input("Attackera med Slag, Spark eller Kast: ").lower()
    # Kollar om attacken är korrekt eller inte genom att se om den tillhör listan. Kanske eventuellt gör en lista som beror på vapnet när jag lägger till det.
    while attack_typ not in ["slag", "spark", "kast"]:
        print("Du gjorde fel, försök igen!")
        attack_typ = input("Attackera med Slag, Spark eller Kast: ").lower()
    

    fiende_attack = random.choice(fiende_attack)
    print("═══════════════════════════════════════════════════════════════")
    attackera(attack_typ, Gladiator1, Gladiator2)
    if Gladiator2.visa_hälsa() <= 0:
        print(f"{colorama.Fore.YELLOW}Du vann!!")
        break
    print("═══════════════════════════════════════════════════════════════")
    print("Det är nu fiendens Tur!")
    print("═══════════════════════════════════════════════════════════════")
    attackera(attack_typ, Gladiator2, Gladiator1)
    if Gladiator1.visa_hälsa() <= 0:
        print(f"{colorama.Fore.CYAN}Du förlorade!!{colorama.Fore.RESET}")
        break
   
    print("")
    print("═══════════════════════════════════════════════════════════════")

    


