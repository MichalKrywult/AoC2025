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
            for k in range(1,len(j)):
                if len(j)%k!=0:
                    continue
                pattern=j[:k]
                repeat_count = len(j)//k
                if repeat_count < 2:
                    continue         
                repeated_pattern = pattern*repeat_count 
                if repeated_pattern==j:
                    invalid_ids+=int(j)
                    break                        
print(invalid_ids)
