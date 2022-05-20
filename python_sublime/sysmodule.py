import sys
import time
print(sys.version)

print("------------")

# for i in range(0,101):
#     time.sleep(0.1)
#     sys.stdout.write("{}% [{}{}]\r".format(i, '#'*i, '.'*(100-i)))
#     sys.stdout.flush()
# sys.stdout.write("\n")


# print(sys.argv)
# print(len(sys.argv))

user_name = sys.argv[1]

pass_word  = sys.argv[2]

if len(sys.argv) != 3:
    sys.stdout.write("[X] To run {} Please enter username and password:\n".format(sys.argv[0]))



print("{} {}".format(user_name,pass_word))


# sys practice pending..