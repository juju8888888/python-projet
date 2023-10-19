#import numpy as np
# message = 'good morning'
# print(message[8])
# message = message.upper() 
# print(message[0:len(message)]) # ending point exluded and begining point include
# message = message.replace('morning', 'afternoon')
# print (message)
def exo1():
    w = input("Please, enter your weight in KG")
    while type(w)!=float:
        try :
            w = float(w)
        except :
            w = input("Please, enter your weight in KG")

    h =input("Please, enter your heigth in m")
    while type(h)!=float:
        try :
            h = float(h)
        except :
            h = input("Please, enter your heigth in m")

    bmi = w/h**2
    if bmi <18.5:
        print('underweight')
    elif bmi<25 :
        print('normal weight')
    elif bmi<30:
        print ('overweihgt')
    else:
        print('obesity')

def exo2():
    number = input("Please, enter a natural number")
    while type(number)!=int:
        try :
            number = int(number)
        except :
            number = input("Please, enter a natural number")

    number2 = input("Please, enter another natural number")
    while type(number2)!=int:
        try :
            number2 = int(number2)
        except :
            number2 = input("Please, enter another natural number")
    if number%number2==0:
        print(number/number2)
    else:
        print(f"{number} is not divisible by {number2}")

def exo3():
    number = input("Please, enter the number of unit")
    while type(number)!=int:
        try :
            number = int(number)
        except :
            number = input("Please, enter the number of unit")
    price =0
    if number <=100:
        price +=0
    elif number <=200:
        price += (number-100)*5
    else :
        price += (number-200)*10 +500
    print(f"the price is Rs{price}")

def exoprof1():
    num = int (input("Enter an integer value"))

    while num>0:
        res = num//3
        print("the integer divison of {} by 3 gives: {}".format(num,res))
        num = int (input("Enter an integer value"))
    
    print("we're done")

def exoprof2():
    num = int (input("Enter an integer value"))
    ndiv = 1

    while ndiv<num:
        res = num//ndiv
        print("the integer divison of {} by {} gives: {}".format(num,ndiv,res))
        ndiv = ndiv+1
    
    print(f"the total number of division is {ndiv}")
    print("we're done")

def exo4():
    num = int (input("Enter an integer value"))
    ndiv = 0

    while num>0:
        if num%3 == 0:
            ndiv = ndiv+1
        num-=1
        
    
    print(f"the total number of division is {ndiv}")
    print("we're done")

def exo5():
    c = 1
    sum = 0
    while c<=10:
        sum += c
        c+=1
    print ("the sum of the first ten natural number is {}".format(sum))

def exo6():
    c=1
    sum=0
    while c<=10:
        number = input("Please, enter a natural number")
        while type(number)!=int:
            try :
                number = int(number)
                sum+=number
            except :
                number = input("Please, enter a natural number")
        c+=1
    print(f"the average of the ten number is {sum/10}")

def exo7():
    name = input("Veuillez entrer votre prenom")
    c=0
    a=-1
    s =""
    while c<len(name):
        try :
            a = int(name[c])
        except:
            s+=name[c]
        if a != -1:
            break;
        c+=1
    print(s)

def exo8():
    number = input("Please, enter a natural number")
    while type(number)!=int:
        try :
              number = int(number)
        except :
                number = input("Please, enter a natural number")
    sum=0
    for i in range(1,number+1):
        sum+=i
    print(sum)

def exo9():
    number = input("Please, enter a natural number")
    while type(number)!=int:
        try :
              number = int(number)
        except :
                number = input("Please, enter a natural number")
    sum=0
    q=0
    for i in range(1,number+1):
        q = (i+1) /i**2
        sum = sum + q
    print(sum)

def exo10():
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                if i+j+k == 22:
                    print (f"{i}{j}{k}")
    print(1000)

def exo11():
    n = input("Please, enter a natural number")
    while type(n)!=int:
        try :
              n = int(n)
        except :
                n = input("Please, enter a natural number")
    val = True
    for i in range(2,n):
        if n%i == 0:
            val = False
    if val == True:
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
    
def exo12():
    n = input("Please, enter a natural number")
    while type(n)!=int:
        try :
              n = int(n)
        except :
                n = input("Please, enter a natural number")
    u1=0
    u2=1
    var=0
    for i in range(0,n):
        var = u1+u2
        u1=u2
        u2=var
    print(u2,"sara perche ti amo TIIIagoo")
    print(u2,"sara perche ti amo fanny")

def exo13():
    var = ["tiago", "fanny", "justine"]
    for i in var:
        print (i)
    print("...............................;")
    var.append("virgil")
    print(var[-1])

def exo14():
    var = ["tiago", "fanny", "justine", "virgil"]
    print(var[2::1])

def exo15():
    var = [1,2,3,4,5,6,7,8]
    sum=0.0
    for i in var:
        sum+=1/i
    print(sum)

def exo16():
    line =  input ("Enter, in a single line the temperature sparate by space")
    smooth_txt = line.split()
    temp = []
    for i in smooth_txt:
        value = float(i)
        temp.append(value)
        print(value)
    
def exo17():
    line =  input ("Enter a  natural number")
    n = int(line)
    list = []
    for i in range(n+1):
        list.append(i**2)
    for j in list:
        print(j)

def exo18():
    line1 = input ("Please, enter the name of all the student separate by space")
    namestr = line1.split()
    line2 = input ("Please, enter the name of all the students notes")
    notestr = line2.split()
    note =[]
    sum = 0
    for i in range(0, len(notestr)):
        note.append(float(i))
        sum+=i
    
    for j in range(0, len(notestr)):
        print(namestr[j],"           : ",note[j])
    
    print(f"The mean is {sum/len(note)}")

def exo19():
    
    listename=[]
    listenote=[]
    sum=0
    stud="a"
    stud=(input("Enter the student name : "))
    note=float(input("Enter his note : "))
    while(stud!=""):     
        listename.append(stud)
        listenote.append(note)
        sum+=note
        stud=(input("Enter the student name"))
        if (stud!=""):
            note=float(input("Enter his note"))
    n=len(listename)
    for i in range (n):
        print(f"{listename[i]:14} : {listenote[i]:5.1f}")
    print("---------")
    avg=sum/n
    print(f"the average is {avg:5.1f} ")
    
    #def exo20():

def exo20():
    v=[]
    n = 'eana'
    while n!='':
        n = input('please, enter numerical values')
        while type(n)!= int and n!='':
            try:
                n = int(n)
            except:
                n = input('please, enter numerical values')
        if n!='':
            v.append(n)
    somme =0
    for i in v:
        somme+=i
    print(f"La moyenne est {somme/len(v)}")

def exo21():
    str = input('Please, enter a string with all the name of the group')
    v = str.split()
    print(f'the list of people is :')
    for i in v:
        print(i)
    print(f'the number of people is {len(v)}')

def exo22():
    list_of_atom = [('H',1.008),('C',12.011),('N',14.007),('O',15.999),('S',32.065),('cl',35.453)]
    i=0
    qAtom =[]
    while i<len(list_of_atom):
        n = input(f"Please enter the number of {list_of_atom[i][0]}")
        while type(n)!= int and n!='':
            try:
                n = int(n)
            except:
                n = input(f"Please enter the number of {list_of_atom[i][0]}")
        qAtom.append(n)
        i+=1
    masse =0
    for i in range(0,len(list_of_atom)):
        masse+=list_of_atom[i][1]*qAtom[i]
    print(f"The mass of the molecule is {masse}")

def exo23():
    n = input(f"Please enter the degree maximum of the polynome")
    while type(n)!= int:
        try:
            n = int(n)
        except:
            n = input(f"Please enter the degree maximum of the polynome")
    list_of_coef =[]
    for i in range(0,n+1):
        coef = input(f"Please enter the coef a{i} of the polynome")
        while type(coef)!= int:
            try:
                coef = int(coef)
            except:
                coef = input(f"Please enter the coef a{i} of the polynome")
        list_of_coef.append(coef)
    val = input(f"Please enter tha value you want to test")
    while type(val)!= int:
        try:
            val = int(val)
        except:
            val = input(f"Please enter tha value you want to test")
    res = 0
    for i in range(0,n+1):
        res += list_of_coef[i]*(val**i)
    print(f"the result of the polynome is {res}")


#exo1()
#exo2()
#exo3()
#exoprof1()
#exoprof2()
#exo4()
#exo5()
#exo6()
#exo7()
#exo8()
#exo9()
#exo10()
#exo11()
#exo12()
#exo13()
#exo14()
#exo15()
#exo16()
#exo17()
#exo19()
#exo20()
#exo21()
#exo22()
exo23()