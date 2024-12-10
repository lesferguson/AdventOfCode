
# data = [int(n.strip()) for n in open("input.txt").readlines()]
data = open("input.txt").readlines()
passports = []
passport = {}
for line in data:

    if line.strip():
        for field in line.split(" "):
            k, v = field.strip().split(":")
            passport[k] = v
    else:
        bad = False
        for field in ["byr", "iyr", "eyr","hgt","hcl", "ecl", "pid"]:
            if field not in passport:
                print("bad passport:", passport)
                bad = True
        if not bad:
            passports.append(passport)
        passport = {}
        continue
for field in ["byr", "iyr", "eyr","hgt","hcl", "ecl", "pid"]:
    if field not in passport:
        print("bad passport:", passport)
        bad = True
if not bad:
    passports.append(passport)

print(len(passports))