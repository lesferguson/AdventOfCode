# Fuel = floor(Mass/3) - 2

masses = None

total_fuel = 0
fuel = int()

for m in masses:
    fuel = int(m / 3) - 2
    total_fuel += fuel
    while fuel > 0:
        fuel = int(fuel/3) - 2
        if fuel > 0:
            total_fuel += fuel
            print(fuel)
    print(total_fuel)

print(total_fuel)

