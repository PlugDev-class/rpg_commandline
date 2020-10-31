import time
import os
import random
import sys
from tkinter import *

leben = 100
jn = ""
gegnerleben = 20
a = 1
attack = False
invnummer = ""
wname = ""
wkraft = ""
gattack = ""
gname = ""
mobforce = 0
mobdef = 0
istende = False
mobdead = []

#0 = nein 1 = ja
def kisten_spawn():
    kistenspawn = zkisten[random.randint(0,30)]
    if kistenspawn == 0:
        kiste_mythic()
    if kistenspawn == 1:
        kiste_episch()
    if kistenspawn == 2:
        kiste_episch()
    if kistenspawn == 3:
        kiste_episch()
    if kistenspawn == 4:
        kiste_episch()
    if kistenspawn == 5:
        kiste_episch()
    if kistenspawn == 6:
        kiste_episch()
    if kistenspawn == 7:
        kiste_selten()
    if kistenspawn == 8:
        kiste_selten()
    if kistenspawn == 9:
        kiste_selten()
    if kistenspawn == 10:
        kiste_selten()
    if kistenspawn == 11:
        kiste_selten()
    if kistenspawn == 12:
        kiste_selten()
    if kistenspawn == 13:
        kiste_selten()
    if kistenspawn == 14:
        kiste_selten()
    if kistenspawn == 15:
        kistenungewoehnlich()
    if kistenspawn == 16:
        kistenungewoehnlich()
    if kistenspawn == 17:
        kistenungewoehnlich()
    if kistenspawn == 18:
        kistenungewoehnlich()
    if kistenspawn == 19:
        kistenungewoehnlich()
    if kistenspawn == 20:
        kistenungewoehnlich()
    if kistenspawn == 21:
        kistenungewoehnlich()
    if kistenspawn == 22:
        kistenungewoehnlich()
    if kistenspawn == 23:
        kistenungewoehnlich()
    if kistenspawn == 24:
        kistenungewoehnlich()
    if kistenspawn == 25:
        kistenungewoehnlich()
    if kistenspawn == 26:
        kistenungewoehnlich()
    if kistenspawn == 27:
        kistenungewoehnlich()
    if kistenspawn == 28:
        kistenungewoehnlich()
    if kistenspawn == 29:
        kistenungewoehnlich()
    if kistenspawn == 30:
        kistenungewoehnlich()






def kistenungewoehnlich():
    print("Du findest eine Ungewöhnliche Kiste")
    kistendrop = zahlen[random.randint(0,10)]
    if kistendrop == 0:
        rostiges_schwert()
    if kistendrop == 1:
        alte_Axt()
    if kistendrop == 2:
        rostige_Schaufel()
    if kistendrop == 3:
        alter_Dolch()
    if kistendrop == 4:
        stumpfes_Schwert()
    if kistendrop == 5:
        Lang_Schwert()
    if kistendrop == 6:
        kaputter_Bogen()
    if kistendrop == 7:
        Stein_Schwert()
    if kistendrop == 8:
        Holz_Schwert()
    if kistendrop == 9:
        Eisen_Axt()
    if kistendrop == 10:
        Eisen_Schwert()

def kiste_selten():
    print("Du findest eine seltene Kiste")
    kistendrop = zahlen[random.randint(0,10)]
    if kistendrop == 0:
        rostiges_schwert()
    if kistendrop == 1:
        alte_Axt()
    if kistendrop == 2:
        rostige_Schaufel()
    if kistendrop == 3:
        alter_Dolch()
    if kistendrop == 4:
        stumpfes_Schwert()
    if kistendrop == 5:
        Lang_Schwert()
    if kistendrop == 6:
        bow()
    if kistendrop == 7:
        Stein_Schwert()
    if kistendrop == 8:
        Lang_Schwert()
    if kistendrop == 9:
        Eisen_Axt()
    if kistendrop == 10:
        Eisen_Schwert()
def kiste_episch():
    print("Du findest eine epische Kiste")
    kistendrop = zahlen[random.randint(0,10)]
    if kistendrop == 0:
        knight_sword()
    if kistendrop == 1:
        timber_axt()
    if kistendrop == 2:
        bow()
    if kistendrop == 3:
        starker_zauberstab()
    if kistendrop == 4:
        Zaubern()
    if kistendrop == 5:
        knight_sword()
    if kistendrop == 6:
        timber_axt()
    if kistendrop == 7:
        bow()
    if kistendrop == 8:
        starker_zauberstab()
    if kistendrop == 9:
       knight_sword()
    if kistendrop == 10:
        Eisen_Schwert()

def kiste_mythic():
    print("Du findest eine mytische Kiste")
    kistendrop = zahlen[random.randint(0,10)]
    if kistendrop == 0:
        Mystisches_Schwert()
    if kistendrop == 1:
        mystische_axt()
    if kistendrop == 2:
        Zaubern()
    if kistendrop == 3:
        Mystisches_Schwert()
    if kistendrop == 4:
        stumpfes_Schwert()
    if kistendrop == 5:
        Mystisches_Schwert()
    if kistendrop == 6:
        Mystisches_Schwert()
    if kistendrop == 7:
        Mystisches_Schwert()
    if kistendrop == 8:
        Mystisches_Schwert()
    if kistendrop == 9:
        Mystisches_Schwert()
    if kistendrop == 10:
        Mystisches_Schwert()
def Lebens_Trank():
    global  leben
    print("Du findest einen Lebens_Trank")
    print("Er füllt deinen Leben um 50 auf")
    leben + 50
    return  leben
def loot_bag():
    global  jn
    print("Du findest ein loot_bag")
    print("Möchtest du sie öffnen?")
    jn = input()
    if jn == "j":
        kistendrop = zahlen[random.randint(0,10)]
        #if kis
def attackintro():
    print("Der Gegner hat", gegnerleben, "HP", "Du hast", leben, "HP")
    print("In deinem Iventar ist", wname, "mit", wkraft, "Angriffspunkten")
def monsterlvl1():
    monsterspawn = zahlen2[random.randint(0,10)]
    if monsterspawn == 0:
        dicker_goblin()
    if monsterspawn == 1:
        goblin()
    if monsterspawn == 2:
        kobold()
    if monsterspawn == 3:
        zombie()
    if monsterspawn == 4:
        riesen_Spinne()
    if monsterspawn == 5:
        unheimlicher_Baum()
    if monsterspawn == 6:
        hexe()
    if monsterspawn == 7:
        riese()
    if monsterspawn == 8:
        golem()
    if monsterspawn == 9:
        kleine_Spinne()
    if monsterspawn == 10:
        waechter()

def kampfsystem():
    global gegnerleben
    global wkraft
    global leben
    global gattack
    global istende
    a = 1

    while gegnerleben > 0:
        print("Du greifst", gname, "mit", wname, "an")
        gegnerleben = gegnerleben - wkraft
        print(gname, "hat noch", gegnerleben, "HP")
        warten()
        if gegnerleben <= 0:
            print("Glückwunsch du hast", gname, "besiegt")
            mobdead.append(gname)
            break
        leben = leben - gattack
        print(gname, "hat dich getroffen.", "Du hast noch", leben, "HP")
        if leben <= 0:
            istende = True
            break
    return istende
    return gegnerleben
    return wkraft
    return leben
    return gattack


def kampfsystem_2():
    global gegnerleben
    global wkraft
    global leben
    global gattack
    global istende

    # unterschiedliche attacks die für jede Waffe definiert sind
    while gegnerleben > 0:
        print("/n Deine Waffe ist:", wname, "mit", wkraft, "Atk")
        print("Welchen Angriff möchtest du ausführen?")
        print("/n Spezialangriff(1), Normalerangriff(2), Heiltrank(3)")
        gibab = int(input())
        if gibab == 1:
            print("Du setzt deinen Spezialangriff ein")
            pech = random.randint(0,10)
            if pech == 0:
                print("Du hattest Pech dein Angriff ist fehlgeschlagen")
                leben = leben - gattack
                print(gname, "hat dich getroffen.", "Du hast noch", leben, "HP")
                if leben <= 0:
                    istende = True
                    break
            if pech == 1:
                print("Du hattest Pech dein Angriff ist fehlgeschlagen")
                leben = leben - gattack
                print(gname, "hat dich getroffen.", "Du hast noch", leben, "HP")
                if leben <= 0:
                    istende = True
                    break
            if pech == 2:
                print("Du hattest Pech dein Angriff ist fehlgeschlagen")
                leben = leben - gattack
                print(gname, "hat dich getroffen.", "Du hast noch", leben, "HP")
                if leben <= 0:
                    istende = True
                    break

            multi = random.randint(1,3)
            wkraft = wkraft * multi
            print("Du erhälst einen Multiplikator von", multi, "/n Nun hat deine Waffe", wname, wkraft, "Atk")
            gegnerleben = gegnerleben - wkraft
            print(gname, "hat noch", gegnerleben, "HP")
            wkraft = wkraft / multi
            if gegnerleben <= 0:
                print("Glückwunsch du hast", gname, "besiegt")
                mobdead.append(gname)
                break
            leben = leben - gattack
            print(gname, "hat dich getroffen.", "Du hast noch", leben, "HP")
            if leben <= 0:
                istende = True
                break
        if gibab == 2:
            print("Du greifst", gname, "mit", wname, "an")
            gegnerleben = gegnerleben - wkraft
            print(gname, "hat noch", gegnerleben, "HP")
            warten()
            if gegnerleben <= 0:
                print("Glückwunsch du hast", gname, "besiegt")
                mobdead.append(gname)
                break
            leben = leben - gattack
            print(gname, "hat dich getroffen.", "Du hast noch", leben, "HP")
            if leben <= 0:
                istende = True
                break
        if gibab == 3:
            print("Du setzt einen Heiltrank ein")
            heil = random.randint(25,200)
            leben = leben + heil
            print("Der Heiltrank heilt dich um", heil, "/n Du hast aktuell", leben, "HP")
            leben = leben - gattack
            print(gname, "hat dich getroffen.", "Du hast noch", leben, "HP")
            if leben <= 0:
                istende = True
                break
def fistende():
    print("Deine Reise ist nun zu ende", "Du hast folgende Gegner besiegt", mobdead)
    print("Willst du es nochmal versuchen")
    print("Dann starte das Programm neu")
    sys.exit(0)
def warten():
    time.sleep(a)

def jnreset():
    jn = ""

#waffen und monster und tränke und perks

zahlen2 = [0,1,2,3,4,5,6,7,8,9,10]
zahlen = [0,1,2,3,4,5,6,7,8,9,10]
zkisten = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

#tränke und perks

#monster
def dicker_goblin():
    print("Es erscheint ein dicker goblin mit 40 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 40 + mobdef
    gattack = 5 + mobforce
    gname = ("Dicker Goblin")
    return gname
    return gattack
    return gegnerleben
def goblin():
    print("Es erscheint ein goblin mit 20 HP mit", mobdef, "Boost")
    global gattack
    global gegnerleben
    global gname
    gegnerleben = 20 + mobdef
    gattack = 10 + mobforce
    gname = ("Goblin")
    return gname
    return gattack
    return gegnerleben
def kobold():
    print("Es erscheint ein kobold mit 25 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 25 + mobdef
    gattack = 10 + mobforce
    gname = ("Kobold")
    return gname
    return gattack
    return gegnerleben
def zombie():
    print("Es erscheint ein zombie mit 10 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 10 + mobdef
    gattack = 15 + mobforce
    gname = ("Zombie")
    return gname
    return gegnerleben
    return gattack
def riesen_Spinne():
    print("Es erscheint eine riesen Spinne mit 20 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 20 + mobdef
    gattack = 20 + mobforce
    gname = ("Riesen Spinne")
    return gname
    return gegnerleben
    return gattack

def unheimlicher_Baum():
    print("Es erscheint ein unheimlicher Baum mit 30 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 30 + mobdef
    gattack = 5 + mobforce
    gname = ("Unheimlicher Baum")
    return gname
    return gegnerleben
    return gattack
def hexe():
    print("Es erscheint eine Hexe mit 40 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 40 + mobdef
    gattack = 10 + mobforce
    gname = ("Hexe")
    return gname
    return gegnerleben
    return gattack
def riese():
    print("Es erscheint ein Riese mit 50 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 50 + mobdef
    gattack = 10 + mobforce
    gname = ("Riese")
    return gname
    return gattack
    return gegnerleben
def golem():
    print("Es erscheint ein Golem mit 100 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 100 + mobdef
    gattack = 5 + mobforce
    gname = ("Golem")
    return gname
    return gegnerleben
    return gattack
def kleine_Spinne( ):
    print("Es erscheint eine kleine Spinne mit 10 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 10 + mobdef
    gattack = 20 + mobforce
    gname = ("Kleine Spinne")
    return gname
    return gegnerleben
    return gattack
def waechter():
    print("Es erscheint ein Wächter mit 25 HP mit", mobdef, "Boost")
    global gegnerleben
    global gattack
    global gname
    gegnerleben = 25 + mobdef
    gattack = 20 + mobforce
    gname = ("Wächter")
    return gname
    return gegnerleben
    return gattack







#waffen

#waffen selten
def knight_sword():
    global wname
    global wkraft
    print("Du erhälst Knight_Sword")
    print("Angriffspunkte 30")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    if jn == ("j"):
        wname = "knight_sword"
        wkraft = 30
        print("In dein Inventar ist jetzt", wname)
        return wkraft
        return wname
    else:
        print("Du behälst deine Waffe")

def timber_axt():
    global wname
    global wkraft
    print("Du erhälst Timber_Axt")
    print("Angriffspunkte 25")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    if jn == ("j"):
        wname = "Timber_Axt"
        wkraft = 25
        print("In dein Inventar ist jetzt", wname)
        return wkraft
        return wname
    else:
        print("Du behälst deine Waffe")

def bow():
    global wname
    global wkraft
    print("Bogen")
    print("Angriffspunkte 25")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    if jn == ("j"):
        wname = "Bogen"
        wkraft = 25
        print("In dein Inventar ist jetzt", wname)
        return wkraft
        return wname
    else:
        print("Du behälst deine Waffe")


def starker_zauberstab():
    global wname
    global wkraft
    print("Starker_Zauberstab")
    print("Angriffspunkte 45")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    if jn == ("j"):
        wname = "Starker_Zauberstab"
        wkraft = 45
        print("In dein Inventar ist jetzt", wname)
        return wkraft
        return wname
    else:
        print("Du behälst deine Waffe")

def Zaubern():
    global wname
    global wkraft
    print("Du kannst die Kunst des Zaubern mit dunkler Magie erlangen. Dafür musst du deinen Waffenslot abgeben somit deine aktuelle Waffe", wname, "mit", wkraft, "Angriffschaden")
    print("Der dunkle Magie Zauber hat 200 Atk")
    print("Willst du die Kunst erlangen")
    jn = input()
    if jn == ("j"):
        wname = "Dunkle_Magie"
        wkraft = 200
        print("Du hast nun die Fähigkeit", wname, "zu benutzen")
        return wkraft
        return wname
    else:
        print("Du behälst deine Waffe")
def mystische_axt():
    global wname
    global wkraft
    print("Mystische_Axt")
    print("Angriffspunkte 210")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    if jn == ("j"):
        wname = "Mystische_Axt"
        wkraft = 210
        print("In dein Inventar ist jetzt", wname)
        return wkraft
        return wname
    else:
        print("Du behälst deine Waffe")

def useless_sword():
    global wname
    global wkraft
    print("Useless_Sword")
    print("Angriffspunkte 0")
    print("Das ist das beste Schwert im Game")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    if jn == ("j"):
        wname = "Useless_Sword"
        wkraft = 0
        print("In dein Inventar ist jetzt", wname)
        return wkraft
        return wname
    else:
        print("Du behälst deine Waffe")


#waffen ungewöhmlich

def rostiges_schwert():
    global wname
    global wkraft
    print("Du erhälst rostiges_Schwert")
    print("Angriffspunkte 10")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 0
        wname = "rostiges schwert"
        wkraft = 10
        print("In dein Inventar ist jetzt rostiges_schwert")
        return wkraft
        return wname
        return invnummer
    else:
        print("Du behälst deine Waffe")

def alte_Axt():
    global wname
    global wkraft
    print("Du erhälst alte_Axt")
    print("Angriffspunkte 5")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 1
        wname = "alte Axt"
        print("In dein Inventar ist jetzt alte_Axt")
        wkraft = 5
        return wkraft
        return invnummer
        return wname
    else:
        print("Du behälst deine Waffe")
def rostige_Schaufel():
    global wname
    global wkraft
    print("Du erhälst rostige_Schaufel")
    print("Angriffspunkte 5")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 2
        wname = "rostige Schaufel"
        print("In dein Inventar ist jetzt rostige_Schaufel")
        wkraft = 5
        return wkraft
        return invnummer
        return wname
    else:
        print("Du behälst deine Waffe")
def alter_Dolch():
    global wname
    global wkraft
    print("Du erhälst alter_Dolch")
    print("Angriffspunkte 5")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 3
        wname = "alter Dolch"
        print("In dein Inventar ist jetzt alter_Dolch")
        wkraft = 5
        return wkraft
        return invnummer
        return wname
    else:
        print("Du behälst deine Waffe")
def Lang_Schwert():
    global wname
    global wkraft
    print("Du erhälst Lang_Schwert")
    print("Angriffspunkte 20")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 9
        wname = "Lang_Schwert"
        print("In dein Inventar ist jetzt Lang_Schwert")
        wkraft = 20
        return wkraft
        return invnummer
        return wname
    else:
        print("Du behälst deine Waffe")
def stumpfes_Schwert():
    global wname
    global wkraft
    print("Du erhälts Stumpfes_Schwert")
    print("Angriffspunkte 2")
    print("Willst du es in deinem Inventr aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 10
        wname = "Stumpfes_Schwert"
        print("In dein Inventar ist jetzt Stumpfes_Schwert")
        wkraft = 2
        return wkraft
        return invnummer
        return wname

def kaputter_Bogen():
    global wname
    global wkraft
    print("Du erhälst kaputter_Bogen")
    print("Angriffspunkte 5")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 4
        wname = "kaputter Bogen"
        wkraft = 5
        print("In dein Inventar ist jetzt kaputter_Bogen")
        return wkraft
        return invnummer
        return wname
    else:
        print("Du behälst deine Waffe")
def Stein_Schwert():
    global wname
    global wkraft
    print("Du erhälst Stein_Schwert")
    print("Angriffspunkte 5")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 5
        wkraft = 5
        wname = "Stein Schwert"
        print("In dein Inventar ist jetzt Stein_Schwert")
        return wkraft
        return invnummer
        return wname
    else:
        print("Du behälst deine Waffe")
def Holz_Schwert():
    global wname
    global wkraft
    print("Du erhälst Holz_Schwert")
    print("Angriffspunkte 2")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 6
        wkraft = 2
        wname = "Holz Schwert"
        print("In dein Inventar ist jetzt Holz_Schwert")
        return wkraft
        return invnummer
        return wname
    else:
        print("Du behälst deine Waffe")
def Eisen_Schwert():
    global wname
    global wkraft
    print("Du erhälst Eisen_Schwert")
    print("Angriffspunkte 20")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 7
        wname = "Eisen Schwert"
        wkraft = 20
        print("In dein Inventar ist jetzt Eisen_Schwert")
        return wkraft
        return invnummer
        return wname
    else:
        print("Du behälst deine Waffe")
def Eisen_Axt():
    global wname
    global wkraft
    print("Du erhälst Eisen_Axt")
    print("Angriffspunkte 15")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    jn = input()
    global invnummer
    if jn == ("j"):
        invnummer = 8
        wname = "Eisen Axt"
        wkraft = 15
        print("In dein Inventar ist jetzt Eisen_Axt")
    else:
        print("Du behälst deine Waffe")
        return wkraft
        return invnummer
        return wname

#ab hier neue Waffen...
def Mystisches_Schwert():
    global wname
    global wkraft
    print("Du erhälst Mystisches_Schwert")
    print("Angriffspunkte 150")
    print("Willst du es in deinem Inventar aufnehmen. Achtung!! Deine vorherige Waffe", wname, "mit", wkraft, "Atk wird ausgetauscht!")
    global invnummer
    if jn == ("j"):
        invnummer = 11
        wname = "Mystisches_Schwert"
        wkraft = 150
        print("In dein Inventar ist jetzt Mystisches_Schwert")
    else:
        print("Du behälst deine Waffe")
        return wkraft
        return invnummer
        return wname

play = True
play2 = True
#Attacksystrm


play = True

while play == True:
    print("Willkommen beim legendären RPG!")
    warten()
    print("Kurze Regeln man kann mit ja [j] oder nein [n] antworten")
    warten()
    print("Viel Spaß Abenteurer")
    warten()
    print("Bist du bereit?")
    jn = input()
    if jn == ("j"):
        print("Zauberwald")
        a = 1
        jnreset()
        warten()
        print("2145 Winter")
        warten()
        print("Neben dir ist eine rostige Kiste möchtest du sie öffnen?")
    jn = input()
    if jn == ("j"):
        print("3")
        print("2")
        print("1")
        jnreset()
        kistenungewoehnlich()


    print("Du läufst durch den dunklen Wald")
    a = 2
    warten()

    print("Ein Monster erscheint")
    #attackintro()
    monsterlvl1()
    kampfsystem_2()
    if istende == True:
        fistende()
    print("Du findest eine Kiste möchtest du sie öffnen")
    jn = input()
    if jn == ("j"):
        kisten_spawn()
    print("Hier spricht der Zaubermeister")
    a = 3
    warten()
    print("Je weiter du durch den dunklen Wald läufst, desto stärker werden die monster. Der Loot wird aber auch immer besser")
    warten()
    print("Du läufst tiefer in den Wald")
    warten()
    mobdef = 5
    mobforce = 5
    print("Ein Monster erscheint")
    monsterlvl1()
    kampfsystem_2()
    if istende == True:
        fistende()
    print("Du findest eine Kiste möchtest du sie öffnen")
    jn = input()
    if jn == ("j"):
        kisten_spawn()
    warten()

    def unendlich_tiefer():
        print("Du läufst tiefer in den Wald")
        warten()
        print("Ein Monster erscheint")
        monsterlvl1()
        kampfsystem_2()
        if istende == True:
            fistende()
            print("Du findest eine Kiste möchtest du sie öffnen")
            jn = input()
        if jn == ("j"):
            kisten_spawn()
        warten()

    mobdef = 10
    mobforce = 10
    unendlich_tiefer()
    mobdef = 20
    mobforce = 20
    unendlich_tiefer()
    mobdef = 20
    mobforce = 20
    unendlich_tiefer()
    mobdef = 25
    mobforce = 25
    unendlich_tiefer()
    mobdef = 30
    mobforce = 30
    unendlich_tiefer()
    mobdef = 40
    mobforce = 40
    unendlich_tiefer()
    print("Du hast gewonnen")
    #sys.exit(app.exec_())