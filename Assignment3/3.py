#8

def introduce(name, age=None):

    if age == None:
        print("My name is", name)
        print("My age is secret.")

    else:
        print("My name is", name)
        print("I am", age, "years old.")

introduce("John",20)
introduce("John")


#9

def drop_minimum(*args):

    numbers = list(args)

    minimum = min(numbers)

    numbers.remove(minimum)

    return numbers

print(drop_minimum(5,-2,8,4,-5,7,10))


#10

def find_max(a,b,c):

    return max(a,b,c)

def main():

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))

    print(find_max(x,y,z))

main()


#11

add = lambda a,b : a+b

print(add(10,20))


#12

fahrenheit = lambda c : c*9/5+32

print(fahrenheit(25))


#13

try:

    file = open("student.txt","x")

    file.write("Python is easy to learn.\n")
    file.write("File handling is important.\n")
    file.write("Practice makes perfect.")

    file.close()

except FileExistsError:
    print("File already exists")

except Exception:
    print("Some error occurred")


#14(a)

file = open("student.txt","r")

print(file.read())

file.close()


#14(b)

file = open("student.txt","r")

count = 1

for line in file:

    print("Line",count,":",line)

    count += 1

file.close()


#15

file = open("student.txt","r")

text = file.read()

words = text.split()

print("Total words:",len(words))

file.close()


#16

file = open("student.txt","a")

file.write("\nPython file handling becomes simple with practice.")

file.close()


#17

numbers = [7,4,0,-2,3]

print(numbers)

try:

    index = int(input("Enter index: "))

    print(numbers[index])

except IndexError:

    print("Invalid Index")


#18

def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    print(a/b)