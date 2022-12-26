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


class Operation(Account):
    """Данный класс используется для создания и подтверждения операций в блокчейне"""

    sender = Account
    receiver = Account.accountID
    amount = 0
    signature = 0
    operation_id = 0

    def __init__(self, sender, receiver, amount, signature):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
        self.operation_id += 1

    def createOperation(self, sender, receiver, amount, signature):
        operation = Operation(sender, receiver, amount, signature)
        print("Operation ID: ", operation.operation_id)
        print(f"Sender: {operation.sender}")
        print(f"Receiver: {operation.receiver}")
        print(f"Amount: {operation.amount} UAH")
        print(f"Signature: {operation.signature}")
        return operation

    def verifyOperation(self, sender_account):
        publickey = int(int(sender_account.wallet.keys()[-1], 16) / 10000)
        verifysignature = (self.signature ** publickey) % 2
        if self.amount <= sender_account.balance:
            sender_account.balance -= self.amount
            return True
        elif self.signature == verifysignature:
            return True
        else:
            return False

    def printOperation(self):
        print(self.operation_id, self.sender, self.receiver, self.amount, self.signature)


class Transaction(Operation):
    """Данный класс используется для создания транзакций в блокчейне"""

    transactionID = ''
    setOfOperations = []
    nonce = 0

    def __init__(self):
        self.transactionID = ''
        self.setOfOperations = []
        self.nonce = 0

    def createTransaction(self, setOfOperations, nonce):
        transaction = Transaction()
        transaction.transactionID = hex(abs(hash(str(nonce) + str(len(setOfOperations)))))[:33]
        transaction.setOfOperations.extend(setOfOperations)
        transaction.nonce = nonce
        return transaction

    def printTransaction(self):
        print(f"ID transaction: {self.transactionID}")
        print(f"Operationsn: {self.setOfOperations}")
        print(f"Nonce value: {self.nonce}")


class Hash:
    """Данный класс используется для хеширования строки данных методом SHA1"""

    def toSHA1(self, message):
        def rotl(x, n):
            return ((x << n) | (x >> (32 - n))) & 0xffffffff

        h0 = 0x67452301
        h1 = 0xefcdab89
        h2 = 0x98badcfe
        h3 = 0x10325476
        h4 = 0xc3d2e1f0
        message_length = len(message.encode('utf-8')) * 8

        if 0 <= message_length < 2 ** 64:
            binary_string = ''.join(format(ord(i), '08b') for i in message)
            padded_message = binary_string + '1'
            k = 448 - (message_length + 1)
            padded_message += '0' * k
            end_message = 64 - message_length.bit_length()
            padded_message += '0' * end_message
            padded_message += bin(message_length)[2:]
            N = []
            M = []
            y = 0
            x = 0

            if len(padded_message) > 512:
                for i in range(0, len(padded_message) // 512):
                    N.append(padded_message[x:x + 512])
                    x += 512
            else:
                N.append(padded_message)
            for i in N:
                for j in range(0, 16):
                    M.append(i[y:y + 32])
                    y += 32
                for k in range(16, 80):
                    M.append(rotl(int(M[k - 3], 2) ^ int(M[k - 8], 2) ^ int(M[k - 14], 2) ^ int(M[k - 16], 2), 1))
                    M[k] = "{0:b}".format(M[k]).zfill(32)

            a = int(hex(h0), 16)
            b = int(hex(h1), 16)
            c = int(hex(h2), 16)
            d = int(hex(h3), 16)
            e = int(hex(h4), 16)
            f = 0

            for i in range(0, 80):
                if 0 <= i <= 19:
                    f = (b & c) | ((~b) & d)
                    k = int('0x5A827999', 16)
                elif 20 <= i <= 39:
                    f = b ^ c ^ d
                    k = int('0x6ED9EBA1', 16)
                elif 40 <= i <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = int('0x8F1BBCDC', 16)
                elif 60 <= i <= 79:
                    f = b ^ c ^ d
                    k = int('0xCA62C1D6', 16)

                M[i] = int(hex(int(M[i], 2)), 16)
                T = rotl(a, 5) + f + e + k + M[i] & 0xffffffff
                e = d
                d = c
                c = rotl(b, 30)
                c = int("{0:b}".format(c).zfill(64)[32:64], 2)
                b = a
                a = T

            h0 = h0 + a & 0xffffffff
            h1 = h1 + b & 0xffffffff
            h2 = h2 + c & 0xffffffff
            h3 = h3 + d & 0xffffffff
            h4 = h4 + e & 0xffffffff

            sha1_hash = '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

            return sha1_hash


class Block(Transaction):
    """Данный класс используется для инициализации блоков в блокчейне"""

    blockID = ""
    prevHash = ""
    setOfTransaction = []
    block_counter = 1

    def __init__(self):
        self.blockID = ""
        self.prevHash = ""
        self.setOfTransaction = []

    def createBlock(self, setOfTransaction, prevHash):
        block = Block()
        block.prevHash = prevHash
        block.setOfTransaction.extend(setOfTransaction)
        block.blockID = "77" + hex(abs(hash(str(self.block_counter) + str(len(setOfTransaction)) + str(prevHash))))[:33]
        Block.block_counter += 1
        return block

    def printBlock(self):
        print("Block Header Info")
        print(f"Previous Block: {self.prevHash}")
        print(f"Block ID: {self.blockID}")
        print(f"Transaction List")
        print(f"{self.setOfTransaction}")


class Blockchain(Block):
    """Данный класс используется для инициации блокчейна и валидации блоков в сети"""

    coinDatabase = dict()
    blockHistory = []
    txDatabase = []
    faucetCoins = 0
    blocks = []

    def __init__(self):
        self.__class__.blocks.append(self)

    @staticmethod
    def initBlockchain():
        genesis_block = Block()
        genesis_block.createBlock(setOfTransaction=['0x7701122000'], prevHash='')
        return genesis_block

    def getTokenFromFaucet(self, account, amount):
        account.updateBalance(amount)
        self.coinDatabase.update({account, account.getBalance()})

    def validateBlock(self, block):
        if len(block.prevHash) == 0:
            print("ERROR: Block prevhash do not exist or match")
        elif block.setOfTransaction in self.txDatabase:
            print("ERROR: Block trasnsactions already in txDatabase")
        elif not block.setOfTransaction and block.setOfTransaction.transactionID == '00':
            print("ERROR: Block transaction list empty")
        elif block.setOfTransaction.setOfOperations.amount > max(self.coinDatabase.values()):
            print("ERROR: Operations amount more than account balance!")
        else:
            print("Block validation status: SUCCESS")

    def showCoinDatabase(self):
        self.coinDatabase.items()

    def printBlockchain(self):
        print('Block: \n'.join(Blockchain.blocks))


class Category:
    """Данный класс используется для учета расходов пользователя по категориям"""

    category_id = 1
    name = ''
    category_list = dict()

    def __init__(self):
        self.name = ''

    def createCategory(self, name):
        new_category = Category()
        new_category.category_id = self.category_id
        new_category.name = name
        self.category_list.update({new_category.name: new_category.category_id})
        Category.category_id += 1
        return new_category

    def removeCategory(self, name):
        if name in Category.category_list:
            Category.category_list.pop(name)
            Category.category_id -= 1
            print(f"You deleted category: {name}\nDelete was successful!")
        else:
            print("Error!")


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
    print("-" * 40)
    hash = Hash()
    print("Hashing message (Kyrylo) using SHA1:")
    print(hash.toSHA1("Kyrylo"))
    print("-" * 40)
    service = Category()
    print(service.createCategory('одяг'))
    service2 = Category()
    print(service2.createCategory('dpennz'))
    print(Category.category_list)
    service2.removeCategory('dpennz')
    print(Category.category_list)
    service3 = Category()
    service3.createCategory('взуття')
    print(Category.category_list)


if __name__ == '__main__':
    main()
