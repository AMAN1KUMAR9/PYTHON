import random
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase="abcdefghijklmnopqrstuvwxyz"
symbols="!@$%&*^#"
no_s="1234567890"
u=random.choice(uppercase)
print(u)
v=random.choice(uppercase)
print(v)
l=random.choice(lowercase)
print(l)
m=random.choice(lowercase)
print(m)
s=random.choice(symbols)
print(s)
w=random.choice(symbols)
print(w)
n=random.choice(no_s)
print(n)
b=random.choice(no_s)
print(b)
o=[u,v,l,m,s,w,n,b]

random.shuffle(o)
for i in o:
    print(i,end="")
# random password generator


