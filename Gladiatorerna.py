import random
import colorama
# skapar klassen Gladiator

class Gladiator:
    def __init__(self, namn, hälsa, snabbhet, mod, vapen):
        #Namn, hälsa, styrka och snabbhet
        self.namn = namn
        self.hälsa = hälsa
        self.snabbhet = snabbhet
        self.mod = mod
        self.vapen = vapen
    # metod som ger namnet
    def visa_namn(self):
        return self.namn

#kom ihåg att spela Domina

    def visa_vapen(self):
        return self.vapen

    def visa_mod(self):
        return self.mod

    def addera_mod(self, tal):
        self.mod += tal
        
    # metod som ger hälsan
    def visa_hälsa(self):
        return self.hälsa
    

    # metod som ger skadan
    def ta_skada(self, skada):
        self.hälsa -= skada

    # metod som ger snabbheten
    def visa_snabbhet(self):
        return self.snabbhet

    def __str__(self):
        return self.namn

#funktion som ber om ett namn och sedan skickar tillbaks namnet med return
class Vapen:
    def __init__(self, namn, skada, modgain, träffchans):
        self.vapen = namn
        self.skada = skada
        self.modgain = modgain
        self.träffchans = träffchans 
Spjut = Vapen("Spjut", random.randint(2,3), 1, 8)
Gladius = Vapen("Gladius", random.randint(3, 4), 1, 5)
Treudd_Net = Vapen("Treudd och Nät", 3, 1, 6)

fiende_lista = ["Maximus", "Gandalf", "Muskkkk"]
fiende_attack = ["Kast, Slag, Spark"]
vapen_lista = ["Spjut", "Gladius", "Treudd och Nät"]

def nytt_namn():
    namn = input("Ange ditt gladiator namn: ")
    return namn
#En funktion för att förkorta attacker, den har tre parametrar, attack som är attacken, attackerare ( den som ska göra skadan), offer(den som ska ta skadan)
def attackera(attackerare, offer):
    if random.randint(1,10) <= attackerare.vapen.träffchans:
        offer.ta_skada(attackerare.vapen.skada)
        if offer.hälsa < 0:
            offer.hälsa = 0
        print(f"{offer} tog {attackerare.vapen.skada} och har nu {offer.hälsa} hälsa kvar.")
    else:
        print(f"{attackerare}s attack missade")

def vapen_val():
    korrekta_svar = ["1", "2", "3"]
    print("Hej välj ett vapen till din Gladiator: ")
    print("(1) Ett mycket träffsäkert spjut.")
    print("(2) En gladius med stark karaktär.")
    print("(3) En pålitlig treudd och nät.")
    val = input("1? 2? 3?: ")
    if val == "1":
        vapen = Spjut
        return vapen
    elif val == "2":
        vapen = Gladius
        return vapen
    elif val == "3":
        vapen = Treudd_Net
        return vapen
    else:
        while val not in korrekta_svar:
            print("Du gjorde fel, välj igen.")
            print("(1) Ett mycket träffsäkert spjut")
            print("(2) En gladius med stark karaktär ")
            print("(3) En pålitlig treudd och nät")
            val = input("1? 2? 3?: ")

    

strid = False

menu = True

while menu == True:
    print("Välkommen till Gladiatorerna!")
    spelar_namn = nytt_namn()
    fiende_namn = random.choice(fiende_lista)
    Gladiator1 = Gladiator(spelar_namn, 35, 10, 0, vapen_val())
    Gladiator2 = Gladiator(fiende_namn, 35, 10, 0, Gladius)
    strid = True
    print("Striden har nu påbörjats!")
    print("")
    menu = False
    
while strid == True:
    print("Det är nu din tur!")
    print("")
    #attack_typ = input("Attackera med Slag, Spark eller Kast: ").lower()
    # Kollar om attacken är korrekt eller inte genom att se om den tillhör listan. Kanske eventuellt gör en lista som beror på vapnet när jag lägger till det.
   # while attack_typ not in ["slag", "spark", "kast"]:
        #print("Du gjorde fel, försök igen!")
        #attack_typ = input("Attackera med Slag, Spark eller Kast: ").lower()
        #fiende_val = random.choice(fiende_attack)
    attackera(Gladiator1, Gladiator2)
    if Gladiator2.visa_hälsa() <= 0:
        print(f"{colorama.Fore.YELLOW}Du vann!!")
        break

    print("Det är nu fiendens Tur!")

    attackera(Gladiator2, Gladiator1)
    if Gladiator1.visa_hälsa() <= 0:
        print(f"{colorama.Fore.CYAN}Du förlorade!!{colorama.Fore.RESET}")
        break
   
    print("")

    


