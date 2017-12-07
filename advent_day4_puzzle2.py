passphrase_file = open("puzzle4_input.txt")

total_count = 0
error_count = 0
good_count = 0

for line in passphrase_file:
    total_count += 1
    words = line.split()
    for word1 in words:
        found = 0
        letters1 = sorted(list(word1))
        for word2 in words:
            letters2 = sorted(list(word2))
            if letters1 == letters2:
                found += 1
        if found > 1:
            error_count += 1
            break

good_count = total_count - error_count
print str(good_count) + "/" + str(error_count) + "/" + str(total_count)
