import Hex_Int_Lib as hil


def main():
    hex_value = int(input("Введите HEX значение которое хотите преобразовать в Little-/Big- Endian: "), 16)
    little_endian, bytes = hil.from_hex_to_little_endian(hex_value)
    big_endian, bytes = hil.from_hex_to_big_endian(hex_value)
    print(little_endian, bytes)
    print(big_endian)


if __name__ == '__main__':
    main()