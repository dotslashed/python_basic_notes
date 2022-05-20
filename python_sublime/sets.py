

set1 = {"tiger", "Lion", "Dear", "Horse", "Buffalo"}

print(set1)

print(type(set1))


set2 = {"tiger", "Lion", "Dear", "Horse", "Elephant"}


print(set2)

print(set1.union(set2))

print(set1.intersection(set2))


print(set1.update(set2))


set1.discard("tiger")

print(set1)

print("\nSets are cool! too")