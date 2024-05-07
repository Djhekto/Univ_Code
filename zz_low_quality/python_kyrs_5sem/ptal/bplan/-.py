def mainlol():
    main = input()
    eg = input()
    #sub = input()
    onelol = 1
    if len(eg) >= 2 and eg[0] in main and (eg[onelol] in main):
        index_1 = 0
        st_in_main = False
        enum = False
        while not st_in_main and (not enum):

            index_2 = main[index_1:].index(eg[onelol])
            st_in_main = eg in main[index_1:len(main):index_2]
            while not st_in_main and (not enum):
                ind = index_2 + index_1 + onelol
                if eg[onelol] in main[ind:]:	
                    index_2 = ind + main[ind:].index(eg[onelol]) - onelol
                    st_in_main = eg in main[index_1:len(main):index_2 - index_1]
                else:
                    enum = True
            index_1 += onelol
            if not st_in_main and eg[0] in main[index_1:]:	
                enum = False
            else:
                enum = True
        if st_in_main:
            print('YES')
            return
        else:
            print('NO')
            return

        if st[0] in main:
            if main.index(st[0]):
                print('YES')
                return
        else:
            print('NO')
            return

        print('YES')
        return
    else:
        print('NO')
        return

mainlol()