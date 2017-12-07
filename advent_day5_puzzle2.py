import datetime

start_time = datetime.datetime.now()

offsets_file = open("puzzle5_input.txt")

offsets = []

for offset in offsets_file:
    value = int(offset)
    offsets.append(value)

end_step = len(offsets)
next_step = 0
steps = 0

while next_step < end_step:
    steps += 1
    current_step = next_step
    next_step += offsets[current_step]
    if offsets[current_step] < 3:
        offsets[current_step] += 1
    else:
        offsets[current_step] -= 1

end_time = datetime.datetime.now()

elapsed = end_time - start_time

print str(steps) + " steps in " + str(elapsed)
