count passing students 
scores = {
    "Aisha": 75,
    "Fatimah": 95,
    "Maryam": 60,
    "Khadijah": 88
}
# passing_students = 0
# for score in scores.values():
#     if score >= 80:
#         passing_students += 1
# print(f"Number of passing students: {passing_students}")

highest_score = 0
highest_student = ""
for key, value in scores.items():
    if value > highest_score:
        highest_score = value
        highest_student = key
print(f"{highest_student}: {highest_score}")

# Recursion 
#  What recursion is
# Base cases
#  Recursive calls
#  Recursion going downward
#  Returning back upward
#  Recursive counting
#  Recursive sums
#  Factorial recursion
def count_down(cups):
    if cups <= 0:
        print("Done!")
        return
    print("Cup: " + str(cups))
    count_down(cups - 1)

count_down(3)


def count_up(n):
    if n == 0:
        return

    count_up(n - 1)
    print(n)

count_up(5)

def countdown(n):
    if n == 0:
        print("Blast off!")
        return

    print(n)
    countdown(n-1)
    # call the function again
countdown(5)

def sum_numbers(n):
    if n == 0:
        return 0
    return n + sum_numbers(n-1)

print(sum_numbers(5))

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))