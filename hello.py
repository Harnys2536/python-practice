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
     total = total + i
print(total)

#challenge 5
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

def reverse_text(text):
    result = ""
    for letter in text:
        result = letter + result
    return result
print(reverse_text("Hello, World!"))

student = ("fatimah", "python", "85")
name, course, score = student
print(f"{name} scored {score} in {course}.")

numbers = {1,2,3,4}
numbers.add(5)
numbers.add(3)
print(len(numbers))

student = {
    "name": "fatimah",
    "age": 24,
    "course": "python"
}

student = {
    "name": "Aisha",
    "age": 20,
    "score": 85
}

student = {
    "name": "Aisha",
    "age": 20,
    "score": 85
}

student = {
    "name": "Aisha",
    "age": 20
    print("name" in student)
}

scores = {
    "Aisha": 75,
    "Fatimah": 95,
    "Maryam": 60,
    "Khadijah": 88
}
for name, score in scores.items():
    if score >= 85:
        print(name)

scores = {
    "Aisha": 75,
    "Fatimah": 95,
    "Maryam": 60,
    "Khadijah": 88
}
total = 0
for value in scores.values():
    total += value
print(total)

scores = {
    "Aisha": 75,
    "Fatimah": 95,
    "Maryam": 60,
    "Khadijah": 88
}
highest_score = 0
for value in scores.values():
    if value > highest_score:
        highest_score = value
print(highest_score)
average = 0
total = 0
for value in scores.values():
    total += value
average = total / len(scores)
print(average)