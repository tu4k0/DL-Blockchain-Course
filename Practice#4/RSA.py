import random


class RSA:

    def __init__(self, message):
        self.message = message

    def Check_prime_number(self, n):
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    def Check_coprime_integer(self, e, k):
        while (e and k):
            if e > k:
                e %= k
            else:
                k %= e
        if (e + k == 1):
            return True
        else:
            return False

    def Keys_generation(self):

        def Eiler(p, q):
            f = (p - 1) * (q - 1)
            return f

        cached_primes = [i for i in range(1, 100) if self.Check_prime_number(i)]
        p = random.choice([i for i in cached_primes])
        q = random.choice([i for i in cached_primes])
        n = p * q
        f = Eiler(p, q)

        e, j = 0, True
        while j:
            e = random.randint(1, f)
            if self.Check_coprime_integer(f, e) == True:
                j = False
            else:
                continue

        d = 1
        while True:
            if (d * e) % f == 1:
                break
            else:
                d += 1

        public_key = [e, n]
        private_key = [d, n]

        return public_key, private_key

    def Encode(self, public_key):
        message_list = list(self.message)
        ciphertext = []

        for i in range(0, len(message_list)):
            message_list[i] = (ord(message_list[i]) ** public_key[0]) % public_key[1]
            ciphertext.append(message_list[i])

        return ciphertext

    def Decode(self, public_key, private_key):
        ciphertext = self.Encode(public_key)
        plaintext = []

        for i in range(0, len(ciphertext)):
            ciphertext[i] = (ciphertext[i] ** private_key[0]) % private_key[1]
            plaintext.append(chr(ciphertext[i]))

        return plaintext


def main():
    print('-' * 100)
    print('RSA Algorithm')
    message = input('Enter message: ')
    cipher = RSA(message)
    private_key, public_key = cipher.Keys_generation()
    print(f'Automatically generated keys: public key:({public_key}), private key:({private_key})')
    ciphertext = cipher.Encode(public_key)
    print('Ciphertext: ', ''.join(str(i) for i in ciphertext))
    plaintext = cipher.Decode(public_key, private_key)
    print('Plaintext: ', ''.join(str(j) for j in plaintext))
    print('-' * 100)


if __name__ == '__main__':
    main()
