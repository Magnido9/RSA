import random

import number_theory_functions

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        p=number_theory_functions.generate_prime(digits)
        q=number_theory_functions.generate_prime(digits)
        N=p*q
        res=0
        while res!=1:
            e=random.randrange(2**(digits-1),2**digits)
            (res,_,_)=number_theory_functions.extended_gcd(e,(q-1)(p-1))
        d=number_theory_functions.modular_inverse(e,(p-1)(q-1))
        return RSA(public_key=(N,e),private_key=(N,d))


    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        (N,e)=self.public_key
        return number_theory_functions.modular_exponent(m,e,N)


    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        (N,d)=self.private
        return number_theory_functions.modular_exponent(c,d,N)
