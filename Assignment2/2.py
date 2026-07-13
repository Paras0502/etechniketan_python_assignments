#33

s1 = "practice is important to perfectly learn python"

result = []

for i in range(len(s1)):
    if s1[i] == "p":
        result.append(i)

print(result)

#34

l = ["aba", "abc", "121", "aa", "madam", "hello", "1991"]

count = 0

for i in l:
    if len(i) > 2:
        if i == i[::-1]:
            count += 1

print(count)

#35

s1 = "How much wood would a woodchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo his wife"

words = s1.split()

result = []

for word in words:
    if len(word) >= 4:
        if word[0] == "w" or word[0] == "W":
            if word not in result:
                result.append(word)

print(result)

#36

s = input("Enter a string: ")

d = {}

for ch in s:
    if ch in d:
        d[ch] = d[ch] + 1
    else:
        d[ch] = 1

print(d)

#37

products = {
    "soap":50,
    "oil":200,
    "laptop":60000,
    "phone":25000,
    "mouse":500
}

max_price = 0
product = ""

for i in products:
    if products[i] > max_price:
        max_price = products[i]
        product = i

print("Costliest product is", product)

#38

d = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys_to_remove = ["name", "salary"]

for key in keys_to_remove:
    del d[key]

print(d)

#39

num = int(input("Enter a number: "))

while num >= 0:
    if num == 0:
        print("Blast!")
    else:
        print(num)

    num = num - 1

#40

print("Welcome to Grade Checker")

choice = "yes"

while choice == "yes":

    marks = float(input("Enter marks: "))

    if marks >= 90:
        print("Grade A+")

    elif marks >= 80:
        print("Grade A")

    elif marks >= 70:
        print("Grade B")

    elif marks >= 60:
        print("Grade C")

    elif marks >= 50:
        print("Grade D")

    else:
        print("Fail")

    choice = input("Continue? (yes/no): ")

print("Thank You")

#41

a = int(input("Enter a number: "))

if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")

elif a % 3 == 0:
    print("Fizz")

elif a % 5 == 0:
    print("Buzz")

else:
    print(a)

#42

password = "python123"

attempt = 1

while attempt <= 3:

    user = input("Enter Password: ")

    if user == password:
        print("Access Granted")
        break

    else:
        print("Wrong Password")

    attempt = attempt + 1

if attempt == 4:
    print("Access Denied")

#43

import random

choice = "yes"

while choice == "yes":

    guess = input("Enter heads or tails: ")

    toss = random.choice(["heads", "tails"])

    print("Coin:", toss)

    if guess == toss:
        print("You guessed it right!")

    else:
        print("Wrong Guess!")

    choice = input("Play Again? (yes/no): ")

print("Thanks for Playing!")