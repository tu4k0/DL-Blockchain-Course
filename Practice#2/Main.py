import Hex_Int_Lib as hil


def main():
    hex_value = input("Введите hex значение которое хотите преобразовать: ")
    hil.from_hex_to_lil_endian(hex(int(hex_value, 16)))


if __name__ == '__main__':
    main()