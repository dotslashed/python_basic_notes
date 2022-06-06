
list1 = [1, 5, 7, 0]

list1.append(43)

# print(list1)

list1.reverse()

# print(list1)

list1.sort()

# print(list1)


set1 = {'apple', 'mango', 'banana', 'apple'}

print(set1)   # uniquely print items

for i in range(5):
	set1.add(i)

print(set1)

dict_1 = {'Name': 'Bhargab', 'State': 'Assam', 'Country': 'India', 'email': 'idontknow@gmail.com'}

for k, v in dict_1.items():
	print(k) if v == 'India' else None         #different way of if else and printing

	print(v) if k == 'Name' else None


j = 0

while j < 10:
	# print(j)
	j+= 1

print("----------")

m = 0

while m < 20:
	# print(m)

	m+=2


# while True:       #this code will never execute coz 43 string will not print, as it will continue the loop
# 	continue
# 	print("43") 	# dead code

# while True:        #will print the '43' after the loop ends
# 	break
# print('43')


employees = {'Alice' : 100000,
'Bob' : 99817,
'Carol' : 122908,
'Frank' : 88123,
'Eve' : 93121}

top_earners = []

for k, v in employees.items():
	top_earners.append((k,v)) if v >= 100000 else None


print(top_earners)
print('----------------------')


print([x*x for x in range(1,6)])

print([x**3 for x in range(11) if x % 2 == 0])

print([(x,y) for x in range(3) for y in range(3)])     #same as the determinant rule of product

# (0,1,2)

# (0,1,2)

#The same scenario in one-liners

top_earner = [(key,val) for key,val in employees.items() if val >= 100000 ] #list comprehended

print(top_earner)

# while True:
# 	print('1')
# 	break
