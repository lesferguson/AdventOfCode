import os

custom_year = "2024"
year = max([int(filename) for filename in os.listdir() if filename.isnumeric()]) if not custom_year else custom_year
days = os.listdir(year)
day_numbers = sorted([int(filename[:-3]) for filename in days if filename[:-3].isnumeric()])
print(year)
print("-----")
for day_num in day_numbers:
    day = f"{day_num}.py"
    print(f"day{day_num}")
    os.system(f'python 2024/{day}')
    print()
