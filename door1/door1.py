numbers = []

with open("door1_input.txt","r") as f:
    for line in f.readlines():
        numbers.append(int(line))
numbers.sort()

restart = True
big_index = len(numbers)-1

while restart:

    for i in range(len(numbers)):
        if (numbers[i]+numbers[big_index]) > 2020: 
            big_index-=1
            break
        
        elif numbers[i]+numbers[big_index] == 2020:
            print(numbers[i]*numbers[big_index])
            restart = False
            break
        
