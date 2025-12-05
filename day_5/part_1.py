with open("data/data5.txt") as f:
    ranges=[]
    ingredients=[]
    end=0
    for line in f:
        line=line.strip().split("-")
        if line==[""]:
            end=1
            continue
        if end==0:
            ranges.append(line)
        else:
            ingredients.append(line)
    fresh=0
    for i in ingredients:
        for j in ranges:
            if int(i[0]) > (int(j[0])-1)  and int(i[0]) < (int(j[1])+1):
                fresh+=1
                break
    print(fresh)