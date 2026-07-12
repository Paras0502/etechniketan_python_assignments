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


