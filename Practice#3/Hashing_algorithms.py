import binascii


def SHA1(message):
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


def MD2(message):
    S = [
        41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6,
        19, 98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188,
        76, 130, 202, 30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24,
        138, 23, 229, 18, 190, 78, 196, 214, 218, 158, 222, 73, 160, 251,
        245, 142, 187, 47, 238, 122, 169, 104, 121, 145, 21, 178, 7, 63,
        148, 194, 16, 137, 11, 34, 95, 33, 128, 127, 93, 154, 90, 144, 50,
        39, 53, 62, 204, 231, 191, 247, 151, 3, 255, 25, 48, 179, 72, 165,
        181, 209, 215, 94, 146, 42, 172, 86, 170, 198, 79, 184, 56, 210,
        150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241, 69, 157,
        112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2, 27,
        96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
        85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197,
        234, 38, 44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65,
        129, 77, 82, 106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123,
        8, 12, 189, 177, 74, 120, 136, 149, 139, 227, 99, 232, 109, 233,
        203, 213, 254, 59, 0, 29, 57, 242, 239, 183, 14, 102, 88, 208, 228,
        166, 119, 114, 248, 235, 117, 75, 10, 49, 68, 80, 180, 143, 237,
        31, 26, 219, 153, 141, 51, 159, 17, 131, 20
    ]

    block_size = 16
    message_bytes = bytearray(message, 'utf-8')
    padding = block_size - (len(message_bytes) % block_size)
    message_bytes += bytearray(padding for _ in range(padding))
    prev_checkbyte = 0
    checksum = bytearray(0 for _ in range(block_size))

    for i in range(len(message_bytes) // block_size):
        for j in range(block_size):
            byte = message_bytes[i * block_size + j]
            prev_checkbyte = checksum[j] = S[byte ^ prev_checkbyte]

    message_bytes += checksum
    buff_size = 48
    digest = bytearray([0 for _ in range(buff_size)])
    n = 18

    for i in range(len(message_bytes) // block_size):
        for j in range(block_size):
            digest[block_size + j] = message_bytes[i * block_size + j]
            digest[2 * block_size + j] = digest[block_size + j] ^ digest[j]

        prev_hashbyte = 0
        for j in range(n):
            for k in range(buff_size):
                digest[k] = prev_hashbyte = digest[k] ^ S[prev_hashbyte]

            prev_hashbyte = (prev_hashbyte + j) % len(S)

    md2_hash = binascii.hexlify(digest[:16]).decode('utf-8')
    return md2_hash


def main():
    print('-'*100)
    message = input('Enter the message: ')
    sha1_hash = SHA1(message)
    print('Hash of the message (SHA1): ', sha1_hash)
    md2_hash = MD2(message)
    print('Hash of the message (MD2): \t', md2_hash)
    print('-' * 100)


if __name__ == '__main__':
    main()
