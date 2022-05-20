
# def function1():
#     print("I am function1")

# function1()


# def function2():
#     return "I am function2"

# func2 = function2()

# print(func2)

# def function3(s):
#     print("\t\n{}".format(s))

# function3("Function 3 which has 1 arguments..")


# def function4(s1,s2):
#     print("\t\n{} {}".format(s1,s2))

# function4('This function has','two arguments...')

# print("\n--------------")


# def func_default(s1="default!"):
#     print("{}".format(s1))

# func_default()  # Prints the default value when no argument passed

# func_default("something")  # Prints the string something..


# def dict_function(**ks):
#     for i in ks:
#         print(i, ks[i])

# dict_function(a="1", b="2", c="3")

# print("Datatypes in function...")

# print("\n")

# def function_datatype(i, f, s, l):

#     print(type(i))
#     print(type(f))
#     print(type(s))
#     print(type(l))

# function_datatype(1, 1.0, "jajakajka", ["a", "b", "c"])

# print("---------")

# print("Scope of a function..:")


# x = 500   #global variable

# def scope():
#     #x = 5   #local variable
#     global x   # got access to glabal x variable value
#     x = x + 1
#     print(x)


# scope()
# print(x)  # value changed to 501

# print("------")
# def func5(p):
#     while p >= 0:
#         print(p)
#         p = p - 1

# func5(4)

def main(a,b):
    c = a*b
    print("Product is: {}".format(c))

main(2,3)
main(3,3)

print("----------")
def ret(c,d):
    return c*d

product = ret(4,3)
print("Product is: {}".format(product))    