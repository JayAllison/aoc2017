# global value to count how many recursive calculations we needed to make
square_count = 0

# I've hand-calculated the first nine, because the geometry of the first two rings is different than the rest
# using a map for caching the results of the calculations, which literally makes a 1,000,000x improvement
value_cache = {0: 0, 1: 1, 2: 1, 3: 2, 4: 4, 5: 5, 6: 10, 7: 11, 8: 23, 9: 25}


def get_root(ring):
    root = 2 * (ring - 1) + 1
    return root


def get_ring(position):
    ring = 1
    while True:
        ring += 1
        root = get_root(ring)
        square = root * root
        if position <= square:
            return ring, root


def get_corners(root):
    square = root * root
    corners = [1, 1, 1, 1, 1]
    corners[4] = square
    corners[3] = corners[4] + 1 - root
    corners[2] = corners[3] + 1 - root
    corners[1] = corners[2] + 1 - root
    corners[0] = corners[1] + 1 - root
    return corners


def get_touching_squares(position):
    touching = []

    if position > 1:
        ring, root = get_ring(position)
        corners = get_corners(root)

        # the position is always touching the previous position
        touching.append(position-1)

        # the only condition where the position is touching the two previous positions
        # is if the previous position is a corner
        for side in range(5):
            offset = 1
            if side == 0:
                # special case due to the way I track corners: corner 0 is actually corner 4 from the previous ring,
                # not corner 0 of the current ring
                offset = 2
            if position - offset == corners[side]:
                touching.append(position-2)

        for side in range(4):
            # find the side which we are on in the current ring
            if corners[side] <= position <= corners[side+1]:
                # now look at the inner ring
                inside_ring = ring - 1
                inside_root = get_root(inside_ring)
                inside_corners = get_corners(inside_root)

                inside_delta = position - corners[side] - 1
                inside_adjacent = inside_corners[side] + inside_delta

                # the position is always touching one ahead inside unless one ahead inside is around the corner
                corner_value = inside_corners[side+1]
                if side == 3:
                    # special case: for the last corner, the next value goes adjacent to it before the spiral starts
                    corner_value += 1
                if inside_adjacent + 1 <= corner_value:
                    touching.append(inside_adjacent+1)

                # the position is always touching the adjacent inside position unless the position is past the corner
                # or, 1st special case - the position is touching inside adjacent IFF the position is 4th corner
                # or, 2nd special case - the inside adjacent is actually inner corner 0
                #   (because that's on the inner inner ring)
                if (inside_adjacent <= inside_corners[side+1] or position == corners[4]) \
                        and inside_adjacent != inside_corners[0]:
                    touching.append(inside_adjacent)

                # the position is always touching one behind unless one behind inside is around the corner
                corner_value = inside_corners[side]
                if side == 0:
                    # special case due to the way I track corners: corner 0 is actually corner 4 from the previous ring,
                    # so actual corner 0 of the current ring is +1
                    corner_value += 1
                if inside_adjacent > corner_value and inside_adjacent > 1:
                    touching.append(inside_adjacent-1)
                break

    return touching


def get_value(position):
    global square_count
    if position in value_cache:
        # square_count += 1
        return value_cache[position]
    else:
        result = 0
        touching = get_touching_squares(position)
        for square in touching:
            result += get_value(square)
        square_count += 1
        value_cache[position] = result
        return result


def run_touching_tests():
    test_results = (
        (10, [9, 2]),
        (11, [10, 9, 3, 2]),
        (12, [11, 3, 2]),
        (13, [12, 3]),
        (14, [13, 12, 4, 3]),
        (15, [14, 5, 4, 3]),
        (16, [15, 5, 4]),
        (17, [16, 5]),
        (18, [17, 16, 6, 5]),
        (19, [18, 7, 6, 5]),
        (20, [19, 7, 6]),
        (21, [20, 7]),
        (22, [21, 20, 8, 7]),
        (23, [22, 9, 8, 7]),
        (24, [23, 10, 9, 8]),
        (25, [24, 10, 9]),
        (26, [25, 10]),
        (27, [26, 25, 11, 10]),
    )

    failed = 0
    for test in test_results:
        test_position = test[0]
        actual = get_touching_squares(test_position)
        expected = test[1]
        if actual != expected:
            print "ERROR! " + str(test_position)
            print "Expected: " + str(expected)
            print "Actual:   " + str(actual)
            print
            failed += 1

    print "Total Failed = " + str(failed)


def main():
    global square_count
    square_count = 0
    target = 347991
    for the_position in range(100):
        the_value = get_value(the_position)
        print str(the_position) + " -> " + str(the_value)
        if the_value > target:
            print "Value at position " + str(the_position) + " = " + str(the_value) + \
                  " (" + str(square_count) + " squares calculated)"
            break


main()
