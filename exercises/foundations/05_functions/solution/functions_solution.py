# Task 1: Pilot Identification
def greet_pilot(name):
    return f"Welcome aboard, Commander {name}. Flight systems ready."


# Task 2: Fuel Consumption Calculator
def calculate_fuel(distance, burn_rate):
    Consumption = distance * burn_rate
    return float(Consumption)


# Task 3: Trip Cost with Standard Fuel Rate
def calculate_trip_cost(fuel_needed, price_per_unit=2.5):
    fuel_Rate = fuel_needed * price_per_unit
    return float(fuel_Rate)


# Task 4: Manifest Broadcast
def display_manifest(cargo_item, quantity, priority="STANDARD"):
    print(f"[CARGO] {quantity}x {cargo_item}")
    print(f"[STATUS] Priority: {priority}")


# Task 5: Dispatch Summary Pipeline
def create_dispatch_summary(pilot_name, distance, burn_rate=1.5, price_per_unit=2.5):
    fuel_needed = calculate_fuel(distance, burn_rate)
    total_cost = calculate_trip_cost(fuel_needed, price_per_unit)
    return (
        f"Dispatch Plan for {pilot_name}: {fuel_needed} fuel units required. "
        f"Total cost: {total_cost} credits."
    )


