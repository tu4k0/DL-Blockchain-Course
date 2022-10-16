def from_hex_to_little_endian(hex_value):
    little_endian_bytes_list = ''
    little_endian_hex = '0x'
    hex_bytes = hex_value.to_bytes(hex_value.bit_length() // 8, byteorder='little')
    hex_bytes_list = list(hex_bytes)
    hex_bytes_amount = hex_value.bit_length() // 8
    for byte in range(0, len(hex_bytes_list)):
        little_endian_bytes_list += str(hex(hex_bytes_list[byte]))
    little_endian_bytes_list = little_endian_bytes_list[:].split('0x')
    for byte in range(0, len(little_endian_bytes_list)):
        little_endian_hex += str(little_endian_bytes_list[byte])
    little_endian_list = list(little_endian_hex[2:])
    decimal_degree = len(little_endian_list)
    little_endian = 0
    for i in range(0, len(little_endian_list)):
        decimal_degree -= 1
        little_endian += (int(little_endian_list[i], 16)) * (16 ** decimal_degree)
    return little_endian, hex_bytes_amount


def from_hex_to_big_endian(hex_value):
    big_endian_bytes_list = ''
    big_endian_hex = '0x'
    hex_bytes = hex_value.to_bytes(hex_value.bit_length() // 8, byteorder='big')
    hex_bytes_list = list(hex_bytes)
    hex_bytes_amount = hex_value.bit_length() // 8
    for byte in range(0, len(hex_bytes_list)):
        big_endian_bytes_list += str(hex(hex_bytes_list[byte]))
    big_endian_bytes_list = big_endian_bytes_list[:].split('0x')
    for byte in range(0, len(big_endian_bytes_list)):
        big_endian_hex += str(big_endian_bytes_list[byte])
    big_endian_list = list(big_endian_hex[2:])
    decimal_degree = hex_bytes_amount*2
    big_endian = 0
    for i in range(0, len(big_endian_list)):
        decimal_degree -= 1
        big_endian += (int(big_endian_list[i], 16))*(16**decimal_degree)
    return big_endian, hex_bytes_amount


def from_little_endian_to_hex(little_endian, bytes):
    hex_list = []
    little_endian = int(little_endian)
    hex_value = '0x'
    for i in range(0, int(bytes)):
        if little_endian % 16 == 0:
            break
        ost = hex(little_endian % 16)
        hex_list.append(hex(little_endian % 16)[2:])
        little_endian = little_endian // 16
        if ost < '0xff':
            hex_list[i]+=hex(little_endian % 16)[2:]
            little_endian = little_endian // 16
            hex_cell = str(hex_list[i])
            cell = list(hex_cell)
            cell[0], cell[1] = cell[1], cell[0]
            hex_list[i] = ''.join(cell)
    for byte in range(0, (int(bytes)-len(hex_list))*2):
        hex_value += '0'
    hex_value += ''.join(hex_list)
    return hex_value


def from_big_endian_to_hex(value):
    print(f'hex: {value}')
