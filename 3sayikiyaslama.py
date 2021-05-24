# -*- coding: utf-8 -*-

a=int(input("1. Sayiyi giriniz: "))
b=int(input("2. Sayiyi giriniz: "))
c=int(input("3. Sayiyi giriniz: "))

if a>b>c:
  print(a,">",b,">",c)
elif a>c>b:
  print(a,">",c,">",b)
elif b>a>c:
  print(b,">",a,">",c)
elif b>c>a:
  print(b,">",c,">",a)
elif c>a>b:
  print(c,">",a,">",b)
elif c>b>a:
  print(c,">",b,">",a)
elif a==b>c:
  print(a,"==",b,">",c)
elif a>c==b:
  print(a,">",c,"==",b)
elif b==a>c:
  print(b,"==",a,">",c)
elif b>c==a:
  print(b,">",c,"==",a)
elif c==a>b:
  print(c,"==",a,">",b)
elif c>b==a:
  print(c,">",b,"==",a)
input()
    
    
    
    
