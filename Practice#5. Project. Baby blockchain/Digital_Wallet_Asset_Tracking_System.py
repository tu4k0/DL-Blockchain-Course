import random


class KeyPair:
    """Данный класс используется для создания приватного и публичного ключей. Обеспечивает аутентичность приложения"""

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
    """Данный класс используется для создания подписи пользователя на основе приватного, публичного ключей и исходного сообщения. Обеспечивает верификацию подписи"""

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


class Account(KeyPair):
    """Данный класс используется для создания аккаунта и проведение операций с аккаунтом"""

    accountID = ''
    wallet = dict()
    balance = 0

    def __init__(self):
        self.accountID = ''
        self.wallet = dict()
        balance = 0

    def genAccount(self):
        acc = Account()
        public_key, private_key = KeyPair.genKeyPair(acc)
        acc.accountID = abs(int(str(hash(public_key))[:10]))
        acc.wallet.update({public_key: private_key})
        acc.balance = 0
        self.accountID = acc.accountID
        self.wallet = acc.wallet
        self.balance = acc.balance
        return acc

    def addKeyPairToWallet(self):
        public_key, private_key = KeyPair.genKeyPair(self)
        self.wallet[public_key] = private_key

    def updateBalance(self, balance):
        self.balance = balance

    def createPaymentOp(self, recipient, amount, key_index):
        print("Payment ID: ", random.randint(1, 1000))
        print(f"From: {self.accountID} \t", f"!Key Pairs: {key_index}!")
        print(f"To: {recipient}")
        print(f"Amount: {amount} UAH")
        if self.balance >= amount:
            result = self.balance - amount
            self.updateBalance(result)
            print("Result: Success!")
        else:
            print("Result: Fail (Not enough balance)")
        return True

    def signData(self, key_index, message):
        private_key_index = self.wallet.get(key_index)
        private_key = int(int(private_key_index, 16) / 10000)
        signature = (message ** private_key) % 2
        return signature

    def getBalance(self):
        return int(self.balance)

    def printBalance(self):
        print("Balance: ", self.balance)

    def printAccount(self):
        print(f" Account ID: {self.accountID}\n", f"Wallet Info: {self.wallet}\n", f"Balance: {self.balance} UAH\n")


def main():
    print("Key pair generation: ")
    keys = KeyPair()
    keys.genKeyPair()
    keys.printKeyPair()
    print("-" * 40)
    print("Signature verification with message (123):")
    signature = Signature()
    print(signature.verifySignature(123, keys.publicKey, signature.signData(keys._privateKey, 123)))
    print("-" * 40)
    print("Account generation: ")
    account = Account()
    account.genAccount()
    account.printAccount()
    print('')
    print("Adding key pair: ")
    account.addKeyPairToWallet()
    account.printAccount()
    print('')
    print("Updating account balance to 100 UAH:")
    account.updateBalance(100)
    account.printAccount()
    print('')
    print("Payment Operation:")
    account.createPaymentOp(recipient=123234, amount=40, key_index=list(account.wallet.items())[-1])
    print('')
    print("Signing data (Message: 7667):")
    print("Signature: ", account.signData(max(account.wallet), 7667))
    print('')
    print("Account balance rest:")
    print(account.getBalance(), "UAH")


if __name__ == '__main__':
    main()
