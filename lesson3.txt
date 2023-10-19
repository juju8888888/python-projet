import numpy as np

def exo1():
    key =('ten', 'twenty', 'thirty')
    value = (10,20,30)
    v = dict(zip(key, value))
    print(v)

def exo2():
    employee =['kelly','emma']
    defauts = {'direction': 'developer',"salary": 8000}
    dicta = dict.fromkeys(employee,defauts)
    print(dicta)

def exo3():
    dico = {'a':100,'b': 200,'c':300}
    value = False
    for i in dico.values():
        if i == 200:
            value =True
    print(value)

def exo4():
    dicto = {'emp1':{'name':'john','salary':7500},
             'emp2':{'name':'Emma','salary':8000},
             'emp3':{'name':'brad','salary':8500}} 
    dicto ['emp3']['salary'] = 500
    print (dicto)

def exo5():
    atommic_dico = {'H': (1,14,20),
                    'HE': (2,1,4),
                    'Li': (3,453,1603),
                    'Be': (4,1560,2742),
                    'B': (5,2349,4200),
                    'C': (6,3915,3915),
                    'N': (7,63,77),
                    'O': (8,54,90),
                    'F': (9,53,85),
                    'Ne': (10,25,27)
                    }
    temp = float(input('Please enter the temperature of the atom in kelvin'))
    element = input('Please enter the element')
    if temp<=atommic_dico[element][1]:
        print('solid')
    elif temp>=atommic_dico[element][2]:
        print('gaz')
    else:
        print('liquid')

def exo6():
    a = []
    test="jtm"
    for i in range(0,5):
        str=input(f'Please enter the {i+1} number')
        while type(test)!=int:
            try:
                test = int(str)
            except:
                str = input(f'Please enter the {i+1} number')
        a.append(test)
        test= 'jtm'
    max = a[0]
    min = a[0]
    for j in a:
        if j<min:
            min = j
        if j>max:
            max = j
    print(f'The maximum is {max} and the minimum is {min}')

def exo7():
    nb_str = input('Enter a number')
    nb ='jtm'
    while type(nb) != int:
        try:
            nb = int(nb_str)
        except:
            nb_str = input('Enter a number')
    if nb%2 == 0:
        print(f"{nb} is Even")
    else:
        print(f"{nb} is Odd")

def exo7bis():
        try:
            nb = int(input("Please enter a number"))
            if nb%2 == 0:
                print(f"{nb} is Even")
            else:
                print(f"{nb} is Odd")
        except ValueError as error:
            print(error)
            
def exo8():
    nb = 0
    while type(nb) == int:
        try:
            nb = int(input('Enter a number'))
            if nb%2 == 0:
                print(f"{nb} is Even")
            else:
                print(f"{nb} is Odd")
        except:
            nb ='str'

def exo9():
    test2= True
    while test2 == True:
        try:
            nb = int(input('Enter a number'))
            test = False
            for i in range(2,nb):
                if nb%i ==0:
                    test = True
            if test == False:
                print(f"{nb} is prime")
            else:
                print(f"{nb} is not prime")
        except ValueError as error:
            test2 = False
            print (error)
    
def exo10():
    y = np.linspace(10,30,dtype='int32')
    y[4] = 1
    print (y)
#exo1()
#exo2()
#exo1()
#exo2()
#exo3()
#exo4()
#exo5()
#exo6()
#exo7()
#exo7bis()
#exo8()
#exo9()
exo10()