with open ("data/data6.txt") as f:
    all_lines=[]
    for line in f:
        line=line.strip().split()
        all_lines.append(line)
lines=all_lines[:-1]
last_line=all_lines[-1]
results=[]
for i in range(len(last_line)):
    if last_line[i]=="*":
        temp=1
        for k in range(4):
            temp*=int(lines[k][i])
        results.append(temp)
    else:
        temp=0
        for k in range(4):
            temp+=int(lines[k][i])
        results.append(temp)
grand_total=0
for r in results:
    grand_total+=r
print(grand_total)