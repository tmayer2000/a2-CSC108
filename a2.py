from typing import List

def get_average_elevation(m: List[List[int]]) -> float:
    """
    Returns the average elevation across the elevation map m.

    Examples
    >>> get_average_elevation([])
    0
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> get_average_elevation(m)
    5.0
    >>> m = [[1,2,2,5],[4,5,4,8],[7,9,9,1],[1,2,1,4]]
    >>> get_average_elevation(m)
    4.0625
    """
    count = 0
    total = 0
    if len(m) == 0:
        return 0
    for sublist in m:
        for num in sublist:
            total += num
            count += 1
    return total/count


def find_peak(m: List[List[int]]) -> List[int]:
    """
    Given an non-empty elevation map m, returns the cell of the
    highest point in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [9,8,7],
             [5,4,6]]
    >>> find_peak(m)
    [1,0]
    >>> m = [[6,2,3],
             [1,8,7],
             [5,4,9]]
    >>> find_peak(m)
    [2,2]
    """
    cell = [0, 0]
    list_count = 0
    num_loc = 0
    highest_num = 0
    while list_count <= (len(m) - 1):
        while num_loc <= (len(m) - 1):
            if m[list_count][num_loc] > highest_num:
                highest_num = m[list_count][num_loc]
                cell.pop(1)
                cell.pop(0)
                cell.append(list_count)
                cell.append(num_loc)
            num_loc += 1
        list_count += 1
        num_loc = 0
    return cell


def is_sink(m: List[List[int]], c: List[int]) -> bool:
    """
    Returns True if and only if c is a sink in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> is_sink(m, [0,0])
    True
    >>> is_sink(m, [2,2])
    True
    >>> is_sink(m, [3,0])
    False
    >>> m = [[1,2,3],
             [2,1,3],
             [5,4,3]]
    >>> is_sink(m, [1,1])
    True
    """
    feet = len(m) - 1
    if not m:
        return False
    i = c[0]
    j = c[1]
    test = m[i][j]
    if i == 0 and j == 0:
        east = m[i][j + 1]
        south = m[i + 1][j]
        southeast = m[i + 1][j + 1]
        if test <= east and test <= south and test <= southeast:
            return True
        else:
            return False
    elif i == feet and j == 0:
        north = m[i - 1][j]
        northeast = m[i - 1][j + 1]
        east = m[i][j + 1]
        if test <= north and test <= east and test <= northeast:
            return True
        else:
            return False
    elif i == feet and j == feet:
        west = m[i][j - 1]
        north = m[i - 1][j]
        northwest = m[i - 1][j - 1]
        if test <= north and test <= west and test <= northwest:
            return True
        else:
            return False
    elif i == 0 and j == feet:
        south = m[i + 1][j]
        southwest = m[i + 1][j - 1]
        west = m[i][j - 1]
        if test <= south and test <= west and test <= southwest:
            return True
        else:
            return False
    elif i == 0 and (j != 0 and j != feet):
        south = m[i + 1][j]
        southeast = m[i + 1][j + 1]
        southwest = m[i + 1][j - 1]
        east = m[i][j + 1]
        west = m[i][j - 1]
        if test <= east and test <= south and test <= west and test <= southeast and test <= southwest and test <= southeast:
            return True
        else:
            return False
    elif i == feet and (j != 0 and j != feet):
        northeast = m[i - 1][j + 1]
        northwest = m[i - 1][j - 1]
        east = m[i][j + 1]
        west = m[i][j - 1]
        north = m[i - 1][j]
        if test <= east and test <= north and test <= west and test <= northeast and test <= northwest:
            return True
        else:
            return False
    elif (i != 0 and i != feet) and j == 0:
        northeast = m[i - 1][j + 1]
        southeast = m[i + 1][j + 1]
        north = m[i - 1][j]
        south = m[i + 1][j]
        east = m[i][j + 1]
        if test <= east and test <= north and test <= south and test <= southeast and test <= northeast and test <= southeast:
            return True
        else:
            return False
    elif (i != 0 and i != feet) and j == feet:
        northwest = m[i - 1][j - 1]
        southwest = m[i + 1][j - 1]
        west = m[i][j - 1]
        north = m[i - 1][j]
        south = m[i + 1][j]
        if test <= north and test <= south and test <= west and test <= southwest and test <= northwest:
            return True
        else:
            return False
    else:
        east = m[i][j + 1]
        west = m[i][j - 1]
        north = m[i - 1][j]
        south = m[i + 1][j]
        southeast = m[i + 1][j + 1]
        southwest = m[i + 1][j - 1]
        northeast = m[i - 1][j + 1]
        northwest = m[i - 1][j - 1]
        if test <= east and test <= north and test <= south and test <= west and test <= southeast and test <= southwest and test <= northeast and test <= southeast and test <= northwest:
            return True
        else:
            return False


def find_local_sink(m: List[List[int]], start: List[int]) -> List[int]:
    """
    Given a non-empty elevation map, m, starting at start,
    will return a local sink in m by following the path of lowest
    adjacent elevation.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]]
    >>> find_local_sink(m, [0,0])
    [3,3]
    >>> m = [[ 5,70,71,80],
             [50, 4, 5,90],
             [60, 3,35, 2],
             [ 1,72, 6, 3]]
    >>> find_local_sink(m, [0,3])
    [2,3]
    >>> m = [[9,2,3],
             [6,1,7],
             [5,4,8]]
    >>> find_local_sink(m, [1,1])
    [1,1]
    """
    begin = start
    while is_sink(m, begin) == False:
        feet = len(m) - 1
        i = begin[0]
        j = begin[1]
        if i == 0 and j == 0:
            east = m[i][j + 1]
            south = m[i + 1][j]
            southeast = m[i + 1][j + 1]
            adj = [east, south, southeast]
            loc = adj.index(min(adj))
            if loc == 0:
                begin = [i, j + 1]
            elif loc == 1:
                begin = [i + 1, j]
            else:
                begin = [i + 1, j + 1]
        elif i == feet and j == 0:
            north = m[i - 1][j]
            northeast = m[i - 1][j + 1]
            east = m[i][j + 1]
            adj = [north, east, northeast]
            loc = adj.index(min(adj))
            if loc == 0:
                begin = [i - 1, j]
            elif loc == 1:
                begin = [i, j + 1]
            else:
                begin = [i - 1, j + 1]
        elif i == feet and j == feet:
            west = m[i][j - 1]
            north = m[i - 1][j]
            northwest = m[i - 1][j - 1]
            adj = [north, west, northwest]
            loc = adj.index(min(adj))
            if loc == 0:
                begin = [i - 1, j]
            elif loc == 1:
                begin = [i, j - 1]
            else:
                begin = [i - 1, j - 1]
        elif i == 0 and j == feet:
            south = m[i + 1][j]
            southwest = m[i + 1][j - 1]
            west = m[i][j - 1]
            adj = [south, west, southwest]
            loc = adj.index(min(adj))
            if loc == 0:
                begin = [i + 1, j]
            elif loc == 1:
                begin = [i, j - 1]
            else:
                begin = [i + 1, j - 1]
        elif i == 0 and (j != 0 and j != feet):
            south = m[i + 1][j]
            southeast = m[i + 1][j + 1]
            southwest = m[i + 1][j - 1]
            east = m[i][j + 1]
            west = m[i][j - 1]
            adj = [east, south, west, southeast, southwest]
            loc = adj.index(min(adj))
            if loc == 0:
                begin = [i, j + 1]
            elif loc == 1:
                begin = [i + 1, j]
            elif loc == 2:
                begin = [i, j - 1]
            elif loc == 3:
                begin = [i + 1, j + 1]
            else:
                begin = [i + 1, j - 1]
        elif i == feet and (j != 0 and j != feet):
            northeast = m[i - 1][j + 1]
            northwest = m[i - 1][j - 1]
            east = m[i][j + 1]
            west = m[i][j - 1]
            north = m[i - 1][j]
            adj = [north, east, west, northeast, northwest]
            loc = adj.index(min(adj))
            if loc == 0:
                begin = [i - 1, j]
            elif loc == 1:
                begin = [i, j + 1]
            elif loc == 2:
                begin = [i, j - 1]
            elif loc == 3:
                begin = [i - 1, j + 1]
            else:
                begin = [i - 1, j - 1]
        elif (i != 0 and i != feet) and j == 0:
            northeast = m[i - 1][j + 1]
            southeast = m[i + 1][j + 1]
            north = m[i - 1][j]
            south = m[i + 1][j]
            east = m[i][j + 1]
            adj = [north, east, south, northeast, southeast]
            loc = adj.index(min(adj))
            if loc == 0:
                begin = [i - 1, j]
            elif loc == 1:
                begin = [i, j + 1]
            elif loc == 2:
                begin = [i + 1, j]
            elif loc == 3:
                begin = [i - 1, j + 1]
            else:
                begin = [i + 1, j + 1]
        elif (i != 0 and i != feet) and j == feet:
            northwest = m[i - 1][j - 1]
            southwest = m[i + 1][j - 1]
            west = m[i][j - 1]
            north = m[i - 1][j]
            south = m[i + 1][j]
            adj = [north, south, west, southwest, northwest]
            loc = adj.index(min(adj))
            if loc == 0:
                begin = [i - 1, j]
            elif loc == 1:
                begin = [i + 1, j]
            elif loc == 2:
                begin = [i, j - 1]
            elif loc == 3:
                begin = [i + 1, j - 1]
            else:
                begin = [i - 1, j - 1]
        else:
            east = m[i][j + 1]
            west = m[i][j - 1]
            north = m[i - 1][j]
            south = m[i + 1][j]
            southeast = m[i + 1][j + 1]
            southwest = m[i + 1][j - 1]
            northeast = m[i - 1][j + 1]
            northwest = m[i - 1][j - 1]
            adj = [north, east, south, west, northeast, southeast, southwest, northwest]
            loc = adj.index(min(adj))
            if loc == 0:
                begin = [i - 1, j]
            elif loc == 1:
                begin = [i, j + 1]
            elif loc == 2:
                begin = [i + 1, j]
            elif loc == 3:
                begin = [i, j - 1]
            elif loc == 4:
                begin = [i - 1, j + 1]
            elif loc == 5:
                begin = [i + 1, j + 1]
            elif loc == 6:
                begin = [i + 1, j - 1]
            else:
                begin = [i - 1, j - 1]
    return begin


def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    """
    Given an elevation map m, a start cell s, a destination cell d, and
    the an amount of supplies returns True if and only if a hiker could reach
    d from s using the strategy dscribed in the assignment .pdf. Read the .pdf
    carefully. Assume d is always south, east, or south-east of s. The hiker
    never travels, north, west, nor backtracks. 

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,4,3],
             [2,3,5],
             [5,4,3]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    True
    >>> can_hike_to(m, [0,0], [0,0], 0)
    True
    >>> can_hike_to(m, [0,0], [2,2], 3)
    False
    >>> m = [[1,  1,100],
             [1,100,100],
             [1,  1,  1]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    False
    >>> can_hike_to(m, [0,0], [2,2], 202)
    True
    """
    if s == d:
        return True
    spot = s
    i = spot[0]
    j = spot[1]
    while supplies > 0:
        if spot == d:
            break
        i = spot[0]
        j = spot[1]
        if i == d[0]:
            supplies = supplies - abs((m[i][j] - m[i][j + 1]))
            if supplies < 0:
                return False
            spot = [i, j + 1]
        elif j == d[1]:
            supplies = supplies - abs((m[i][j] - m[i + 1][j]))
            if supplies < 0:
                return False
            spot = [i + 1, j]
        else:
            south = m[i + 1][j]
            east = m[i][j + 1]
            next = [east, south]
            pos = next.index(min(next))
            if pos == 0:
                supplies = supplies - abs((m[i][j] - m[i][j + 1]))
                if supplies < 0:
                    return False
                spot = [i, j + 1]
            else:
                supplies = supplies - abs((m[i][j] - m[i + 1][j]))
                if supplies < 0:
                    return False
                spot = [i + 1, j]
    if spot == d:
        return True
    return False


def rotate_map(m: List[List[int]]) -> None:
    """
    Rotates the orientation of an elevation map m 90 degrees counter-clockwise.
    See the examples to understand what's meant by rotate.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> rotate_map(m)
    >>> m
    [[3,3,3],
     [2,3,4],
     [1,2,5]]
    >>> m = [[5,9,1,8],
             [2,4,5,7],
             [6,3,3,2],
             [1,7,6,3]]
    >>> rotate_map(m)
    >>> m
    [[8,7,2,3],
     [1,5,3,6],
     [9,4,3,7],
     [5,2,6,1]]
    """
    new = {}
    for x in range(len(m)):
        new[x] = []
    for sublist in m:
        for c in range(len(sublist)):
            new[c].append(sublist[c])
    for key in new:
        m.pop(key)
        m.insert(0, new[key])


"""
You are not required to understand or use the code below. It is there for
curiosity and testing purposes.
"""
def create_real_map()-> List[List[int]]:
    """
    Creates and returns an elevation map from the real world data found
    in the file elevation_data.csv.

    Make sure this .py file and elevation_data.csv are in the same directory
    when you run this function to ensure it works properly.
    """
    data = open("elevation_data.csv")
    m = []
    for line in data:
        m.append(line.split(","))
    data.close()
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m



    
    










    
