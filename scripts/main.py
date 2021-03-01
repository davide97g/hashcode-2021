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
            'length': int(L)
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
        # print(streets_names)
    # ? parse end

    # ? algorithm

    # ? output
    with open(f"../submissions/{name}.txt", "w") as f:
        f.write(f"{len(intersections)} \n")  # intersections
        for intersection in intersections:
            f.write(intersection+"\n")
            intersection_streets = intersections.get(intersection)
            f.write(f"{len(intersection_streets)} \n")
            for street in intersection_streets:
                time = 1
                f.write(f"{street} {time}\n")


# files_name = files_name[:1]
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
