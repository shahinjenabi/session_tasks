# task

A = int(input("add your first number"))

B = int(input("add your second number"))

C = int(input("add your third number"))

D = int(input("add your fourth number"))

# average

total = A + B + C + D

average = total / 4

print(average)

# maximum

biggest = A

if B > biggest:
    biggest = B 
if C > biggest:
    biggest = C
if D > biggest:
    biggest = D 

print(biggest)  

# minimum

smallest = A
if B < smallest:
    smallest = B
if C < smallest:
    smallest = C
if D < smallest:        
    smallest = D 

print(smallest)

# variance
# variane = v 

va = (A - average) ** 2
vb = (B - average) ** 2
vc = (C - average) ** 2
vd = (D - average) ** 2

variance = (va + vb + vc + vd)  / 4

print(variance)





