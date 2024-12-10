import json
from re import match

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
        for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
            if field not in passport:
                print("missing", field, passport)
                bad = True
                break
            else:
                if field == "byr" and not 1920 <= int(passport[field]) <= 2002:
                    print("bad byr:", passport)
                    bad = True
                    break
                elif field == "iyr" and not 2010 <= int(passport[field]) <= 2020:
                    print("bad iyr:", passport)
                    bad = True
                    break
                elif field == "eyr" and not 2020 <= int(passport[field]) <= 2030:
                    print("bad eyr:", passport)
                    bad = True
                    break
                elif field == "hgt" and passport[field].endswith("cm") and not 150 <= int(
                        passport[field].strip("cm")) <= 193:
                    print("bad hgt:", passport)
                    bad = True
                    break
                elif field == "hgt" and passport[field].endswith("in") and not 59 <= int(
                        passport[field].strip("in")) <= 76:
                    print("bad hgt:", passport)
                    bad = True
                    break
                elif field == "hgt" and not passport[field].endswith("in") and not passport[field].endswith("cm"):
                    print("bad hgt:", passport)
                    bad = True
                    break
                elif field == "hcl" and not len(passport[field]) == 7 and not match(r'#[\dA-Fa-f]{6}', passport[field]):
                    print("bad hcl:", passport)
                    bad = True
                    break
                elif field == "ecl" and not passport[field] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    print("bad ecl:", passport)
                    bad = True
                    break
                elif field == "pid" and not len(passport[field]) == 9:
                    print("bad pid:", passport)
                    bad = True
                    break

        if not bad:
            passports.append(passport)
        passport = {}
        continue

bad = False
for field in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
    if field not in passport:
        print("missing", field, passport)
        bad = True
        break
    else:
        if field == "byr" and not 1920 <= int(passport[field]) <= 2002:
            print("bad byr:", passport)
            bad = True
            break
        elif field == "iyr" and not 2010 <= int(passport[field]) <= 2020:
            print("bad iyr:", passport)
            bad = True
            break
        elif field == "eyr" and not 2020 <= int(passport[field]) <= 2030:
            print("bad eyr:", passport)
            bad = True
            break
        elif field == "hgt" and passport[field].endswith("cm") and not 150 <= int(passport[field].strip("cm")) <= 193:
            print("bad hgt:", passport)
            bad = True
            break
        elif field == "hgt" and passport[field].endswith("in") and not 59 <= int(passport[field].strip("in")) <= 76:
            print("bad hgt:", passport)
            bad = True
            break
        elif field == "hgt" and not passport[field].endswith("in") and not passport[field].endswith("cm"):
            print("bad hgt:", passport)
            bad = True
            break
        elif field == "hcl" and not match(r'#[0-9A-Fa-f]{6}', passport[field]):
            print("bad hcl:", passport)
            bad = True
            break
        elif field == "ecl" and not passport[field] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            print("bad ecl:", passport)
            bad = True
            break
        elif field == "pid" and not len(passport[field]) == 9:
            print("bad pid:", passport)
            bad = True
            break

if not bad:
    passports.append(passport)

for p in passports:
    print(json.dumps(p, sort_keys=True))

print(len(passports))
