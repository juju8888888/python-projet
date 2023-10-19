# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:11:32 2023

@author: legal
"""

import matplotlib.pyplot as plt 
import numpy as np

x  = np.linspace(-2,2,101)
y = x**2
print(x)

plt.plot(x,y) #vector x,y

plt.show()

x = np.linspace(0,3*np.pi, 500)
plt.plot(x, np.sin(x**2))
plt.plot(y) # take number of points
plt.title('A simple chirp')
plt.show()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xlim(-1.5,1.5)
plt.ylim(-0.5,2.5)
plt.plot(x,y)
plt.show()


plt.legend()

# S0_1 Trigonometric function
n = int(input("combien de valeurs "))
x = np.linspace(-1,1,n)
y = np.cos(2*np.pi*x)
plt.plot(x,y)
plt.title('Body function (2pix)')
plt.show()
plt.savefig("cospix.png")

while True:   
    try :
        n = int(input("combien de valeurs "))
        x = np.linspace(0,4,n)
        y = np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x)
        plt.plot(x,y)
        plt.title('Body function (2pix)')
        plt.show()
        plt.savefig("cospix.png")
    except ValueError as e : 
        print(e)
    except Exception as e: 
        print(e)
        

# Isotherm of an ideal gas

n=int(input("quel est le nombre de point"))
t = int(input("Enter the temperature"))
R = 0.08206
Vm = np.linspace(2,10,n)
plt.xlabel("Molar volume (L/mol)")
plt.ylabel("Pressure(atm)")
plt.title("Isotherm (ideal gas)")
p = R*t/Vm
plt.plot(Vm, p)
plt.savefig("isotherm.jpeg")
plt.show()

# modification previous exercize

n= int(input("quel est le nombre de point "))
c = int(input("quel est le nombre de courbe que tu veux "))
t = int(input("Enter the temperature "))
R = 0.08206
x = np.linspace(2,10,n)
for i in range (0,c):
    t = int(input("Enter the temperature"))
    p = R*t/x
    plt.plot(x, p)
    
plt.xlabel("Molar volume (L/mol)")
plt.ylabel("Pressure(atm)")
plt.title("Isotherm (ideal gas)")
plt.savefig("isotherms.jpeg")
plt.show()

#Gaussian function 
n = int(input("combien de valeurs "))
f = int(input("what is the first value "))
l = int(input("what is the last value "))
x0 = int(input("Choose the value for x0 "))
s = float(input("Choose the value for s "))
x = np.linspace(f, l,n)
y = 1/(np.sqrt(2))*np.exp((-1/2)*(x-x0)**2/s**2)
plt.plot(x,y)
plt.title('Gaussian function')
plt.show()
plt.savefig("Gaussian.png")

