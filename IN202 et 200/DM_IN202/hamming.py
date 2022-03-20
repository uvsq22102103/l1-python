def parité(bits:list, indices:list):
    out = 0
    for bit in indices:
        out += bits[bit]
    return out % 2


def hamming(bits:list):
    c1, c2, c3 = parité(bits,[0,1,3]), parité(bits,[0,2,3]), parité(bits,[2,1,3])
    return [c1,c2,bits[0],c3,bits[1],bits[2],bits[3]]


def reverse_hamming(bits:list):
    c1, c2, c3 = parité(bits,[0,1,4]), parité(bits,[0,2,4]), parité(bits,[2,1,4])
    k1, k2, k3 = bits[0], bits[1], bits[3]
    if c1 != k1 and c2 != k2 and c3 == k3:
        bits[0] = 0 if bits[0] == 1 else 1
        return [bits[0], bits[1], bits[2], bits[4]]
    elif c1 != k1 and c2 == k2 and c3 != k3:
        bits[1] = 0 if bits[1] == 1 else 1
        return [bits[0], bits[1], bits[2], bits[4]]
    elif c1 == k1 and c2 != k2 and c3 != k3:
        bits[2] = 0 if bits[2] == 1 else 1
        return [bits[0], bits[1], bits[2], bits[4]]
    elif c1 != k1 and c2 != k2 and c3 != k3:
        bits[4] = 0 if bits[4] == 1 else 1
        return [bits[0], bits[1], bits[2], bits[4]]
    elif c1 == k1 and c2 == k2 and c3 == k3:
        return [bits[0], bits[1], bits[2], bits[4]]
    elif c1 != k1 and c2 == k2 and c3 == k3:
        return [bits[0], bits[1], bits[2], bits[4]]
    elif c1 == k1 and c2 != k2 and c3 == k3:
        return [bits[0], bits[1], bits[2], bits[4]]
    elif c1 == k1 and c2 == k2 and c3 != k3:
        return [bits[0], bits[1], bits[2], bits[4]]

print(hamming([1,1,0,0]))
print(reverse_hamming([0,1,1,1,1,0,0]))
