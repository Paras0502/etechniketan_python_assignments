import keyword

# 1
print(keyword.kwlist)

# 2
x = 10
print(type(x))

# 3
t = (10, 20, 30, 40)
print(t[-1])
print(t[1])

# 4
num = int("123")
print(num + 10)

# 5
f = 12.75
print(int(f))

# 6
s1 = "Hello"
s2 = "World"
new_string = s1 + " " + s2
print(new_string)
print(len(new_string))

# 7
flag = True
print(type(flag))

# 8
tup = (10, 20, 30, 40, 50)
print(len(tup))

# 9
language = "Python"
version = 3.13
result = language + str(version)
print(result)

# 10
name = input("Enter Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
course = input("Enter Course: ")

m1 = float(input("Enter Subject 1 Marks: "))
m2 = float(input("Enter Subject 2 Marks: "))
m3 = float(input("Enter Subject 3 Marks: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

print(name)
print(age)
print(city)
print(course)
print("Percentage =", percentage)

# 11
subjects = ["Python", "SQL", "Excel", "Tableau"]

print(subjects)
print(subjects[0])
print(subjects[-1])

subjects.insert(1, "Power BI")
print(subjects)

subjects.remove("Excel")
print(subjects)

new_list = subjects.copy()
print(new_list)

new_list.sort()
print(new_list)

print("Excel" in subjects)

# 12
attendance = True
assignment_submitted = False

print(attendance or assignment_submitted)
print(attendance and assignment_submitted)
print(not attendance)