# 4.	Create a function simple_interest(p, r, t) to calculate simple interest.

def simple_intress(p,r,t):
    return ((p*r*t)/100)

print('simple intress for')
p=100
r=3.4
t=12

print('prncpile :',p)
print('time',t)
print('rate',r)

print("Simple Intress",simple_intress(p,r,t))

