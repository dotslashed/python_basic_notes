

list1 = ['aaa','bbb','ccc','ddd','eee']

print(list1)

list2 = [i for i in list1]

print("This is list2: {}".format(list2))

list3 = [x for x in list1 if x=='aaa']

list0 = [x if x=='bbb' else "X" for x in list1]

print(list0)

print(list3)

print("-------")

list4 = [hex(x) if x>=0 else "X" for x in range(5)]

print(list4)

list5 = [hex(x) if x>=0 and x<=2 else "X" for x in range(5)]

print(list5)

list5 = [hex(x) if x>=0 or x<=2 else "X" for x in range(5)]

print(list5)

list6 = [x*x for x in range(5)]

print(list6)


list7 = [[1,2],[3,4],[5,6],[7,8]]

list8 = [x for y in list7 for x in y]

print(list8)      # prints all the items indiviadually to a single list from the nested list



list9 = [x for x in "Bhargab"]

print(list9) # in a list format

print("".join(list9))  #again back to a string

print("_".join(list9))

print("\n".join(list9))

print("\nXXXXXXXXXXXXXX")

