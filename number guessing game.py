import random
n = input("your name : ")
t = random.randint(1, 10)
s = 1
u = input("number : ")
v = int(u)
while v != t :
  u = input("number : ")
  v = int(u)
  s = s + 1
if v == t :
  print(s, "-", n,"you are winer!!!!!!!!!!!!!!!!")
