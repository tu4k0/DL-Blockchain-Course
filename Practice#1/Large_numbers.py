import random
import math
import asyncio
from time import time


async def task1():
    print("Кол-во вариантов ключей, которые можно задать последовательностью:")
    for i in range(3,13):
        key_options = 2**2**i
        print(f"{2**i} бит: {key_options}")


async def task2():
    print("Сгенерированное случайное значение ключа в диапазоне 0х00.. до 0хFF.. при длине ключа: ")
    keys_array = []
    for i in range(3,13):
        key = hex(random.randint(0,2**2**i))
        keys_array.append(key.upper())
        print(f"{2**i} бит: 0x{key.upper()[2:]}")
    await task3(keys_array)


async def task3(keys_array):
    print("\n\nВыберите для ключа какой длиной бит необходимо выполнить брутфорс:")
    bit = int(input())
    start_time = time()
    key_index = int(math.log2(bit)-2)
    key = keys_array[key_index-1]
    hex_range = bit/4
    start_key = '0x'
    for i in range(0, int(hex_range)):
        start_key += '0'
    start = int(start_key, 16)
    end = int(key,16)
    while start != end:
        start += 1
    print(f"Количество времени, потраченного на нахождение ключа {hex(start).upper()} длиной {bit} бит составляет: {(time()-start_time)*1000} мс")


async def main():
    await task1()
    print("\n")
    await task2()


if __name__ == '__main__':
    asyncio.run(main())
