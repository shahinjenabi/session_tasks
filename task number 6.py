# TASK1

# def delta(a , b ,c):
#     delta = b * b - 4 * a * c

# for i in range(3):
   

def analize():
    numbers_text = []

    print("add your number if you whant stop prees enter :")
    while True:
        n = input("number :")
        if n == "":
            break
        numbers_text = numbers_text + [n]

numbers = []
for i in numbers_text:
    numbers = numbers + [int(i)]

# average

total = 0

count = 0

for number in numbers :
    total = total + number
    count = count + 1
average = total / count

# biggest
 
biggest = number[0]
for number in numbers:
    if number > biggest:
        biggest = number


# smallest 

smallest = number[0]
for number in numbers:
    if number < smallest:
        smallest = number

# variance
variance = 0 
for number in numbers:
    variance = variance + (number - average) ** 2
variance = variance / count

return average , biggest , smallest , variance







