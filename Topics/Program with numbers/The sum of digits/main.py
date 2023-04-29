# put your python code here
number = int(input())
firstDigit = number // 100
secondDigit = (number % 100) // 10
thirdDigit = number % 10
print(firstDigit + secondDigit + thirdDigit)
