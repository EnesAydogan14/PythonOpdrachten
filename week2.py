services = {
    "1": ("Knippen", 20),
    "2": ("Baard trimmen", 15),
    "3": ("Knippen + Baard", 30),
}

print("Kies een service:")
for key, (name, price) in services.items():
    print(f"{key}. {name} - €{price}")

choice = ""
while choice not in services:
    choice = input("Maak een keuze (1/2/3): ").strip()
    if choice not in services:
        print("Ongeldige keuze, probeer opnieuw.")

service_name, service_price = services[choice]

if service_price >= 25:
    print("Je hebt een premium service gekozen.")
else:
    print("Je hebt een standaard service gekozen.")

print(f"Gekozen: {service_name} (€{service_price})")
