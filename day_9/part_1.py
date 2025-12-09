with open("data/data9.txt") as f:
    lines=[]
    for line in f:
        line=line.strip().split(",")
        lines.append((line[0],line[1]))
    max_area=-1
    for i in range(len(lines)):
       point=lines[i]
       for j in range(i+1,len(lines)):
            point2=lines[j]
            length=abs(int(point[0])-int(point2[0]))+1
            width=abs(int(point[1])-int(point2[1]))+1
            if width*length>max_area:
                max_area=width*length

print(max_area)

