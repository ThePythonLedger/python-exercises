# Task 1
security_level = 5
countdown_log = ""
while security_level > 0:
    security_level_str = str(security_level)
    countdown_log += security_level_str + " "
    security_level -= 1

# Task 2
total_energy = 0
for energy in range(1, 11):
    if energy % 2 != 0:
        continue
    total_energy += energy

# Task 3
bypass_code = 7
attempts_made = 0
for attempt in range(1, 101):
    attempts_made += 1
    if attempt == bypass_code:
        break

# Task 4
grid_output = ""
for row in range(1, 4):
    for col in range(1, 4):
        coords = f"[{row},{col}]"
        grid_output += coords
    grid_output += "/n"

# Task 5
secret_pin = 42
current_attempt = 35
valid_checks = 0
while True:
    current_attempt += 1
    if current_attempt % 5 == 0:
        continue
    valid_checks += 1
    if current_attempt == secret_pin:
        break
