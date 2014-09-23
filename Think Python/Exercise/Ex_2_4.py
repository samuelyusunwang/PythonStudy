# Ex 2.4

#1
r = 5
pi = 3.1415926

V = 4/3 * pi * r**3
print(V)

#2
p = 24.95
discountRate = 0.4
shipping1 = 3
shipping2 = 0.75
n = 60

cost = p*(1-discountRate)*n + shipping1*1 + shipping2*(n-1)

print(cost)

#3
T1 = (1+1)*(8+15/60)
T2 = 3*(7+12/60)

T = T1+T2

H = (52+T)//60 + 6
M = 52+T - (52+T)//60*60
print(H,M)
