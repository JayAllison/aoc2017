memory_bank = [14, 0, 15, 12, 11, 11, 3, 5, 1, 6, 8, 4, 9, 1, 8, 4]
# memory_bank = [0, 2, 7, 0]

results = set()


def get_memory_bank_string():
    global memory_bank
    s = ""
    for i in range(len(memory_bank)):
        s += str(memory_bank[i]) + "_"
    return s


def find_fullest_memory_bank():
    global memory_bank
    max_value = 0
    position = 0
    for i in range(len(memory_bank)):
        if memory_bank[i] > max_value:
            position = i
            max_value = memory_bank[i]
    return position


def reallocate_memory_bank(bank):
    global memory_bank
    length = len(memory_bank)
    value = memory_bank[bank]
    memory_bank[bank] = 0
    for i in range(value):
        position = (bank + i + 1) % length
        memory_bank[position] += 1


count = 0

while True:

    count += 1
    current_value = (get_memory_bank_string())
    results.add(current_value)
    reallocate_memory_bank(find_fullest_memory_bank())
    current_value = get_memory_bank_string()
    if current_value in results:
        print count
        break
