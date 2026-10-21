print("Hello, Python in VS Code!")
# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix
print("Welcome to the Debugging Lab!")
name = input("Enter your name: ")
print("Hello " + name + "!" + " Let's calculate your test scores.")
scores = [85, 90, 78, 88, 92]
total = 0
for score in scores:
    total = total + score
average = total / len(scores)
print("Your average score is:", average)
highest = scores[0]
for s in scores:
    if s > highest:
        highest = s
print("Your highest score was:", highest)
