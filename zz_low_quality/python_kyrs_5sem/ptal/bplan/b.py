from itertools import product
import sys
possible_encodings = ['cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp437', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp864', 'cp866', 'cp869', 'cp874', 'cp875', 'hp_roman8', 'iso8859_10', 'iso8859_16', 'iso8859_4', 'iso8859_5', 'koi8_r', 'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland', 'mac_latin2']
alp = '!"(),:;%АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЫЬЭЮЯ'.encode('koi8_r')

def main():
    buffer = sys.stdin.read().strip()
    head_tail = buffer[:4] + buffer[-4:]
    if head_tail == 'ПРОЦКНЦ;':
        print(buffer)
        return
    if 'KM' in head_tail or '×{´F' in head_tail:
        buffer = buffer.split('%')
    else:
        buffer = buffer.split('\n')
    possible_pairs = {}
    for (e1, e2) in product(possible_encodings, repeat=2):
        if e1 == e2:
            continue
        try:
            t1 = alp.decode(e1).encode(e2)
            codings = ((e2, e1),)
            possible_pairs[codings] = t1
            if head_tail.encode(e1).decode('koi8_r') == 'ПРОЦКНЦ;':
                res = []
                for line in buffer:
                    res.append(line.encode(e1, errors='ignore').decode('koi8_r', errors='ignore'))
                print('\n'.join(res))
                return
        except UnicodeEncodeError:
            continue
        except UnicodeDecodeError:
            continue
    possible_pairs_2 = {}
    for (pair, buff) in possible_pairs.items():
        for (e1, e2) in product(possible_encodings, repeat=2):
            if e1 == e2:
                continue
            try:
                if pair[0][0] == e1:
                    continue
                t1 = buff.decode(e1).encode(e2)
                codings = ((e2, e1),) + pair
                possible_pairs_2[codings] = t1
                ((c1, c2), (c3, c4)) = codings
                if head_tail.encode(c2).decode(c3).encode(c4).decode('koi8_r') == 'ПРОЦКНЦ;':
                    res = []
                    for line in buffer:
                        res.append(line.encode(c2).decode(c3).encode(c4).decode('koi8_r'))
                    print('\n'.join(res))
                    return
            except UnicodeEncodeError:
                continue
            except UnicodeDecodeError:
                continue
    for (pair, buff) in possible_pairs_2.items():
        for (e1, e2) in product(possible_encodings, repeat=2):
            if e1 == e2:
                continue
            try:
                if pair[0][0] == e1:
                    continue
                t1 = buff.decode(e1).encode(e2)
                codings = ((e2, e1),) + pair
                ((c1, c2), (c3, c4), (c5, c6)) = codings
                if head_tail.encode(c2).decode(c3).encode(c4).decode(c5).encode(c6).decode('koi8_r') == 'ПРОЦКНЦ;':
                    res = []
                    for line in buffer:
                        res.append(line.encode(c2).decode(c3).encode(c4).decode(c5).encode(c6).decode('koi8_r'))
                    print('\n'.join(res))
                    return
            except UnicodeEncodeError:
                continue
            except UnicodeDecodeError:
                continue
if __name__ == '__main__':
    main()