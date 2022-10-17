# Practice #2. HEX<->. Описание

## Язык программирования: 
Python  

## Особенности реализации
В качестве реализации создания собственной библиотеки для конвертации HEX<-> было создано модуль Hex_Int_lib.py, в котором описано алгоритм конвертации в виде 4 функций с аргументами и возвращаемыми значениями: 
1. from_hex_to_little_endian(hex_value) - принимает в качестве аргумента hex значение (0x..), возвращает little_endian integer и количество байт hex значения;
2. from_hex_to_big_endian(hex_value) - принимает hex значение (0x..), возвращает big_endian integer и количество байт hex значения;
3. from_little_endian_to_hex(little_endian, bytes) - принимает little_endian integer и количество байт в котором проводить конвертацию, возвращает hex значение;
4. from_big_endian_to_hex(big_endian, bytes) - принимает big_endian integer и количество байт в котором проводить конвертацию, возвращает hex значение;

## Результат работы програмы
Practice#2_Result.png  
![Image text](https://github.com/tu4k0/DL-Blockchain-Course/blob/main/Practice%232/Practice%232_Result.png)