map_object = []
trees = []
col = 0

with open("door3_input.txt","r") as f:
    map_object = list(map(lambda line: line.strip(), f.readlines()))

for i in range(0,len(map_object),2):
    if(map_object[i][col%31] == '#'):
        trees.append((i,col))
    col+=1

print(len(trees))

########################
#        Part 2        #
########################

#Right 1, down 1. (86)
#Right 3, down 1. (187)
#Right 5, down 1. (75)
#Right 7, down 1. (89)
#Right 1, down 2. (44)

print(86*187*75*89*44)