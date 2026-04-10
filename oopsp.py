#oops is know object oriented programming system they are divide into six
#class, object , inheritance, encapusaltion , abstraction, polymorphism

# oops terminilogy: arrtibutes are also know as data memebers or variables
# behavior also know as member function are method


# # class is know as blueprint of object  it is defined with class keyword 

# class sankar():
#     print("hello world")
    
    
# object : object is entity which staes and behavior using object we can acces methods and variables it is instances of class


#constructor is special methos in a class that is automatically called when a new object is callled 
# it mainely used for intilize the object 

# def__init__(self,__)

# construcot is defined 2 types they are default and paramterized 

# default : a constructor doesnot accpet any arguments exept self 
# it used when you dont need to pass value while creating a object 




# class student:
#     def __init__(self):
#         self.name="sankar"
# s=student()
# print(s.name)
 
 
 
# # parametrized constructor:a constructor that accept arguments beside self 
# used to intialize object with specfic values 


# class student:
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age 

# c= student("sai", 76)
# print(c.name)
# print(c.age)


# class family:
#     def __init__(self, name, gender, age, phonenumber):
#         self.a=name
#         self.b=gender
#         self.c=age
#         self.d=phonenumber
    
#     def data(self):
#         print("name:", self.a)
#         print("gender:", self.b)
#         print("age:", self.c)
#         print("phonenumber:", self.d)
        
# name=input("Enter the name: ")
# gender=input("Enter the gender:")
# age=int(input("Enter the age:"))
# phonenumber=int(input("Enter the phonenumber:"))
        
# data_obj = family(name, gender, age, phonenumber)
# data_obj.data()



# inheritance:it allows us to define a class that inherits all the methods and properties from another class


# parent class is the class being inherited from also base class
# child clas is the class that inherits from another class also called derived class

# they are divided into five types they are 
# single , multiple, hierachal, hybrid , multihierical 

#single inheritance : a child class inherits from only parent class is callled single inheritance 

# class parent:
#     def show_parent(self):
#         print("this is parent class")

# class child(parent):
#     def show_child(self):
#         print("this is child class")
        
# obj = child()
# obj.show_parent()
# obj.show_child()


# In this code the child was inherits  from the one parent class


# muiltiple inheritance:a child class inherits from more than one parenet class

# class father:
#     def outputf(self):
#         print("this is father class")
# class mother:
#     def outputm(self):
#         print("this is mother class")


# class child(father, mother):
#     def output(self):
#         print("this is child class")
# s=child()
# s.outputf()
# s.outputm()
# s.output()


#multilevel inheritance : it is called as chanin of inheritance 


# class grandfather():
#     def output(self):
#         print("this is grand father")

# class father(grandfather):
#     def outputf(self):
#         print("this is father")
        
# class child(father):
#     def outputc(self):
#         print("this is child")
# family=child()
# family.output()
# family.outputf()
# family.outputc() 




# hierichal inheritance: multiple child class inherits from the same parent 

# class suseela():
#     def output(self):
#         print("this is mother")

# class sudha(suseela):
#     def outputd(self):
#         print("this is sudha daughter class")
        
# class sanki(suseela):
#     def outputs(self):
#         print("this is sanki son class")
    
# a=sudha()
# a1=sanki()
# a.output()
# a.outputd()
# a1.output()
# a1.outputs()

# hybrid : a combination of two are more types of inheritance 



# class tata():
#     def output(self):
#         print("this is tata family")

# class dady(tata):
#     def outputd(self):
#         print("this is dady")

# class atha(tata):
#     def outputt(self):
#         print("this is atha")

# class avva(dady, atha):
#     def outputa(self):
#         print("this is avva")

# family=avva()
# family.output()
# family.outputd()
# family.outputt()
# family.outputa()








# polymorphism:
# poly-------> many
# morph------->forms
#  mixing os many form is called polymorphism 
 
 
# they are 2 types of polymorphism they are complie type and run time polymophism 


# compile time---(Static)
# it is not supported in python 
# it is method over loading i
# it is assocaited with function overloading 
#       function overloading is not suppoted in python we cant define the type of paremter thaty it is not supoorted 
#       we can use default and dispactch

# the complie time polymorphis has same name and differnt paremetrs 
# the complier decides at complie time which methos to run 
# code execution is fast 


# class math:
#     def add(Self, a, b, c):
#         return a+b+c

# obj=math()
# print(obj.add(2))
# print(obj.add(2,3))
# print(obj.add(2,3,4))


# by overcoming this we can use default arguments and dispatch from third party 


# class math:
#     def add(Self, a=0, b=0, c=0):
#         return a+b+c

# obj=math()
# print(obj.add(2))
# print(obj.add(2,3))
# print(obj.add(2,3,4))


 
# class math:
#     def add(self, *args):
#         return sum(args)

# obj = math()
# print(obj.add(2))
# print(obj.add(2,3))
# print(obj.add(2,3,4))

#but we can simulate it using default argumnets **args   **kwargs






# runtime ----(dynamic)
# it is suppoted in pyhton 
# it is method overridding
 
# it is not required to decalre the type of variable in pyhton when assiigin the value for it
# code execution is slow

# to define a method in subclass with same mname to ove ride in superclass

# methos over ridding methos name must be samein parent and child class paremeter must be same 

# class methodoverridding():
#     def output(self):
#         print("this is parent class")

# class child(methodoverridding):
#     def output(self):
#         print("this is child class")
# obj=child()
# obj.output()

# output: this prinbts only a child class 


# self:self class used to acces the cureent class only 



# we use super() keyword in pyhton used to call the methos from the parent in a child classit 
# alllows you to acces and extend the functionality of inheritance methods 

# class methodoverridding():
#     def output(self):
#         print("this is parent class")
# class child(methodoverridding):
#     def output(self):
#         print("this is child class")
#         super().output()
# obj=child()
# obj.output()






# encapsulation it is mechanism of wrapping the data and code actionable on the data methods together as
# a single unit 
# in this they are 3 types they are 

# public , protected , private

# public : accessible for any one 

# class sankar:
#     def __init__(self, name , age):
#         self.name=name
#         self.age=age

# p = sankar("sai", 34)
# print(p.name)
# p.age=88
# print(p.age) 

# Accessible outside the class

# ✅ Can be modified directly
# 
# Public members are variables or methods that can be accessed from anywhere (inside or outside the class).



#protected: accessible inside of the class and subclass should not be  accesed by out side 

# class Parent:
#     def _show(self):   # protected method
#         print("This is Parent class")

# class Child(Parent):
#     def _show(self):   # overriding (polymorphism)
#         print("This is Child class")

# obj = Child()
# obj._show()   # Calls Child version # “I have an object of Child, so first check inside Child class”

# class gfather:
#     def __init__(self):
#         print("this is gfather class")

# class father(gfather):
#     def __init__(self):
#         print("this is father class")
# o = father()


# private : not directly accesible outside of class


# class grandfather():
#     def __init__(self,a):
#         self .__y = a
#         print(self. __y)

# class father(grandfather):
#     def output1(self):
#         print(self.__y)

# class child2(father):
#     def output2(self):
#         print("child2", self.__y)
        
# obj = child2(12)
# obj.display2()
# obj.display1()



# local varible is defined inside the function it only can accesed with in the function
# it can be created when function starts it can be destroyed when function ends 


# def my_fun():
#     x=10
#     print("Inside function")
# my_fun()


# global varible: a global varible is defined outside of all fucntion 
# it can accesed any where i  the program inside or outside function 
# but is you want the modify the inside the function you must use the globalkeyword
hmm