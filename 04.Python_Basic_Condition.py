#=====================================
#=======Python_Basic_examples=========
#====== Python  If Condition =========
#=====================================

# if else
print("===== if else =====")

x = 100
if x == 100:
    print("x = 100")
else:
    print("x != 100")

# if ..elif..else
print("===== if ..elif..else =====")

x = 200
if x == 100:
    print("x = 100")
elif x > 100:
    print("X > 100")
elif x > 50:
    print("X > 50")
else:
    print(x)

# Nested if
print("===== Nested if ===== ")
x = 100
if x > 100:
    print("x = 100")
    if x == 50:
       print("x = 50")
else:
    print(x)

# If whith boolean operators
print("===== If whith boolean operators ===== ")
print("===== and ===== ")
name = "Hani"
age = 30
if name == "Hani" and age == 30:
    print("Welcome Hani")
else:
    print("You atr not Hani")

print("===== or ===== ")
x = 10
y = 30
if x == 10 or y == 20:
    print("Welcome")
else:
    print("hello")

# Single If Statement
print("===== Single If Statement ===== ")
x = 10
if x == 10: print(x)

# True condition false 
print("===== True condition false ===== ")
print("===== Example-1 ===== ")
x = 20
print("x > 20") if x > 20 else print("x != 20")
print("===== Example-2 ===== ")
age = 16
isAllowed = True if age > 18 else False
print(isAllowed)
print("===== Example-3 ===== ")
username = "admen"
age = 15
print("true") if username == "admen" and age >= 18 else print("false")

print("===== Condition in , not in ===== ")
names = ["Hani","Ahmed","Ali"]
if "Ahmed" in names:   ## in
    print("Ahmed found")
if "Sari" not in names:    # not in
    print("Sari not found")

print("===== Condition all([]) , any ===== ")
print("===== all([... ,... ,...]) == and ===== ")
x,y,z = 5,6,7
if all([x==5,y==6,z==7]):     #  list[]
    print("Welcome")
print("===== any([... ,... ,...])== or ===== ")
x,y,z = 5,6,7
if any([x==5,y==12,z==11]):     #  list[]
    print("Hello")

print("===== Example 1 =====")
a = 1
b = 2
if a == 1 and b == 2:
    print(True) # will print
if a == 0 or b == 2:
    print(True) # will print
if not(a == 1 and b == 3):
    print(True) # will print 
if a != 0 and  b != 3:
    print(True) # will print

print("===== Example 2 =====")
x = 1
if x in (0,2,4):
    print("Match")
else:
    print("Not Found")


















    


















































