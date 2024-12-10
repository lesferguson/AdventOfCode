import re

def build_paths(current_valve, current_path):
    pass

def run(data):
    valves = {}
    for line in data:
        valve_info, tunnel_info = line.split("; ")
        valves[valve_info[6:8]] = {"open": False, "rate": valve_info[23:], "connections": re.findall(r'([A-Z][A-Z])', tunnel_info)}

    current_valve = "AA"
    total_flow = 0
    for minute in range(1, 31):
        if valves[current_valve]["open"]: # Move
            print()
        else:
            valves[current_valve]["open"] = True
            total_flow += valves[current_valve]["rate"] * (30 - minute)

        print()
    return