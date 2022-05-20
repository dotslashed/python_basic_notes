# single_str = 'hello we are python'

# print(single_str)

# multi_str = """hello this
# is a
# multiline
# string dont mind"""

# print(multi_str)
# print('----------------------------------------------------------')
# print(single_str.upper())

# print('I\'m escaped successfully using the backslash')

# hex_ecs = '\x41\x42\x43\x44' #a hex in string

# print(hex_ecs)

# print("are" in single_str)

# print("test" in single_str)

# print(single_str.startswith('a'))

# print(single_str.startswith('hello'))

# print(single_str.index('hello'))

# print(single_str.index('python'))

# string strinpping and replacing in python

# messy_str = '    this is a mess messed up!            '

# print(messy_str)

# print(messy_str.strip())

# print(messy_str.replace('!', '?').strip())

# print(messy_str.replace('messed', 'fucked').strip())

#Splitting strings around delimiters.


new_str = 'Hi how are you doing'

new_str2 = 'hi,you,yes,you,I,am,calling,you'

print(new_str2.split(","))       #split across comma

print(new_str.split())          #split accross space; by default

domain_name = 'examplecom'

domas = domain_name.rjust(20,'x')

print(domas)

print("domain name is {} characters long.".format(len(domain_name)))  #doesnot require to type cast when using format method.

print("{} {} {}".format('10', '\x41', 'Success!'))

print("-----------------------------------------------")

length = len(domain_name)

print(f"domain_name is {length} characters long!") #string literals, no need to bother about type casting at all.

print(f"domain_name is {length:.2f} characters long!")

print("domain name is %d characters long" % len(domain_name))  #this is a more efficient method to do the same task

print("domain name is %x characters long" % len(domain_name))

print("domain name is %f characters long" % len(domain_name))

print("domain name is %o characters long" % len(domain_name))

print(f"domain name is {len(domain_name)} chars long!") #bash way