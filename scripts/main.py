from progress.bar import ChargingBar

files_name = ['a', 'b', 'c', 'd', 'e', 'f']
bar = ChargingBar("Solving", max=len(files_name))

# * main function


def solve(lines):
    # ? parse start
    duration, intersections, streets, cars, bonus_points = lines[0].split(" ")
    # print(duration, intersections, streets, cars, bonus_points)
    lines = lines[1:]
    # for line in lines:
    #     print(line)
    # ? parse end


# * for every input test file, solve
for name in files_name:
    f = open(f"../inputs/{name}.txt", "r")
    lines = f.readlines()
    f.close()
    solve(lines)
    bar.next()
bar.finish()
