# read test.txt
with open("test.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line[0])
    file.close()
