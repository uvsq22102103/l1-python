def parité(bits:list, indices:list):
    out = 0
    for bit in indices:
        out += bits[bit]
    return out % 2


def hamming(bits: list):
    c1, c2, c3 = parité(bits, [0, 1, 3]), parité(bits, [0, 2, 3]), parité(bits, [2, 1, 3])
    return [bits[0], bits[1], bits[2], bits[3], c1, c2, c3]


def switch_bin(binary: int):
    if binary == 0:
        binary = 1
    else:
        binary = 0
    return binary


def reverse_hamming(bits: list):
    c1, c2, c3 = parité(bits, [0, 1, 3]), parité(bits, [0, 2, 3]), parité(bits, [2, 1, 3])
    if c1 != bits[-3] and c2 != bits[-2] and c3 != bits[-1]:
        bits[3] = switch_bin(bits[3])
    elif c2 != bits[-2] and c3 != bits[-1]:
        bits[2] = switch_bin(bits[2])
    elif c1 != bits[-3] and c3 != bits[-1]:
        bits[1] = switch_bin(bits[1])
    elif c1 != bits[-3] and c2 != bits[-2]:
        bits[0] = switch_bin(bits[0])
    return [bits[0], bits[1], bits[2], bits[3]]
