# Decimal(10) To Binary(2)
# Decimal(10) To Octal(8)
# Decimal(10) To Hexadecimal(16)
# Binary(2) To Decimal(10)
# Octal (8)To Decimal(10)
# Hexadecimal (16) To Decimal(10)

import math

_MAX_FRACTIONAL_DIGIT = 10
_HEX_CODES = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}
_HEX_CODES_REV = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}


def _DecimalToAny(numStr, digit):
    result = ''
    strList = numStr.split('.')
    integer = int(strList[0])

    while integer != 0:
        quotient, remainder = divmod(integer, digit)
        integer = quotient
        if digit == 16:
            result = _ToHex(remainder) + result
        else:
            result = str(remainder) + result

    if len(strList) == 2:
        result += '.'
        fractional = float('0.' + strList[1])

        i = 0
        while fractional != 0 and i != _MAX_FRACTIONAL_DIGIT:
            calc = fractional * digit
            _integer = int(calc)
            fractional = calc - _integer
            if digit == 16:
                result += _ToHex(_integer)
            else:
                result += str(_integer)

            i += 1

    return result


def _AnyToDecimal(numStr, digit):
    result = 0
    strList = numStr.split('.')
    integer = strList[0]

    for index, item in enumerate(integer[::-1]):
        value = _ToInt(item)
        result += (int(value) * (digit ** index))

    if len(strList) == 2:
        result = float(result)
        fractional = strList[1]

        for index, item in enumerate(fractional):
            value = _ToInt(item)
            result += (int(value) * (digit ** ((index + 1) * -1)))

    return str(result)


def _ToHex(code):
    if isinstance(code, int) and code in _HEX_CODES:
        return str(_HEX_CODES[code])

    return str(code)


def _ToInt(code):
    if isinstance(code, str) and code in _HEX_CODES_REV:
        return _HEX_CODES_REV[code]

    return str(code)


# (10)->(2)
def DecimalToBinary(num):
    return _DecimalToAny(num, 2)


# (10)->(8)
def DecimalToOctal(num):
    return _DecimalToAny(num, 8)


# (10)->(16)
def DecimalToHexadecimal(num):
    return _DecimalToAny(num, 16)


# (2)->(10)
def BinaryToDecimal(num):
    return _AnyToDecimal(num, 2)


# (8)->(10)
def OctalToDecimal(num):
    return _AnyToDecimal(num, 8)


# (16)->(10)
def HexadecimalToDecimal(num):
    return _AnyToDecimal(num, 16)


if __name__ == '__main__':
    decimalToBinary1 = DecimalToBinary('12')
    decimalToBinary2 = DecimalToBinary('15.625')
    decimalToOctal1 = DecimalToOctal('395')
    decimalToOctal2 = DecimalToOctal('17.25')
    decimalToHexadecimal1 = DecimalToHexadecimal('2748')
    decimalToHexadecimal2 = DecimalToHexadecimal('799.375')
    binaryToDecimal1 = BinaryToDecimal('101')
    binaryToDecimal2 = BinaryToDecimal('1101.101')
    octalToDecimal1 = OctalToDecimal('26')
    octalToDecimal2 = OctalToDecimal('162.4')
    hexadecimalToDecimal1 = HexadecimalToDecimal('4EB')
    hexadecimalToDecimal2 = HexadecimalToDecimal('B2.5')

    # print('decimalToBinary1: ', decimalToBinary1)
    # print('decimalToBinary2: ', decimalToBinary2)
    # print('decimalToOctal1: ', decimalToOctal1)
    # print('decimalToOctal2: ', decimalToOctal2)
    # print('decimalToHexadecimal1: ', decimalToHexadecimal1)
    # print('decimalToHexadecimal2: ', decimalToHexadecimal2)
    # print('binaryToDecimal1: ', binaryToDecimal1)
    # print('binaryToDecimal2: ', binaryToDecimal2)
    # print('octalToDecimal1: ', octalToDecimal1)
    # print('octalToDecimal2: ', octalToDecimal2)
    # print('hexadecimalToDecimal1: ', hexadecimalToDecimal1)
    # print('hexadecimalToDecimal2: ', hexadecimalToDecimal2)

    assert decimalToBinary1 == '1100'
    assert decimalToBinary2 == '1111.101'
    assert decimalToOctal1 == '613'
    assert decimalToOctal2 == '21.2'
    assert decimalToHexadecimal1 == 'ABC'
    assert decimalToHexadecimal2 == '31F.6'
    assert binaryToDecimal1 == '5'
    assert binaryToDecimal2 == '13.625'
    assert octalToDecimal1 == '22'
    assert octalToDecimal2 == '114.5'
    assert hexadecimalToDecimal1 == '1259'
    assert hexadecimalToDecimal2 == '178.3125'
