
print("Welkom bij Old Town Barber!")

name = input("Wat is je naam? ").strip()
service_price = float(input("Wat kost de service (€)? "))
tip_percent = float(input("Hoeveel % fooi wil je geven? "))

tip_amount = service_price * (tip_percent / 100)
total = service_price + tip_amount

print("\n--- Bonnetje ---")
print(f"Klant: {name}")
print(f"Service: €{service_price:.2f}")
print(f"Fooi: €{tip_amount:.2f}")
print(f"Totaal: €{total:.2f}")
