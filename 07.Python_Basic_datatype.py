#=====================================
#=======Python_Basic_examples=========
#===== Python Basic Data Type ========
#=====================================

print(" ====== different between ''/ ""/ ''' ''' ======== ")
# تستخدم جميعها عن طباعة النصوص
# '' ""  لا يوجد  اي فوق  بينهم
#''' '''  تستخدم للتعليق من عدة اسطر

print(" ====== Python String Formatting ======== ")
print(" ====== String ======== ")
f_name = "Hani"
l_name = "Ali"
print(f_name+ " "+ l_name) # Hani Ali
print(f_name,l_name) # Hani Ali
print(f"{f_name} {l_name}") # Hani Ali    \n new line
print('Hani\tAli')
print('Hani\nAli') # Hani
                   # Ali
text = "To make sure a string will display as expected"
print(text.upper()) # جعل الحروف كبيرة
print(text.lower()) # جعل الحروف صغيرة
print(text.title()) # اول حرف من كل كلمة كبير
print(text.replace("will","not will")) # تغير الكلمة بكلمة اخرىاو العبارات
print(text.split()) # فصل الكلمات او الجمل مع تحدد نوع الفاصل

t = "Welcome hani"
print(t[0]) # w
print(t[1]) # e
print(t[-1]) # i   من النهاية 
print(t[-3]) # a

print(t[:5]) # Welco   // اذا القطع من الصفر مو لازم نكتبه
print(t[0:5]) # Welco    //slice شريحة
print(t[6:13]) # e hani
print(t[6:]) # e hani  //اذا القطع للنهاية مو لازم نكتب النهاية
#another functions: https://www.w3schools.com/python/python_ref_string.asp

print(" ====== List ======== ")


















