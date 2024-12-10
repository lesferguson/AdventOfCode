from collections import defaultdict

def run(data):

    school = defaultdict(int, {})
    for fish in data:
        school[fish] += 1

    for _ in range(256):
        new_school = defaultdict(int, {})
        for cycle, population in school.items():
            if cycle == 0:
                new_school[8] += population
                new_school[6] += population
            else:
                new_school[cycle-1] += population

        school = new_school

    total_pop = 0
    for cycle, population in school.items():
        total_pop += population
    return total_pop