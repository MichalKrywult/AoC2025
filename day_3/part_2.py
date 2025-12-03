with open("data/data3.txt") as f:
    whole_joltage = 0
    for line in f:
        line = line.strip()
        batteries = len(line)
        while batteries > 12:
            removed = False
            for i in range(len(line) - 1):
                if line[i] < line[i+1]:
                    line = line[:i] + line[i+1:]
                    batteries -= 1
                    removed = True
                    break
            if not removed:
                line = line[:-1]
                batteries -= 1
        whole_joltage += int(line)
    print(whole_joltage)
