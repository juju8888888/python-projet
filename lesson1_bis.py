# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:45:25 2023

@author: legal
"""

liste =['joe biden','hgshgl','soighsgh', 'glsjlkg','sldgj', 'skgs']
print(liste[2])
liste.append('kjghsjj')
print(liste)

liste.remove('joe biden')
print(liste)
liste[4] = 'juju'
print(liste)

smooth = [3.14, 7, -2+3j, 'water', False, [1,2]]
print(smooth[::2]) #ça print tous les deux
print(smooth[5][1])
print(smooth[3][4])
print(smooth[1::2])
print(smooth[-4:-2])

sum = 0
for i in range(1,10):
    sum += 1/i
    print(f"{sum:.2f}")
    
line = "Temperature is 298.15 K before combustion"
words = line.split(' ') #○but you can also split sur une lettre en particulier
words = line.split('a')
line = input("Enter, in a single line and separated by spaces, the desired temperature values: ")
smooth_t = line.split()
print("List is nox {}".format(smooth_t))
temp = []
for element in smooth_t:
    value = float(element)
    temp.append(value)
print("The final list is {}".format(temp))

listname = []
listgrade = []
sum = 0
name = "name"
while name != "":
    name = str(input("Enter the name of the student: "))
    if name != "":
        listname.append(name)
        grade = float(input("Enter the grade of the student: "))
        listgrade.append(grade)
for e in listgrade:
    sum = sum+e
moyenne = sum/len(listgrade)
print("The mean is {}".format(moyenne))
for i in range(len(listname)):
    print(listname[i], end = " ")
    print(listgrade[i])

# correction exercice 

name = input("Enter student name: ")
grade = input("Enter grade out of 10: ")
names = []
grades = []
sum = 0
while name!= "":
    names.append(name)
    grades.append(grade)
    sum += float(grade)
    name = input("Enter student name: ")
    grade = input("Enter grade out of 10: ")
average = sum/len(grades)
for i in range (len(names)):
    print("{:14}{:5.1f}".format(names[i], float(grades[i])))
print(average)

#S07_7 Variable length list of numeric values

number = input("Enter a number")
sum = 0
nsum = 0
average = 0
numbers = []
while number!= "":
    numbers.append(number)
    sum = sum + 1
    nsum = number + nsum
average = nsum/sum
for i in range (0,len(numbers)):
    print(numbers[i]+" ")
print("the average is {}".format(average))
    
