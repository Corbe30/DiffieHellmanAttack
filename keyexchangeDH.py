
"""

DIFFIE HELLMAN PROTOCOL

Given p,g,a,b --> Obtain A y B

"""
# use Python 3 print function
# this allows this code to run on python 2.x and 3.x
from __future__ import print_function

# Variables Used
p = int(input("Enter value for p: ")) #Example: 10784399
g = int(input("Enter value for g: ")) #Example:13
a = int(input("Enter value for a: ")) #Example:12
b = int(input("Enter value for b: ")) #Example:15

print("Given this values: \n")
print("p =", str(p) )
print("g =", str(g) )
print("a =", str(a) )
print("b =", str(b) )

# Alice Sends Bob A = g^a mod p
A = (g**a) % p
print( "Alice Sends Over Public Chanel (A):", str(A) )

# Bob Sends Alice B = g^b mod p
B = (g ** b) % p
print( "Bob Sends Over Public Chanel (B):", str(B) )

print( "-----------------")
print( "Privately Calculated Shared Secret (K): ")
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = (B ** a) % p
print( "Alice Shared Secret: ", str(aliceSharedSecret ))

# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = (A**b) % p
print( "Bob Shared Secret: ", str(bobSharedSecret ))
