station_name = "Orion 9"
module_count = 12
signal_frequency = 1420.405
life_support_active = True
backup_generator = None

raw_energy_reading = "100"
energy_level = int(raw_energy_reading)
raw_distance_reading = 45
exact_distance = float(raw_distance_reading)
raw_status_code = 1
is_operational = bool(raw_status_code)

station_status = str(module_count) + " - " + station_name
print(station_status)
