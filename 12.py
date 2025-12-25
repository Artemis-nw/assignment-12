def audit_energy_usage(filename):
    room_totals = {}
    power_hogs = {}
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            pp = line.split(',')
            ####################
            if len(pp) != 4:
                continue
            appliance, room, day_sum, night_sum = pp
            try:
                day_usage = float(day_sum)
                night_usage = float(night_sum)
            except ValueError:
                continue
            total_usage = day_usage + night_usage
            #####################
            if room in room_totals:
                room_totals[room] += total_usage
            else:
                room_totals[room] = total_usage
            if total_usage > 10.0:
                power_hogs.append((appliance, total_usage))
            #####################
    
    return room_totals, power_hogs
def save_energy_report(room_totals, power_hogs):
    with open('energy_report.txt', 'w') as file2:
        file2.write("ROOM ENERGY CONSUMPTION (kWh)\n")
        file2.write("-----------------------------\n")
        for room in sorted(room_totals.keys()):
            total = room_totals[room]
            file2.write(f"{room}: {total:.1f}\n")

        file2.write("\nPOWER HOGS (> 10 kWh)\n")
        file2.write("---------------------\n")
        for appliance, usage in power_hogs:
            file2.write(f"{appliance} ({usage:.1f} kWh)\n")
room_totals, power_hogs = audit_energy_usage('energy_log.txt')
save_energy_report(room_totals, power_hogs)

