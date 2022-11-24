import random


class KeyPair:
    """Данный класс используется для подписи операций пользователя. Обеспечивает аутентичность приложения"""
    publicKey = ''
    _privateKey = ''

    def __init__(self):
        self.publicKey = 'publicKey'
        self._privateKey = '_privateKey'

    def genKeyPair(self):

        def Check_prime_number(n):
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            return True

        def Check_coprime_integer(e, k):
            while (e and k):
                if e > k:
                    e %= k
                else:
                    k %= e
            if (e + k == 1):
                return True
            else:
                return False

        def Eiler(p, q):
            f = (p - 1) * (q - 1)
            return f

        cached_primes = [i for i in range(1, 1000) if Check_prime_number(i)]
        p = random.choice([i for i in cached_primes])
        q = random.choice([i for i in cached_primes])
        n = p * q
        self.n = n
        f = Eiler(p, q)

        e, j = 0, True
        while j:
            e = random.randint(1, f)
            if Check_coprime_integer(f, e) == True:
                j = False
            else:
                continue

        d = 1
        while True:
            if (d * e) % f == 1:
                break
            else:
                d += 1

        publickey = (hex(e) + str(hex(n).strip('0x')))[0:10]
        self.publicKey = publickey
        privatekey = (hex(d) + str(hex(n).strip('0x')))[0:10]
        self._privateKey = privatekey

        return publickey, privatekey

    def printKeyPair(self):
        print('PublicKey: ', self.publicKey)
        print('PrivateKey: ', self._privateKey)


class Signature(KeyPair):
    """Данный класс используется для верификации подписи пользователя"""

    signature = 0

    def __init__(self):
        super().__init__()

    def signData(self, privateKey, message):
        privatekey = int(int(privateKey, 16) / 10000)
        signature = (message ** privatekey) % 2
        self.signature = signature
        return signature

    def verifySignature(self, message, publicKey, signature):
        publickey = int(int(publicKey, 16) / 10000)
        verifysignature = (signature ** publickey) % 2
        if signature == verifysignature:
            return True
        else:
            return False

    def printSignature(self):
        print(self.signature)


def main():
    print("Key pair generation: ")
    keys = KeyPair()
    keys.genKeyPair()
    keys.printKeyPair()
    print("-" * 40)
    print("Signature verification with message (123):")
    signature = Signature()
    print(signature.verifySignature(123, keys.publicKey, signature.signData(keys._privateKey, 123)))


if __name__ == '__main__':
    main()
