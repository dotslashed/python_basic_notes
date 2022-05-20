
# print("A list with different data types:")

# list_1 = ["A", "B", "C", "D", "E", "F", 1, 3.5, [], ("hello", "test"), False]

# print(list_1)

# print(type(list_1))

# print(list_1[:8])

# print(list_1[-1])
# print("===============================================")
# # list operations
# print("List operations")
# list_1 = ["Z"] + list_1

# print(list_1)

# list_1.append("K")

# print(list_1)

# list_1[3] = "P"

# print(list_1)

# list_1.insert(0, "H")

# print(list_1)

# del list_1[3]


# print(list_1)

# #print(max(list_1))

# print(list_1.index("P"))

# print(list_1.count("A"))

# list_1.reverse()

# print(list_1)

# print(list_1[::-1])  # printing everything but reverse

# list_1.append("A")

# print(list_1.count("A"))


# list_1.pop()

# print(list_1)

# list_1.clear() # operation complete clearing the list items; empty list

# print(list_1)

list_2 = [1, 7, 4, 9, 11, 13]

print(list_2)

list_2.sort()

print(list_2) #ascending order

list_2.sort(reverse=True) #descending order

print(list_2)

#copying list items from one list to another new list
list_3  = list_2.copy()

print(list_3)

list_3.append(17)

print(list_3)

print(list_2)

list_4 = list(map(float, list_3 ))

print(list_4)