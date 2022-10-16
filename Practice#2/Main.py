import Hex_Int_Lib as hil


def main():
    # hex_value = int(input("Введите HEX значение которое хотите преобразовать в Little-/Big- Endian: "), 16)
    # little_endian, bytes = hil.from_hex_to_little_endian(hex_value)
    # big_endian, bytes = hil.from_hex_to_big_endian(hex_value)
    # print(little_endian, bytes)
    int_value = int(input("Введите HEX значение которое хотите преобразовать в Little-/Big- Endian: "))
    # hex = hil.from_little_endian_to_hex(int_value,32)
    big_hex = hil.from_big_endian_to_hex(int_value,32)
    print(big_hex)
    # print(big_endian)


if __name__ == '__main__':
    main()