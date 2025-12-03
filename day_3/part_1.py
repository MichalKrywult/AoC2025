with open("data/data3.txt") as f:
    whole_joltage=0
    for line in f:
        first_battery=0
        first_battery_index=0
        second_battery=0
        line=line.strip()
        for i in range(len(line)-1):
            if first_battery<int(line[i]):
                first_battery=int(line[i])
                first_battery_index=i
        for j in range(first_battery_index+1,len(line)):
            if second_battery<int(line[j]):
                second_battery=int(line[j])
        joltage=int(str(first_battery)+str(second_battery))
        whole_joltage+=joltage
    print(whole_joltage)