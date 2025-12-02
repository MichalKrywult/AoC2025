position = 50
count_zeroes = 0
with open("data/data1.txt") as f:
    for line in f:
        side = line[0]
        steps = int(line[1:])
        for _ in range(steps):
            if side == 'L':
                position = (position - 1) % 100
            else:
                position = (position + 1) % 100
            if position == 0:
                count_zeroes += 1
print(count_zeroes)
