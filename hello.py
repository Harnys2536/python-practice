#challenge 1
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#challenge 2
score = int(input("Enter your score: "))
if score >= 70:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
else:
    print("F")

    #challenge 3
number = int(input("Enter a number: "))
for i in range(number):
    if i % 3 == 0:
        print(i)

#challenge 4
number = int(input("Enter a number: "))
total = 0
for i in range(0,number + 1):
     total = total + 1
print(total)