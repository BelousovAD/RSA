import random

from math import gcd
from math import sqrt

def is_prime(x):
	if x % 2 == 0:
		return False
	for i in range(3, round(x**(1/2)) + 1, 2):
		if x % i == 0:
			return False
	return True

def mi(a, b):
    if (a == 0):
        x = 0
        y = 1
        return b, x, y
    d, x1, y1 = mi(b % a, a);
    x = y1 - (b // a) * x1
    y = x1
    return d, x, y

def multi_invers(a, b):
    x = mi(a, b)
    return x[1]

def generate_key(P, Q):
    N = P * Q

    #значение функции Эйлера
    phi = (P - 1) * (Q - 1)
    
    #открытая экспонента
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = multi_invers(e, phi * -1)
    return ((e, N), (d, N))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    dba = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in dba]
    return ''.join(plain)

if __name__ == "__main__":

    p = int(random.randrange(1, 10000))
    q = int(random.randrange(1, 10000))

    while not is_prime(p):
        p = int(random.randrange(1, 10000))
    while not is_prime(q):
        q = int(random.randrange(1, 10000))

    public, private = generate_key(p, q)

    print("Public key: ", public)
    print("Private key: ", private)

    message = input("Введите сообщение: ")
    encrypted_msg = encrypt(public, message)

    print("Зашифрованное сообщение: ", ''.join(map(lambda x: str(x) + " ", encrypted_msg)))
    print("Рассшифрванное сообщение: ", decrypt(private, encrypted_msg))