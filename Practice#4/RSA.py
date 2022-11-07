import random


def main():
    def check_prime(n):
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    cached_primes = [i for i in range(1, 100) if check_prime(i)]
    p = random.choice([i for i in cached_primes])
    q = random.choice([i for i in cached_primes])
    n = p * q
    e = 0
    k = 0
    j = True

    def Eiler(p, q):
        e = (p - 1) * (q - 1)
        return e

    e = Eiler(p, q)

    def relatively(e, k):
        while (e and k):
            if e>k:
                e %= k
            else:
                k %= e
        if (e+k == 1):
            return True
        else:
            return False


    while j:
        k = random.randint(1, e)
        if relatively(e, k) == True:
            j = False
        else:
            continue

    print(k, e)

    d=1
    while True:
        if (d*k) % e == 1:
            break
        else:
            d+=1

    print(d)



    print(f'public key: ({k}, {n})')
    print(f'private key: ({d}, {n})')

    message = input('Enter message: ')

    arr = list(message)

    encode_message = ''
    for i in range(0, len(arr)):
        print(ord(arr[i]))
        arr[i] = (ord(arr[i])**k) % n
        encode_message += str(arr[i]) + ' '

    decode_message = ''
    for i in range(0, len(arr)):
        arr[i] = (arr[i] ** d) % n
        decode_message += chr(arr[i])

    print(decode_message)

if __name__ == '__main__':
    main()
