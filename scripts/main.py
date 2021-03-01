from progress.bar import ChargingBar

files_name = ['a', 'b', 'c', 'd', 'e', 'f']

# dictionaries & lists
cars = []
streets = {}
intersections = {}

# * main function


def solve(name, lines):
    # ? parse start
    D, I, S, V, F = map(lambda x: int(x), lines[0].split(" "))
    # print(D, I, S, V, F)
    lines = lines[1:]
    lines_streets = lines[:S]
    # print("--- streets ---")
    for l in lines_streets:
        B, E, street_name, L = l.split(" ")
        street_name = street_name.replace("\n", "")
        streets[street_name] = {
            'i_start': B,
            'i_end': E,
            'length': int(L),
            'requests': 0
        }
        if intersections.get(E) is None:
            intersections[E] = [street_name]
        else:
            intersections[E].append(street_name)
        # print(streets[street_name])
    # print("--- paths ---")
    lines_paths = lines[S:S+V]
    for l in lines_paths:
        # P = l.split(" ")[0] # ! useless
        streets_names = list(map(lambda name: name.replace(
            "\n", ""), l.split(" ")[1:]))
        cars.append(streets_names)
        for street in streets_names:
            streets[street]['requests'] += 1
    # ? parse end

    # ? statistics
    tot_length = 0
    tot_requests = 0
    for street_name, value in streets.items():
        tot_length += value['length']
        tot_requests += value['requests']

    avg_length = tot_length/len(streets)
    avg_requests = tot_requests/len(streets)
    print("\ntotal length", tot_length, "average length", avg_length)
    print("total requests", tot_requests,
          "average requests", avg_requests)
    # ? algorithm
    intersections_clean = {}

    for intersection, intersection_streets in intersections.items():
        streets_clean = []
        for street in intersection_streets:
            if streets.get(street)['requests'] > 0:
                streets_clean.append(street)
        if len(streets_clean) > 0:
            intersections_clean[intersection] = streets_clean

    # ? output
    with open(f"../submissions/{name}.txt", "w") as f:
        f.write(f"{len(intersections_clean)} \n")  # intersections
        for intersection, intersection_streets in intersections_clean.items():
            f.write(intersection+"\n")
            f.write(f"{len(intersection_streets)} \n")
            highest_requests = max(
                list(map(lambda s: streets[s]['requests'], intersection_streets)))
            for street in intersection_streets:
                # time = 1
                time = streets.get(street)['requests']
                # if time >= D:
                #     time = D - len(intersection_streets) - 1
                if time >= avg_requests:
                    time = round(3*avg_requests)
                else:
                    time = round(avg_requests)
                if time == 0:
                    time = 1
                elif time >= D and len(intersection_streets) > 1:  # do not overflow
                    time = D-1
                f.write(f"{street} {time}\n")


# files_name = files_name[:2]
bar = ChargingBar("Solving", max=len(files_name))
# * for every input test file, solve
for name in files_name:
    cars = []
    streets = {}
    intersections = {}
    f = open(f"../inputs/{name}.txt", "r")
    lines = f.readlines()
    f.close()
    solve(name, lines)
    bar.next()
bar.finish()
