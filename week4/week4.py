
FILE_NAME = "appointments.txt"

def save_appointment_to_file(appt: dict, filename: str) -> None:

    line = f"{appt['customer']}|{appt['service']}|{appt['price']}|{appt['duration']}|{appt['date']}|{appt['time']}\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(line)

def load_appointments_from_file(filename: str) -> list:
    appointments = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 6:
                    print("Waarschuwing: fout formaat regel overgeslagen:", line)
                    continue
                customer, service, price, duration, date, time = parts
                appointments.append({
                    "customer": customer,
                    "service": service,
                    "price": float(price),
                    "duration": int(duration),
                    "date": date,
                    "time": time
                })
    except FileNotFoundError:
        pass
    return appointments


new_appt = {
    "customer": input("Naam: ").strip(),
    "service": input("Service: ").strip(),
    "price": float(input("Prijs: ").strip()),
    "duration": int(input("Duur (min): ").strip()),
    "date": input("Datum (YYYY-MM-DD): ").strip(),
    "time": input("Tijd (HH:MM): ").strip(),
}

save_appointment_to_file(new_appt, FILE_NAME)
print("\nOpgeslagen!")

all_appts = load_appointments_from_file(FILE_NAME)
print("\nAlle afspraken uit bestand:")
for a in all_appts:
    print(a)
