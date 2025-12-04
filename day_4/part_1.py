with open("data/data4.txt") as f:
    input=[]
    paper_rolls=0
    for line in f:
        input.append(line.strip())
    possible_directions=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    for i in range(len(input)):
        for j in range(len(input[i])):
            occupied_spots=0
            if input[i][j]=='@':
                for direction in possible_directions:
                    new_i=i+direction[0]
                    new_j=j+direction[1]
                    if 0<=new_i<len(input) and 0<=new_j<len(input[i]):
                        if input[new_i][new_j]=='@':
                            occupied_spots+=1
                if occupied_spots<4:
                    paper_rolls+=1
    print(paper_rolls)