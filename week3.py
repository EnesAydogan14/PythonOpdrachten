appointments = []

services = {
    "1": {"name": "Knippen", "price": 20, "duration": 30},
    "2": {"name": "Baard trimmen", "price": 15, "duration": 20},
    "3": {"name": "Knippen + Baard", "price": 30, "duration": 50},
}

def show_services(service_dict: dict) -> None:
    print("\nServices:")
    for key, s in service_dict.items():
        print(f"{key}. {s['name']} - €{s['price']} ({s['duration']} min)")

def ask_choice(service_dict: dict) -> str:
    choice = ""
    while choice not in service_dict:
        choice = input("Kies service (1/2/3): ").strip()
        if choice not in service_dict:
            print("Ongeldige keuze.")
    return choice

def add_appointment(appts: list, customer: str, service: dict, date: str, time: str) -> dict:
    appt = {
        "customer": customer,
        "service": service["name"],
        "price": service["price"],
        "duration": service["duration"],
        "date": date,
        "time": time,
    }
    appts.append(appt)
    return appt

customer = input("Naam: ").strip()
show_services(services)
choice = ask_choice(services)

date = input("Datum (YYYY-MM-DD): ").strip()
time = input("Tijd (HH:MM): ").strip()

new_appt = add_appointment(appointments, customer, services[choice], date, time)

print("\nAfspraak toegevoegd:")
print(new_appt)
print("\nAlle afspraken:")
for a in appointments:
    print(a)
