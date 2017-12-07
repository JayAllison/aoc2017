offsets_file = open("puzzle5_input.txt")

offsets = []

for offset in offsets_file:
    value = int(offset)
    offsets.append(value)

end = len(offsets)
next = 0
steps = 0

while next < end:
    steps += 1
    current = next
    next += offsets[current]
    offsets[current] += 1

print steps
