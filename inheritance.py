
# single inheritance_______________________

# class parent:
#     def display(self):
#         print("this is parent class")

# class child(parent):
#     def print1(self):
#         print("this is child class")

# c1=child()
# c1.display()
# c1.print1()

# multiple inheritance_________________

# class parent:
#     def display(self):
#         print("this is parent class")

# class parent1():
#     def print1(self):
#         print("this is parent1 class")

# class child(parent,parent1):
#     def print_child(self):
#         print("call from child class")

# c1=child()
# c1.display()
# c1.print1()
# c1.print_child()

# multilevel inheritance_______________________

# class parent:
#     def display(self):
#         print("this is parent class")

# class child1(parent):
#     def print_child1(self):
#         print("this is child1 class")

# class child2(child1):
#     def print_child2(self):
#         print("call from child class")

# c1=child2()
# c1.display()
# c1.print_child1()
# c1.print_child2()

# hierarchical inheritance__________________________

# class parent:
#     def display(self):
#         print("this is parent class")

# class child1(parent):
#     def print_child1(self):
#         print("this is child1 class")

# class child2(parent):
#     def print_child2(self):
#         print("call from child class")

# c2=child2()
# c1=child1()
# c2.display()
# c2.print_child2()
# # we can call this function using only c2 object
# c1.print_child1()


#hybrid inheritance________________________________________

class A:
    def method_a(self):
        print("Method A from class A")

class B(A):
    def method_b(self):
        print("Method B from class B")

class C(A):
    def method_c(self):
        print("Method C from class C")

class D(B, C):
    def method_d(self):
        print("Method D from class D")

class E(D):
    def method_e(self):
        print("Method E from class E")

# Create an object of class E
obj = E()

# Access methods from various classes in the hybrid inheritance hierarchy
obj.method_a()  
obj.method_b() 
obj.method_c() 
obj.method_d()  
obj.method_e()  

