class Vigenere:

    def __init__(self, message, key):
        self.message = message.upper().replace(' ', '')
        self.key = key.upper()

    def Vigenere_table(self):
        alphabet = ''
        for i in range(ord('A'), ord('Z') + 1):
            alphabet += chr(i)
            vigenere_table = ['' for i in range(ord('A'), ord('Z') + 1)]
        for i in range(0, len(vigenere_table)):
            vigenere_table[i] = list(alphabet)
            alphabet = alphabet[1:] + alphabet[0]

        return vigenere_table

    def Key(self):
        cipher_key = ''
        d = 0
        for j in range(len(self.message)):
            if len(self.key) <= len(self.message):
                if self.message[j].isdigit():
                    cipher_key += '-'
                else:
                    if d >= len(self.key):
                        d = 0
                    cipher_key += self.key[d]
                    d += 1
            else:
                break
        return cipher_key

    def Encode(self):
        vigenere_table = self.Vigenere_table()
        cipher_key = self.Key()
        counter = 0
        encription = ''
        i = 0
        while i <= len(vigenere_table):
            if counter < len(self.message):
                if self.message[counter] == vigenere_table[0][i]:
                    for j in range(0, len(vigenere_table)):
                        if cipher_key[counter] == vigenere_table[j][0]:
                            encription += vigenere_table[j][i]
                            i = 0
                            counter += 1
                            break
                elif self.message[counter].isdigit():
                    encription += self.message[counter]
                    i = 0
                    counter += 1
                else:
                    i += 1
            else:
                break
        return encription

    def Decode(self):
        encription = self.message
        vigenere_table = self.Vigenere_table()
        cipher_key = self.Key()
        z = 0
        decryption = ''
        i = 0
        while i <= len(vigenere_table):
            if z < len(encription):
                if cipher_key[z] == vigenere_table[i][0]:
                    index = i
                    for j in range(0, len(vigenere_table)):
                        if encription[z] == vigenere_table[index][j]:
                            decryption += vigenere_table[0][j]
                            i = 0
                            z += 1
                            break
                elif encription[z].isdigit():
                    decryption += encription[z]
                    i = 0
                    z += 1
                else:
                    i += 1
            else:
                break
        return decryption


def main():
    print('-' * 100)
    print('Vigenere Cipher')
    mode = input('Choose mode (Encode/Decode): ').lower()
    message = input('Enter the message: ')
    key = input('Enter key: ')
    cipher = Vigenere(message, key)
    if mode == 'encode':
        print(f'Ciphertext: {cipher.Encode()}')
    elif mode == 'decode':
        print(f'Plaintext: {cipher.Decode()}')
    print('-' * 100)


if __name__ == '__main__':
    main()
