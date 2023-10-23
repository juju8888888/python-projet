# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 10:27:33 2023

@author: legal
"""
import pandas as pd
name = 'names.txt'
f_name = open(name)
for name in f_name:
    if "a" in name:
        name = name.strip()
        print("Hello {}".format(name))
print(f_name)

#the basics: 

# f= open("ligne.txt", "r") #reading
f= open("lignes.txt", "w") #writing
# f= open("text.txt", "a") #appending
# f= open("text.txt", "r+") #reading and writing
file = open("lignes.txt")
print(f.name)
print(f.mode)
print(file)
# f.close 

#Reading Files (Context Manager):
with open("text.txt", "r") as f:
    pass

with open("text.txt", "r") as f:
    # Small Files:
    f_contents = f.read()
    print(f_contents)
    

with open("text.txt", "r") as f:
    # Small Files:
    f_contents = f.readlines()
    print(f_contents)
    
'''Avec f.read(), tout le contenu est stocké dans une seule chaîne de caractères, 
tandis qu'avec f.readlines(), le contenu est stocké dans une liste où chaque élément 
est une ligne du fichier.'''

with open("text.txt", "r") as f: 
    f_contents = f.readline()
    print(f_contents, end = '')
    f_contents = f.readlines()
    print(f_contents, end = '')
    f_contents = f.readlines()
    print(f_contents, end = '')
    f_contents = f.readlines()
    print(f_contents, end = '')
    
with open("text4.txt", "w")as f:
    f.write("Hello Word")
    f.seek(5)
    f.write("---")
    f.write("R")
    
print(open("text4.txt"))

with open("test2.txt", "w")as f:
    val = 'names'
    val1 = '10'
    val2 = 'niamh'
    f.write(val+' '+val1+ '\n'+val2)

with open("text.txt", "r") as rf:
    with open("text copy.txt", "w")as wf: 
        for line in rf:
            wf.write(line)
'''Pour chaque ligne du fichier source (rf), 
la ligne est écrite dans le fichier de destination (wf). 
Ainsi, le contenu complet du fichier source est copié dans 
le fichier de destination.'''

with open("The_toad.jpg", "rb")as rf:
    with open("toad_copy.jpg", "wb")as wf:
        for line in rf:
            wf.write(line)
        
with open("test2.txt", "wb") as f:
    
    
    