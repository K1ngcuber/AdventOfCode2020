numbers = []

with open("door1_input.txt","r") as f:
    for line in f.readlines():
        numbers.append(int(line))
numbers.sort()

restart = True
big_index = len(numbers)-1
result = 0

while restart:
    for i in range(len(numbers)):
        result = numbers[i]+numbers[big_index]
        if (result) > 2020: 
            big_index-=1
            break
        elif result < 2020:
            for j in range(len(numbers)):
                if numbers[j] == numbers[i]:
                    continue
                result += numbers[j]
                if result > 2020:
                    break
                elif result == 2020:
                    print(numbers[big_index]*numbers[i]*numbers[j])
                    restart = False
                    break
                    
        
