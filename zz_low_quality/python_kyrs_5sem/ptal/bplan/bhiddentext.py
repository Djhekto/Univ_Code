def ff():
    text = input()
    tlen = len(text)
    b = input()
    zero = 0
    blen = len(b)
    if blen > tlen:
        print('NO')
        return
    if blen == zero:
        print('YES')
        return
    (i, j, step, cur_begin) = (zero, zero, zero, zero)
    one = 1
    while i < tlen:
        while i < tlen and text[i] != b[j]:
            i += one
        if i >= tlen:
            print('NO')
            return
        else:
            cur_begin = i
            j += one
            if j >= blen:
                print('YES')
                return
            while i < tlen and text[i] != b[j]:
                i += 1
                step += 1
            if i >= tlen:
                print('NO')
                return
            else:
                while i < tlen and j < blen and (text[i] == b[j]):
                    j += 1
                    i += step
                if j == blen:
                    print('YES')
                    return
                else:
                    i = cur_begin + 1
                    step = 0
                    j = 0
    print('NO')


ff()