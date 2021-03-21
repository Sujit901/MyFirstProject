# def add_two_numbers(num1,num2,num3=0):
#     s = num1+num2+num3
#    return s

# ss = add_two_numbers(3,4)
# print("Sum is",ss)



# def add_two_numbers(*args):
#     print(type(args))
#     print(args)
#     s = 0
#     for i in args:
#         s = s + i
#     return s

# ss = add_two_numbers(3,4)
# print("Sum is",ss)


# def add_two_numbers(*args):
#     print(type(args))
#     print(args)
#     s = sum(args)
#     return s

# ss = add_two_numbers(3,4)
# print("Sum is",ss)


# def information(**kwargs):
#     print(type(kwargs),kwargs)
#     for k, v in kwargs.items():
#         print(k, v)

# information(name="Ram", age=25, address="Bhaktapur")


# d = "Sujit"
# a = 10
# print("Difference of two is: ",d-a) #(Type error example)


#x = [5, 4, 3, 2, 1]
#y = sorted(x)
#y = x.sort()
#print(x, y)


# class Info:
#     name = "Sujit"
#     address = "Butwal"

# obj = Info()

# print(type(obj))

# print(obj.name)
# obj.address = "Kathmandu"
# print(obj.address)
# del obj.address
# print(obj.address)


# class Info:
#     address = "Butwal"

#     def __init__(self, name):
#         #print(type(self))
#         self.name = name
#         print("name", name)

# obj = Info("Sujit")
# obj.address = "Bhairahawa"
# print(obj.name, obj.address)

# obj1 = Info("Sudip")
# print(obj1.name, obj1.address)



# class SumOfTwo:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def add(self):
#         s = self.a + self.b
#         print("sum of two", s)

# obj = SumOfTwo(10, 20)
# print("obj.a", obj.a)
# print("obj.b", obj.b)
# obj.add()



