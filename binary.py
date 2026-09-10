

# input: integer
# output: list of bits (most significant bit on the first position)
def toBinary(n):
    result = []
    while n > 0:
        result.append(n % 2)
        n = n // 2
    result.reverse()
    return result

# input: list of bits (most significant bit on the first position)
# output: integer
def fromBinary(bits):
    result = 0
    for bit in bits:
        result = result * 2 + bit
    return result

# input: character
# output: list of 8 bits.
def encodeCharacter(c):
    result = toBinary(ord(c))
    n = len(result)
    return  [0] * (8-n) + result

# input: list of 8 bits.
# output: corresponding character
def decodeCharacter(bits):
    return chr(fromBinary(bits))

# input: message as string
# output: list of bits.
def encodeMessage(message):
    result = []
    for c in message:
        result = result + encodeCharacter(c)
    return result

# input: list of bits. Each character takes 8 bits.
# output: message as string
def decodeMessage(message):
    result = ""
    while len(message)>0:
     first_chunk = message[0:8]
     c = decodeCharacter(first_chunk)
     result = result + c
     message = message[8:]
    return result

# print(encodeMessage("Kanelbulle"))
print(decodeMessage([0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]))
