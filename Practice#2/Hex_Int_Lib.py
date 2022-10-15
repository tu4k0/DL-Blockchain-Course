def from_hex_to_little_endian(value):
    hex_bytes = value.to_bytes(value.bit_length() // 8, byteorder='little')
    hex_bytes_list = list(hex_bytes)
    hex_bytes_amount = value.bit_length() // 8
    little_endian_bytes_list = ''
    little_endian_hex = '0x'
    for byte in range(0, len(hex_bytes_list)):
        little_endian_bytes_list += str(hex(hex_bytes_list[byte]))
    little_endian_bytes_list = little_endian_bytes_list[:].split('0x')
    for byte in range(0, len(little_endian_bytes_list)):
        little_endian_hex += str(little_endian_bytes_list[byte])
    little_endian = int(little_endian_hex, 16)
    return little_endian, hex_bytes_amount


def from_hex_to_big_endian(value):
    print(f'big endian: {value}')


def from_little_endian_to_hex(value):
    print(f'hex: {value}')


def from_big_endian_to_hex(value):
    print(f'hex: {value}')
