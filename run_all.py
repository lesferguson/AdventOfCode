import os
import re

year = "2024"
days = os.listdir(year)
for day in days:
    if re.fullmatch(r"\d{1,2}.py", day):
        print(year + "/" + day)
        os.system(f'python 2024/{day}')
