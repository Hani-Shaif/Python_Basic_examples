#=====================================
#=======Python_Basic_examples=========
#========= Python Function ===========
#=====================================

print("=== Print numbers that are divisible by five and ten =======")

def divdedby(x,y):
    for n in range(1,101):
        if n%x==0 and n%y==0:
            print(n)

divdedby(5,10)


print("=== differnet between return and print=== ")

# print
    # القيمة الراجعة لم تخزن وايضا انا لا استطيع استخدام عليها العمليات الحسابية

print("=== print === ")
def mysum(x,y):
    print(x+y)
a = (mysum(5,80))
print(a) # result = None

# Return
    # القيمة ترجع واستطيع استخدام العمليات الحسابية عليها

print("=== return === ")
def mysum(x,y):
    return x+y
b = (mysum(5,20))
print(b) # result = 25

w = 100
d = w / b
print(d)

"""
    Define a Function
    def function_name(parameters):
       function body
    return[expression]
"""
print("=====================================")
print("------- Calling a Function ---------")
def print_str(str):
    print(str)
print_str("Hani")
print("=====================================")
print("------- Function Arguments ---------")

"""
    Function Arguments :
    you can call a function by using the following types of formal arguments :
        - required arguments # متغير مطلوب للدالة ضروري
        - keyword arguments # تساعدني في تغير المعاملات عند 
        - default arguments # يمة افتراضية ناخذها في حالة عدم اعطاء قيم
        - variable-length arguments
"""
print("=====================================")
print("------- required arguments ---------")

def printme(str):
    print(str)
    return
printme(str) # result: <class 'str'>

print("=====================================")
print("------- Keyword arguments ---------")

def printme(str):
    print(str)
    return
printme(str= "Welcome") # result: Welcome
print("===========")

def printme(x,y):
    print(x+y)
    print(x)
    return
printme(y = 12,x = 22) # result: Welcome
print("=====================================")
print("------- Default arguments ---------")

def printme(name = "Ahmed" , age = 31):
    print('name: '+ name)
    print('age: ', age)
    return
printme(name = "Sami" ,age = 20)
printme("Ali" )
print("===============")
def printme(age = 31):
    print(age)
    print('age: ', age)
    return
printme(age = 20)
printme(33)
printme()
print("=========R======")
def printme(x,y=0):# x = 0,y =0 default value
    print(x+y)
    return
a = printme(100)
print(a)

print("=====================================")
print("------- Variable Length arguments ---------")

  ##  لاحقا ندرسه


print("=====================================")
print("---------- Lambda  -----------")

mysum = lambda x,y : x + y
print(mysum(10,20)) # doing return default
c = (mysum(10,20))
print(c)
print("-------------")
printme = lambda x=50,y=20 : x  + y
print(printme())

print("=====================================")
print("---------- Scope  -----------")
# scope : a  variable is only available from inside the region it is created.
# المتغير متاح فقط من داخل المنطقة التي تم إنشاؤها فيه.

# Global
# لعنصر المعرف خارج الدولة يكون عام

# Local
# العنصر المعرف داخل الدالة يبقى خاص ولا يمكننا استخدامه خارجها

x = 10
print(x)# 10  Global
def number():
    x = 20 # Local
    print(x) # 20
number() 
print(x) # 10
print("-------")
# Converts the local value to global
x = 10
print(x)# 10  Global
def number():
    global x #Converts the local value to global
    x = 20 # Local
    print(x) # 20
number() 
print(x) # 20





























































 























































  































































