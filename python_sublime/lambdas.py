#Function shortening with lambda

add  = lambda x : x + 10

print("Additions is: {}".format(add(10)))


product_func = lambda x, y : x*y

print("Product is: {}".format(product_func(2,4)))

# Anonymous function

print("The product is: ", (lambda x,y : x + y)(100,200))

ord_func = lambda x: [ ord(i) for i in x ]

print(ord_func("ABCD"))

# odd even

is_even = lambda x: x % 2 == 0

print(is_even(2))

print(is_even(1029129))

print(is_even(21291190))



str = 'string'

result = []

for i in range(0, len(str), 2):
    result.append(str[i:i+2])
print(result)




