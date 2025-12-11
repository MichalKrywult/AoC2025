def count(current, target, graph,memory):
    if current in memory:
        return memory[current]
    if current==target:
        return 1
    if current not in graph: 
        return 0
    total=0
    for neighbour in graph[current]:
        neighbour_paths=count(neighbour,target,graph,memory)
        total+=neighbour_paths
    memory[current]=total
    return total



with open("../data/data11.txt") as f:
    graph={}
    for line in f:
        line=line.strip().split(":")
        device_name=line[0]
        outputs=line[1].split(" ")
        outputs.pop(0)
        graph[device_name]=outputs
    start="you"
    end="out"
    number_of_paths=count(start, end, graph,memory={})
    print(number_of_paths)