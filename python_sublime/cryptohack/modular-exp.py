# # You can think of this as raising some number to a certain power (2^10 = 1024), and then taking the remainder of the division by some other number (1024 mod 17 = 4). In Python there's a built-in operator for performing this operation: pow(base, exponent, modulus)


# x = pow(101, 17, 22663)

# print(x)
# print('--------------------------')

# ####### RSA cipher..
# p, q = 17, 23

# N = p*q

# e = 65537

# message = 12

# cipher_text = pow(message, e, N)

# print(cipher_text)
# print('-----------------------')
