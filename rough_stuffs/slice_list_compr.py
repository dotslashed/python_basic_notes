

numbers = [32, 98, 12, 65, 53, 99, 73, 88, 97, 10]

print(numbers[:5])


print(numbers[3:])


print(numbers[3:9])


print(numbers[-10:])

print(numbers[2:-3])

# While using negative slicing, the direction of printing is left to right whereas the direction of counting is right to left after that follows the normal rule.


print(numbers[-5:-1])

#But
print(numbers[-3:-5]) # is empty because of the direction.

print('-------------------')


print(numbers[::]) #prints the list as it is


print(numbers[::-1])  #prints the same list but reverse


print(numbers[::-2])  #reverse direction 2 intervals.


print(numbers[::2])   #after 2 intervals.


print('-----------------------------\n')


print([number for number in numbers if number % 2 == 0])

print([number-2 for number in numbers])

print([number/2 for number in numbers if 65 in numbers])

