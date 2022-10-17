import Hex_Int_Lib as hil


def main():
    print('\n')
    print("-" * 100)
    print("a. Convert HEX --> Little-Endian")
    hex_value = input("Enter HEX value: ")
    little_endian, little_endian_bytes = hil.from_hex_to_little_endian(hex_value)
    print(f"Number of bytes: {little_endian_bytes}\nLittle-endian: {little_endian}")
    print("-"*100)
    print("b. Convert HEX --> Big-Endian")
    hex_value = input("Enter HEX value: ")
    big_endian, big_endian_bytes = hil.from_hex_to_big_endian(hex_value)
    print(f"Number of bytes: {big_endian_bytes}\nBig-endian: {big_endian}")
    print("-" * 100)
    print("c. Convert Little-Endian --> HEX")
    little_endian = input("Enter Little-Endian value: ")
    hex_value = hil.from_little_endian_to_hex(little_endian, little_endian_bytes)
    print(f"Number of bytes: {little_endian_bytes}\nHEX value: {hex_value}")
    print("-" * 100)
    print("d. Convert Big-Endian --> HEX")
    big_endian = input("Enter Big-Endian value: ")
    hex_value = hil.from_big_endian_to_hex(big_endian, big_endian_bytes)
    print(f"Number of bytes: {big_endian_bytes}\nHEX value: {hex_value}")
    print("-" * 100)


if __name__ == '__main__':
    main()