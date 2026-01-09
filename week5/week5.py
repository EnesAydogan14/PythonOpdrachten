from datetime import datetime

APPTS_FILE = "appointments.txt"
PROFILE_FILE = "profile.txt"

SERVICES = {
    "1": {"name": "Knippen", "price": 20, "duration": 30},
    "2": {"name": "Baard trimmen", "price": 15, "duration": 20},
    "3": {"name": "Knippen + Baard", "price": 30, "duration": 50},
}

def save_profile(profile: dict) -> None:
    line = f"{profile['name']}|{profile['email']}|{profile['phone']}\n"
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        f.write(line)

def load_profile() -> dict | None:
    try:
        with open(PROFILE_FILE, "r", encoding="utf-8") as f:
            line = f.readline().strip()
            if not line:
                return None
            name, email, phone = line.split("|")
            return {"name": name, "email": email, "phone": phone}
    except FileNotFoundError:
        return None

def save_appt(appt: dict) -> None:
    line = f"{appt['customer']}|{appt['service']}|{appt['price']}|{appt['duration']}|{appt['date']}|{appt['time']}\n"
    with open(APPTS_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def load_appts() -> list:
    appts = []
    try:
        with open(APPTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 6:
                    continue
                customer, service, price, duration, date, time = parts
                appts.append({
                    "customer": customer,
                    "service": service,
                    "price": float(price),
                    "duration": int(duration),
                    "date": date,
                    "time": time,
                })
    except FileNotFoundError:
        pass
    return appts

def show_services() -> None:
    print("\nServices:")
    for key, s in SERVICES.items():
        print(f"{key}. {s['name']} - €{s['price']} ({s['duration']} min)")

def choose_service() -> dict:
    show_services()
    choice = ""
    while choice not in SERVICES:
        choice = input("Kies service (1/2/3): ").strip()
        if choice not in SERVICES:
            print("Ongeldige keuze.")
    return SERVICES[choice]

def is_future_date(date_str: str) -> bool:
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").date()
        return d >= datetime.now().date()
    except ValueError:
        return False

def book_appointment(profile: dict) -> None:
    service = choose_service()

    date = ""
    while not is_future_date(date):
        date = input("Datum (YYYY-MM-DD, alleen toekomst): ").strip()
        if not is_future_date(date):
            print("Ongeldige datum (format of verleden).")

    time = input("Tijd (HH:MM): ").strip()

    appt = {
        "customer": profile["name"],
        "service": service["name"],
        "price": service["price"],
        "duration": service["duration"],
        "date": date,
        "time": time,
    }
    save_appt(appt)
    print("\n✅ Afspraak geboekt!")
    print(appt)

def show_appointments(profile: dict) -> None:
    appts = [a for a in load_appts() if a["customer"] == profile["name"]]

    def sort_key(a):
        try:
            return datetime.strptime(a["date"] + " " + a["time"], "%Y-%m-%d %H:%M")
        except ValueError:
            return datetime.max

    appts.sort(key=sort_key)

    print("\n--- Jouw afspraken (chronologisch) ---")
    if not appts:
        print("Geen afspraken gevonden.")
        return

    for a in appts:
        print(f"{a['date']} {a['time']} | {a['service']} | €{a['price']} | {a['duration']} min")

def setup_profile() -> dict:
    print("\nProfiel instellen")
    name = input("Naam: ").strip()
    email = input("Email: ").strip()
    phone = input("Telefoon: ").strip()

    if not name or not email or not phone:
        print("❌ Alle velden zijn verplicht.")
        return setup_profile()

    profile = {"name": name, "email": email, "phone": phone}
    save_profile(profile)
    print("✅ Profiel opgeslagen!")
    return profile

def main():
    print("=== Old Town Barber - Python Console App ===")
    profile = load_profile()
    if not profile:
        profile = setup_profile()

    while True:
        print("\nMenu:")
        print("1. Profiel bekijken/wijzigen")
        print("2. Afspraak boeken")
        print("3. Mijn afspraken bekijken")
        print("4. Stoppen")

        choice = input("Keuze: ").strip()
        if choice == "1":
            profile = setup_profile()
        elif choice == "2":
            book_appointment(profile)
        elif choice == "3":
            show_appointments(profile)
        elif choice == "4":
            print("Tot de volgende keer!")
            break
        else:
            print("Ongeldige keuze.")

if __name__ == "__main__":
    main()
