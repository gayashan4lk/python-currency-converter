#  write your code here 
file = open('../Summer/data/dataset/input.txt', 'r')
count = 0
for line in file:
    if line == 'summer\n':
        count = count + 1
file.close()
print(count)
