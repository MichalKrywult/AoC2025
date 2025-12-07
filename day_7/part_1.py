with open("data/data7.txt") as f:
    lines=[]
    for line in f:
        line=line.strip()
        temp=[]
        for j in line:
            temp.append(j)
        lines.append(temp)
    start=-1
    for i,k in enumerate (lines[0]):
        if k=="S":
            start=i
    split_count=0
    max_width=len(lines[0])
    active={start}
    for i in range(1,len(lines)):
        new=set()
        for j in active:
            symbol=lines[i][j]
            if symbol==".":
                new.add(j)
            if symbol=="^":
                split_count+=1
                if j+1<max_width:
                    new.add(j+1)
                if j-1>-1:
                    new.add(j-1)
        active=new
    print(split_count)