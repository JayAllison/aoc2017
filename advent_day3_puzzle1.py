position = 347991

ring = 1
root = 1
corners = [1, 1, 1, 1, 1]
midpoints = [0, 0, 0, 0]
min_distance = 0
max_distance = 0

while True:
    ring += 1
    root = 2 * (ring - 1) + 1
    square = root * root

    if position <= square:

        corners[4] = square
        corners[3] = corners[4] + 1 - root
        corners[2] = corners[3] + 1 - root
        corners[1] = corners[2] + 1 - root
        corners[0] = corners[1] + 1 - root

        midpoints[3] = corners[4] + 1 - ring
        midpoints[2] = corners[3] + 1 - ring
        midpoints[1] = corners[2] + 1 - ring
        midpoints[0] = corners[1] + 1 - ring

        min_distance = ring - 1
        max_distance = root - 1

        print "For Position " + str(position) + " - "

        print "Ring " + str(ring) + ": "
        print "  Root:      " + str(root)
        print "  Corners:   " + str(corners)
        print "  Midpoints: " + str(midpoints)
        print "  Min/Max:   " + str(min_distance) + ", " + str(max_distance)
        print

        distance = 0
        for side in range(4):
            if corners[side] <= position <= midpoints[side]:
                print str(corners[side]) + ", " + str(midpoints[side])
                distance = ring - 1 + midpoints[side] - position
                print distance
            elif midpoints[side] <= position <= corners[side+1]:
                print str(corners[side]) + ", " + str(midpoints[side])
                distance = ring - 1 + position - midpoints[side]
                print distance
        break
