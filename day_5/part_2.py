with open("data/data5.txt") as f:
    ranges=[]
    for line in f:
        line=line.strip().split("-")
        if line==[""]:
            break
        line=(int(line[0]),int(line[1]))
        ranges.append(line)
    ranges.sort()
    current_start=ranges[0][0]
    current_end=ranges[0][1]
    new_ranges=[]
    for start, end in ranges:
        if start <= current_end + 1:
            current_end=max(current_end,end)
        else:
            new_ranges.append((current_start,current_end))
            current_end=end
            current_start=start
    new_ranges.append((current_start,current_end))
    all_fresh_ids=0
    for i in new_ranges:
        all_fresh_ids+=(i[1]-i[0]+1)
    print(all_fresh_ids)
    


