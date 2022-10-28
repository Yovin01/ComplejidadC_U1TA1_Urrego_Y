import matplotlib.pyplot as plt
def codigo_1 (n):
    a=0
    for j in range (1, n+1):
        a+=a+j
        for k in range (n, 0,-1):
            a-=1
            a*=2
    return a

def codigo_2():
    a=0
    a-=1
    a*=2

def codigo_3(n):
    a=0
    for j in range (1,n+1):
        for k in range (1, n+1):
            a+=a +(k*j)
    return a
#Graficas    
def cod_1 (n):
    return 3*n + 1
def cod_2():
    return 3
def cod_3(n):
    return n*n +1
n = range(0 , 50)
plt.plot(n, [cod_1(i) for i in n])
plt.plot(n, [cod_2() for i in n])
plt.plot(n, [cod_3(i) for i in n])
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.xlim(0, 15)
plt.ylim(0, 50)
plt.show() 


