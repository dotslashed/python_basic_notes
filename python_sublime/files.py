# #using simple read() shows the contents of the file but not iterates.

# f = open('passwords.txt', 'rt')

# print(f)

# print(f.readlines())

# f.seek(0)

# print(f.readlines())

# f.seek(0)
# for lines in f:
#     print(lines.strip())  # iterating over the file items array

# # use f.seek() when need and depeding on the file pointer position.


# f.close()    # closing the file after operation

# f = open('demo.txt', 'w')

# f.write('hello this is a file written in python')

# f.close()


with open('passwords.txt', encoding='latin-1') as f:
    for line in f:
        print(line.strip())
