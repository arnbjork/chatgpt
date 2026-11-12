
import json
import os

FIL = "kalender.json"

def hamta_planer():
    if os.path.exists(FIL):
        with open(FIL, "r", encoding="utf-8") as fil:
            return json.load(fil)
    return []

def spara_planer():
    with open(FIL, "w", encoding="utf-8") as fil:
        json.dump(planer, fil, ensure_ascii=False, indent=4)

planer = hamta_planer()

def visa_kalender():
    print("\n===== MIN KALENDER =====")

    if not planer:
        print("Du har inga planer ännu.")
    else:
        for i, plan in enumerate(planer):
            print(f"{i + 1}. {plan['datum']} kl. {plan['tid']} - {plan['namn']}")

def lagg_till():
    print("\n--- Lägg till en plan ---")
    datum = input("Datum (ÅÅÅÅ-MM-DD): ")
    tid = input("Tid (TT:MM): ")
    namn = input("Vad ska du göra? ")

    planer.append({
        "datum": datum,
        "tid": tid,
        "namn": namn
    })

    spara_planer()
    print("Planen har lagts till!")

def ta_bort():
    visa_kalender()

    if not planer:
        return

    try:
        nummer = int(input("\nVilken plan vill du ta bort? "))
        if 1 <= nummer <= len(planer):
            borttagen = planer.pop(nummer - 1)
            spara_planer()
            print(f"Du tog bort: {borttagen['namn']}")
        else:
            print("Ogiltigt nummer!")
    except ValueError:
        print("Skriv ett giltigt nummer!")

while True:
    print("\n===== KALENDERMENY =====")
    print("1. Visa kalender")
    print("2. Lägg till plan")
    print("3. Ta bort plan")
    print("4. Avsluta")

    val = input("\nVälj ett alternativ: ")

    if val == "1":
        visa_kalender()
    elif val == "2":
        lagg_till()
    elif val == "3":
        ta_bort()
    elif val == "4":
        print("Kalendern sparad. Hejdå!")
        break
    else:
        print("Fel val, försök igen!")

