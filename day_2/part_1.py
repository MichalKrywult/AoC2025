ranges=[]
invalid_ids=0
with open("data/data2.txt") as f:
    line = f.readline().strip().split(',')
    for r in line:
        start=int(r.split('-')[0])
        end=int(r.split('-')[1])
        ranges.append((start,end))
    for i in ranges:
        start=int(i[0])
        end=int(i[1])
        for j in range(start,end+1):
            j=str(j)
            copy=j
            copy2=j
            half=(len(str(j))//2)
            if len(str(j))%2==0:
                first_half=str(j)[:half]
                second_half=str(j)[half:]
            else:
                first_half=str(j)[:half+1]
                second_half=str(j)[half+1:]
            if first_half==second_half:
                invalid_ids+=int(j)
print(invalid_ids)