print(10 > 9)

print(9 > 10)

print(9 == 9)

print(9 != 9)
print("--------------------------------------")
print((10 / 9))

print(10 // 9)

print(10 * 10)

print(10 ** 10)

print(10 % 9)
print(10 % 10)
print("-------------------------------------")

x = 10

x = x + 5
x = x*5
print(x)
x = x**2
print(x)
x = x / 10
print(x)

print(bin(13)[2:])
print("----------------------------------------")
y = 5

z = 2

bin1 = bin(y)[2:].rjust(4,"0")

bin2 = bin(z)[2:].rjust(4,"0")

print(bin1)
print(bin2)

print("Below is and operation :")
print(bin(z & y)[2:].rjust(4,"0"))

print("Below is or operation")

print(bin(z | y)[2:].rjust(4,"0"))

print("Finished!!!")