DIRECTIONS = {"NORTH":"SOUTH", "SOUTH":"NORTH", "EAST":"WEST", "WEST":"EAST"}


def dirReduc(dirs):
    travel = []

    for d in dirs:
        if travel and DIRECTIONS[d] == travel[-1]:
            travel.pop()
        else:
            travel.append(d)

    return travel