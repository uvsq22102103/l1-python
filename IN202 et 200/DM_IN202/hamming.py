def parité(bits:list, indices:list):
    out = 0
    for bit in indices:
        out += bits[bit]
    return out % 2


def hamming(bits:list):
    c1, c2, c3 = parité(bits,[0,1,3]), parité(bits,[0,2,3]), parité(bits,[2,1,3])
    return [c1,c2,bits[0],c3,bits[1],bits[2],bits[3]]


def reverse_hamming(bits:list):
    c1, c2, c3 = parité(bits,[2,4,6]), parité(bits,[2,5,6]), parité(bits,[4,5,6])
    k1, k2, k3 = bits[0], bits[1], bits[3]
    if c1 == k1 and c2 == k2 and c3 == k3:
        return [bits[2],bits[4],bits[5],bits[6]]
    elif c1 != k1 and c2 != k2 and c3 == k3:
        bits[2] = 0 if bits[2] == 1 else 0
        return [bits[2],bits[4],bits[5],bits[6]]
    elif c1 == k1 and c2 != k2 and c3 != k3:
        bits[5] = 0 if bits[5] == 1 else 0
        return [bits[2],bits[4],bits[5],bits[6]]
    elif c1 != k1 and c2 == k2 and c3 != k3:
        bits[4] = 0 if bits[4] == 1 else 0
        return [bits[2],bits[4],bits[5],bits[6]]
    elif c1 != k1 and c2 != k2 and c3 != k3:
        bits[6] = 0 if bits[6] == 1 else 0
        return [bits[2],bits[4],bits[5],bits[6]]
    elif c1 != k1 and c2 == k2 and c3 == k3:
        return [bits[2],bits[4],bits[5],bits[6]]
    elif c1 == k1 and c2 != k2 and c3 == k3:
        return [bits[2],bits[4],bits[5],bits[6]]
    elif c1 == k1 and c2 == k2 and c3 != k3:
        return [bits[2],bits[4],bits[5],bits[6]]


test = hamming([1, 1, 0, 0])
print(test)
tests = [[1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0, 1]]
print(reverse_hamming(test))
print('\n')
for i in tests:
    print(reverse_hamming(i))
