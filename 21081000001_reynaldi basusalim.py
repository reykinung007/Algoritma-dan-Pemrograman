# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 07:13:25 2022

@author: USER
"""

#judul
print("Progam mengurutkan 3 bilangan terkecil ke terbesar")
#siapkan variabel
print("masukkan 3 bilangan yang diinginkan")
a=int(input("masukkan nilai1 ="))
b=int(input("masukkan nilai2 ="))
c=int(input("masukkan nilai3 ="))
#input nilai
if a<b and a<c:
    if b<c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b<a and b<c:
    if a<c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a<b:
        print(c, a, b)
    else:
        print(c, b, a)
         
