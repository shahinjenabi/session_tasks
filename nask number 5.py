# delta

a = int(input("add a number ofr a"))
b = int(input("add a number ofr b"))
c = int(input("add a number ofr c"))

delta = b * b - 4 * a * c

print("delta:", delta)

if delta > 0 :
    print(-b + (delta ** 0.5)/ 2 * a)
elif delta == 0 :
    print( print(-b - (delta ** 0.5)/ 2 * a))
else:
    print("none real roots")

# pyisic

start = float(input("add start point :"))
end = float(input("add end point :"))
speed = float(input("add speed :"))

if end > start :
    distance = end - start
else:
    distance = start - end 
time = distance / speed

print("distance :", distance)
print("time :", time)



# average 

total = 0 

count = 0 
print("rule : if you add a negetive number its the end")
number = int(input(" add a number :"))

while number >= 0:
    total = total + number
    count = count + 1
    number = int(input("next number "))

if count > 0 :
    average = total / count
    print("numbers count :", count)
    print("average :", average)
else:
    print("no number")

# calculator

a = float(input("add a number :"))

b = float(input("add a number :"))

operator = input("add adjective operator :")

if operator == "+":
    result = a + b
    print("result :", result)
elif operator == "-":
    result = a - b
    print("result :", result)
elif operator == "*":
    result = a * b
    print("result :", result)
elif operator == "/":
    result = a / b
    print("result :", result)
elif operator == "**":
    result = a ** b
    print("result :", result)
elif operator == "%":
    result = a % b
    print("result :", result)
else:
     print("fail")

# fobonacci

n = int(input("how many number you whant"))

a = 0 
b = 1
count = 0

while count < n:
    print(a)
    next = a + b 
    a = b 
    b = next 
    count = count + 1



# gol ya pooch

hands = ["right","left"]

gol = ["gol","gol"]

choose = input("choose a hand")

if choose == hands[0]:
    gol[0] = "gol"
elif choose == hands[1]:
    gol[1] = "gol"

    guess = input("guess which hand")

if guess == "left" and gol[0] == "gol":
    print("nice one")
elif guess == "right" and gol[1] == "gol":
    print("good luck")
else:
    print("so sad you lose")


# rock paper scissor

player1 = input("rock paper scissor :")
    
player2 = input("rock paper scissor :")

if player1 == player2:
    print("equel")

elif player1 == "rock" and player2 == "scissor":
    print("player1 wins")
elif player1 == "scissor" and player2 == "paper":
    print("player1 wins")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins")
elif player2 == "rock" and player1 == "scissor":
    print("player2 wins")
elif player2 == "scissor" and player1 == "paper":
    print("player2 wins")
elif player2 == "paper" and player1 == "scissor":
    print("player2 wins")

# esm famil

latter = input("enter your latter :")

name = input("name :")
family= input("family :")
city = input("city :")
country = input("country")
car = input("car: ")
celebrity = input("celebrity :")
food = input("food :")
animal = input("animal")


print("name :", name)
print("family :", family)
print("city :", city)
print("country :", country)
print("car: ",car )
print("celebrity :", celebrity)
print("food :",food )
print("animal :", animal)







