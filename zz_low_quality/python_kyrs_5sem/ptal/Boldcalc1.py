from re import match, sub, search, compile

def ff():
    while 1:
        try:
            s1 = input()
            if s1[0]!="#":
                otvet = main(s1)
                #print(s1,': ',otvet)
                if otvet!="do not print me":
                    print(otvet)
        except:
            break#EOF

osibki1 = compile(r'/{2,}|\*\*|[a-zA-Z0-9]\w*\(|\.|([^0-9A-Za-z_](\d)+[eE][+-]\d)')
localdict = {}
globalki = globals()
imyadlyasubb = compile(r"(?<!\w)([a-zA-Z_]\w*)")
imyadlyamatch = compile(r"([a-zA-Z_]\w*)\s*=\s*(.*)")
mat1s = compile(r"([a-zA-Z_]\w*)\s*=\s*(.*)")
    
def main(str1):
    stemp1= "do not print me"
    if match(r"#", str1) is None:
        if osibki1.search(str1):
            return "Syntax error"
        str1 = sub(r"/", r"//", str1)
        str1 = imyadlyasubb.sub(r"_c_\1", str1)
        if imyadlyasubb.fullmatch(str1):
            try:
                return eval(str1, globalki, localdict)
            except NameError:
                return "Name error"
        elif imyadlyamatch.match(str1):
            s = mat1s.match(str1)
            right = s.group(2)
            left = s.group(1)
            try:
                right = eval(right, globalki, localdict)
            except NameError:
                return "Name error"
            except SyntaxError:
                print("Syntax error")
                return stemp1
            else:
                try:
                    #print("exec",left,right,m,d)
                    exec(left + "=" + str(right), globalki, localdict)
                except SyntaxError:
                    return "Syntax error"
                else:
                    return stemp1
        else:
            if search(r"=", str1):
                return "Assignment error"
            try:
                return eval(str1, globalki, localdict)
            except SyntaxError:
                return "Syntax error"
            except NameError:
                return "Name error"
            except BaseException:
                return "Runtime error"


ff()