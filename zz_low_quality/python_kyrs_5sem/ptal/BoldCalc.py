from re import match, sub, search, compile

d = {}
m = globals()
base_mistake = compile(r'/{2,}|\*\*|[a-zA-Z0-9]\w*\(|\.|([^0-9A-Za-z_](\d)+[eE][+-]\d)')
name_for_sub = compile(r"(?<!\w)([a-zA-Z_]\w*)")
name_for_match = compile(r"([a-zA-Z_]\w*)\s*=\s*(.*)")
splitting_match = compile(r"([a-zA-Z_]\w*)\s*=\s*(.*)")


def work(f):
    if match(r"#", f) is None:
        if base_mistake.search(f):
            print("Syntax error")
            return 0
        f = sub(r"/", r"//", f)
        f = name_for_sub.sub(r"_c_\1", f)
        if name_for_sub.fullmatch(f):
            try:
                print(eval(f, m, d))
            except NameError:
                print("Name error")
                return 0
            else:
                return
        elif name_for_match.match(f):
            s = splitting_match.match(f)
            right = s.group(2)
            left = s.group(1)
            try:
                right = eval(right, m, d)
            except NameError:
                print("Name error")
                return 0
            except SyntaxError:
                print("Syntax error")
            else:
                try:
                    exec(left + "=" + str(right), m, d)
                except SyntaxError:
                    print("Syntax error")
                    return 0
                else:
                    return 0
        else:
            if search(r"=", f):
                print("Assignment error")
                return 0
            try:
                print(eval(f, m, d))
            except SyntaxError:
                print("Syntax error")
                return 0
            except NameError:
                print("Name error")
                return 0
            except BaseException:
                print("Runtime error")
                return 0
            else:
                return 0


s = input()
while s != '':
    work(s)
    try:
        s = input()
    except:
        break