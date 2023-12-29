def loop():
    for x in range(10): 
        print (x)
        if x == 3:
            return
        
loop();
####################
print("#"*30)
#pass function as parameter

def twice(y , x):
    return y(y(x))    


def mul(x):
    return x**2   

out = twice(mul , 2)
print(out)

####################
print("#"*30)
#define function inside another

def function1(x):
    def function2(y):
        return y + 2
    return 3 * function2(x)
    
function1(2)
# call the function
# a = function1(2)
# print (a)

# b = function2(2.5) # error
# print (b)

##############################
#global vs local 

x = 1
def add_one (x):
    x = x + 1
    # add one to the local x
    return x


# call the function
y = add_one (x)
print(x)
print(y)


def f1():
    global x
    x = x + 1
    return f"x from f1: {x}"

def f2():
    return f"x from f1: {x+2}"

def f3():
    x = 5
    return f"x from f1: {x+1}" 


x = 0
print(f1()) #global
print(f2()) #global
print(f3()) #local

###############################
print("#"*30)
def func1 (x, a = 1, b = 2 ):
    
    """this function take tree variables. The
    first one have to be supplied, however the
    other two have a default values"""
    return x + a - b


print(help(func1))
print(func1(20))
###############################
print("#"*30)
#assignment using tubles 

t = (1, 2, 3)
x, y, z = t
print (t) # (1, 2,3)
print (y) # 2

class A: 
     def setdata(self, value): 
         self.data = value 
     def display(self):
         print(self.data) 
         
         
         
x = A() 
y = A() 


print(x)
print(y)
print(isinstance(x,A))

print("##########################")

x.setdata("Ali") 
y.setdata(3.14159) 
x.display()
y.display()

print("##########################")

x.data = "New value" 
x.display()   #calling the initionated value by name

print("##########################")

x.anothername = "spam" #initionate a new parameter (not clean code)
print(x.anothername)

class Customer:
     def __init__(self, name, balance):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")

cust1 = Customer("Lara de Silva" , 100) 
print(cust1.name) 
print(cust1.balance) 


class Customer2:
    def	__init__(self, name, balance=0):  
        self.name = name
        self.balance = balance
        print("The	init	method was called")
        

cust2 = Customer2("Lara de Silva")
print(cust2.balance) 



class Customer3:
    def	__init__(self, name, balance=0):  
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return 'Customer : ' +str(self.name)+ ' , balance: ' + str(self.balance) 
    
    def __add__(self, other): 
        return Customer("Test_Customer",self.balance + other)

cust3 = Customer3("Lara de Silva") 
print(cust3.balance) 
print(cust3)

c3 = cust3 + 230
print(c3.balance)



class Employee:


	def __init__(self):
		print('Employee created.')

	def __del__(self):
		print('Destructor called, Employee deleted.')

obj = Employee()
del obj

class Person(object):
	def __init__(self, name, idnumber):
         self.name = name
         self.idnumber = idnumber
def display(self):
    print(self.name)
    print(self.idnumber)



obj = Person("Khalid", 257853)

print("Name: ", obj.name)
print("Id: ", obj.idnumber)

obj.display()


class Student:

	_name = None
	_roll = None
	_branch = None

	def __init__(self, name, roll, branch): 
		self._name = name
		self._roll = roll
		self._branch = branch
	
	def _displayRollAndBranch(self):

		print("Roll: ", self._roll)
		print("Branch: ", self._branch)

class Geek(Student):

	def __init__(self, name, roll, branch): 
         Student.__init__(self, name, roll, branch) 
	
def displayDetails(self):
    print("Name: ", self._name) 
		  
    self._displayRollAndBranch()

obj = Geek("Ali", 1706256, "Information Technology") 

obj.displayDetails() 

class Geek:
	
	__name = None
	__roll = None
	__branch = None

	def __init__(self, name, roll, branch): 
		self.__name = name
		self.__roll = roll
		self.__branch = branch


	def __displayDetails(self):
		print("Name: ", self.__name)
		print("Roll: ", self.__roll)
		print("Branch: ", self.__branch)
	
	def accessPrivateFunction(self):
		
		self.__displayDetails() 

	
	def get_name(self):
		self.__name 
    
	def set_name(self , name):
		self.__name = name 

	def get_roll(self):
		self.__roll

	def set_roll(self , roll):
		self.__roll = roll 

	def get_branch(self):
		self.__branch
    
	def set_branch(self , branch):
		self.__branch = branch 

             
obj = Geek("Osama", 1706256, "Information Technology")

obj.accessPrivateFunction()
class A(object): 
	def __init__(self, x): 
		self.x = x 
	
	def getX(self): 
		return self.X 
	
class B(object): 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 
	def getSum(self): 
		return self.X + self.y 



class C_A(A): 
	def isA(self): 
		return True
	
	def isB(self): 
		return False


class C_B(B): 
	def isA(self): 
		return False
	
	def isB(self): 
		return True

def getC(cond): 
	if cond: 
		return C_A(1) 
	else: 
		return C_B(1,2) 


ca = getC(True) 
print(ca.isA()) 
print(ca.isB()) 
	
cb = getC(False) 
print(cb.isA()) 
print(cb.isB()) 


class A(object): 
	def __init__(self, x): 
		self.x = x 
	
	def getX(self): 
		return self.X 


cond = True


class C(A if cond else object): 
	def isA(self): 
		return True

ca = C(1) 
print(ca.isA()) 

class CSStudent:
	stream = 'cse'				
	def __init__(self,name,roll):
		self.name = name		 
		self.roll = roll		

a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) 
print(b.stream) 
print(a.name) 
print(b.name) 
print(a.roll) 
print(b.roll) 


print(CSStudent.stream) 



CSStudent.stream = 'mech'

print(a.stream)
print(b.stream) 
class Parent(): 
	def __init__(self): 
		self.value = "Inside Parent"
	
	def show(self): 
		print(self.value) 
		

class Child(Parent): 

	def __init__(self): 
		self.value = "Inside Child"
		 
	def show(self): 
		print(self.value) 
		
		
obj1 = Parent() 
obj2 = Child() 

obj1.show() 
obj2.show() 

print('################################################')


class Parent(): 
	
	def show(self): 
		print("Inside Parent") 
		
class Child(Parent): 
	
	def show(self): 
		
		Parent.show(self)    
		print("Inside Child") 
		
obj = Child() 
obj.show() 

def product(a, b):
	p = a * b
	print(p)


def product(a, b, c):
	p = a * b*c
	print(p)

product(4, 5, 5)


print('####################################################')


def add(datatype, *args):


	if datatype == 'int':
		answer = 0


	if datatype == 'str':
		answer = ''

	for x in args:


		answer = answer + x

	print(answer)



add('int', 5, 6)


add('str', 'Hi ', 'Geeks')

print('####################################################')


def add(a=None, b=None):

	if a != None and b == None:
		print(a)

	else:
		print(a+b)


add(2, 3)

add(2)

print('####################################################')



from multipledispatch import dispatch


@dispatch(int, int)
def product(first, second):
	result = first*second
	print(result)



@dispatch(int, int, int)
def product(first, second, third):
	result = first * second * third
	print(result)


@dispatch(float, float, float)
def product(first, second, third):
	result = first * second * third
	print(result)


product(2, 3) 

product(2, 3, 2) 

product(2.2, 3.4, 2.3) 
