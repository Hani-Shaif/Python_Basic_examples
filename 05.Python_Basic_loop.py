#=====================================
#=======Python_Basic_examples=========
#======= Python  While , For =========
#=====================================

#=============== While ===============
x = 1
while x < 6:
    print(x)
    x += 1;
print("========= Infinte Loop ========")
#we use this loop in GUI to render all the GUI apps on screen

# x = 0
# while x < 10:
    # print(x)  # يطبع صفر لمالا نهاية
x = 0  # Single While statement
while x < 10: print(x); x += 1 # الفاصلة المنقوطة تنهي السطر

print("========= Nested While Loop ========")
x = 1
while x <= 5:
    y = 1
    while y <= 10:
        print(f" {x} X {y} = {x * y}") # f = format string 
        y += 1
    print("------------")
    x += 1

print("========= For لكل ========")
for x in "python":  #لكل جزء من كل ومعناها في المثال لكل حرف من كلمة بايثون
    print(x)
print("-------------")
x = [1,3,5,6,7,8]

for y in x:
    print(y) # يطبع الاعداد كلا بسطر

# الفرق بين while and for
  # while تكرار
  # for تكرار لقيم مرتبة او  كلمات

print("===== For range() =====")
# range(start=0 , end, step=1)
  # range(10)  => start = 0 end = 10 step = 1 ==> 0,1 ,,,, 9
  # range(2,10)  => start = 2 end = 10 step = 1 ==> 2 ,,, 9
  # range(2,10,3)  => start = 2 end = 10 step = 3 ==> 2,5,8

print("===== Example-1 =====")
for x in range(1,11): print(x) # print 1 2 3 ..10
print("===== Example-2 =====")
for x in range(1,11,2): print(x) # print 1 3 5 7 9
print("===== Example-2 =====")
x = 1
while x <= 5:
    y = 1
    while y <= 10:
        print(f"{x} X {y} = {x * y}")
        y += 1
    print("-----------")
    x += 1
#=================================    
print("===== Example-3 => جدول الضرب =====")

for x in range(1,6):
    for y in range(1,11):
        print(f"{x} X {y} = {x * y}")
    print("-------------")
    
print("===== Loop with List =====")

# Loop with List
print("===== Example-1 =====")
info = ["Hani","Yemen",30]
for x in info:
    print(x)
print("----------------")
print("===== Example-2 =====")

infoFamily = [["Hani",30],["Ali",27],["Hassan",22]]
for x in infoFamily:
    for y in x:
      print(y)
    print("----")
    
print("----------------")
print("===== Example-3 =====")
numbers = [[1,2,3],[4,5,6],[7,8,9]]
for x in numbers[0]:
    print(x)

print("--------------------")
print("===== For VS While الفروق بينهم =====")
# for
    # يفضل استخدامها عندما يكون عدد التكرارات معروفة
    # نقدر نعمل  تكرار داخل قائمة اونص 
    #
# while
    # التكرار يستمر حتى يصبح الشرط خطأ
    # كثر مرونة وتستخدم بشكل اكبر
    #

print("===== Loop Control Statements Break,Continue,pass =====")
print("===== Break وقف=====")
x = 0
while x <= 10:
    print(x)
    x += 1
    if x == 4:
        break # وقف التكرار ولكن لا يوقف البرنامج



print("===== Continue اطلع كمل ولكن لا تطبعني=====")

x = 0
while x <= 10:
    print(x) # 0 1 2 3 5 6 7 8 9 10
    x += 1
    if x == 6:
        continue

print("------------")

print("===== pass  =====")

for x in range(10):
    pass # لاحقا ساكتب الكود هنا 
print("----------------------")
print("-----------Lopps Examples-1 -----------")
print("Number\tSquare")
print("--------for------")
for x in range(0,11):
    #y = x**2  // print(x , "\t" ,x**2) 
    print(x ,"\t", x**2 ) # \t = tab
                          # \n new line
print("--------------------")
print("Number\tSquare")
print("-------while-------")
x = 1
while x < 11:
    print(x, "\t" , x*x)
    x += 1

print("-----------Lopps Examples-2 -----------")

start = int(input("Enter Start : "))# string
end   = int(input("Enter end : "))
print("Number\tSquare")
print("--------------")
for x in range(start,end): # end = 11 or end+1
    print(x, "\t" ,x*x)

print("----------------------")
rows = int(input("Enter Row : "))# 5  
cols   = int(input("Enter Col : "))
for x in range(rows):
    for y in range(cols):
        print("*", end="")
    print()

print("--------------Examples-4 --------------")  

for x in range(8):
    for y in range(x+1):
        print("*",end='')# defoult = end='\n'  
    print()

print("----------------")
for x in range(8):
    for y in range(x+1):
        print('*',end='') # اطبعي نجمة وانزلي سطر جديد
    print()

print("----------------")
















 























































  































































