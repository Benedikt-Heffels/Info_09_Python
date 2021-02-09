#Grundfunktionen
JA = ["Ja", "ja", "JA", "OK", "Ok", "ok"]
NEIN = ["Nein", "nein", "NEIN", "nö", "Nö", "NÖ"]


print("Willkommen beim interaktiven Anmeldeservice des Gymnasium Benediktivus!")
print("Leider befindet sich unsere Software noch in der Beta-Phase (d.h. Entwicklungsphase). Wir bitten dies zu Entschuldigen.")
print("Derzeit kann dieses Programm leider nur mit den Antworten Ja/Nein umgehen, wenn nicht anders gefordert.")
beta_ok = input("Ist das für Sie in Ordnung? ")

if beta_ok in JA:
    name = input("Geben Sie bitte ihren Namen ein: ")
    alter = input("Hallo " + name + "! Wie alt sind Sie? ")
    if int(alter) > 18: # größer/älter
        print("OK, " + name)
    elif int(alter) < 18: # kleiner/jünger
        Einverstaendnis = input("Hallo " + name + ", du möchtest dich also an unserer Schule anmelden. Sind deine Eltern den damit einverstanden? ")
        if Einverstaendnis in JA:
            print("Ok, dann lass uns beginnen")
        elif Einverstaendnis in NEIN:
            print("Wir freuen uns über dein Interesse! Aber komm doch bitte mit deinen Eltern wieder. Ok, " + name +"?")
if beta_ok in NEIN:
    Ersatz_Schulleitung = input("Das tut us Leid. Wir können Ihnen jedoch einen Termin mit unserer Schulleitung anbieten. Ist das für sie in Ordnung? ")
    if Ersatz_Schulleitung in JA:
        print("Das ist schön!")
    elif Ersatz_Schulleitung in NEIN:
        print("Es tut uns Leid, das wir sie nicht für unsere Schule gewinnen konnten!")
        print("Wir können ihnen als Ersatzschule stattdessen das Kreisgymnasium Benstadt empfehlen.")

