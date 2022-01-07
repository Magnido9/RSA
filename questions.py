import random
import number_theory_functions as ntf
from rsa_functions import RSA
#Question 1
(d,a,b)=ntf.extended_gcd(797,5279)
print("Answer to question 1:")
if 1000000%d==0 and a>0 and b<0:
    print("The transaction is possible")
else:
    print("The transaction is impossible")
#Question 2
t=ntf.modular_exponent(ntf.modular_exponent(123456,74896543,1000),74365753,1000)
print()
print("Answer to question 2:")
print(str(t)[0])
#Question 3
#we used wolframe alpha to find phi of N
N=12215009
p=3491
q=3499
phi=12208020
e=3499
d=(ntf.modular_inverse(e,phi))
rsa=RSA(private_key=(N,d),public_key=(N,e))
t=rsa.decrypt(42)
t2=rsa.encrypt(t)
print()
print("Answer to question 3:")
print("Decrypted:")
print(t)
print("Re-encrypted:")
print(t2)
#Question 4
(d,a,b)=ntf.extended_gcd(991,11)
if(d==1):
    print("Inverse")
    print("X^"+str(b%991)+" mod991")
    for i in range(991):
        assert(ntf.modular_exponent(i,11*901,991) == i)
#Question 5
p=7919
q=6841
message=4269
N=p*q
res=0
while res!=1:
    e=random.randrange(2**(4-1),2**4)
    res,_,_=ntf.extended_gcd(e,(q-1)*(p-1))
d=ntf.modular_inverse(e,(p-1)*(q-1))
rsa=RSA(public_key=(N,e),private_key=(N,d))
encrypted=rsa.encrypt(message)
print()
print("Answer to question 5:")
print("Message:")
print(message)
print("Encrypted:")
print(encrypted)
decrypted=rsa.decrypt(encrypted)
print("Decrypted:")
print(decrypted)
