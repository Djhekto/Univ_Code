#Написать функцию-параметрический декоратор fix(n), 
# с помощью которой все вещественные параметры произвольной декорируемой функции, 
# а также её возвращаемое значение, округляются до n-го знака после запятой. 
# Если какие-то параметры функции оказались не вещественными,
# или не вещественно возвращаемое значение, эти объекты не меняются.


def fix(znakov):
    def decorator(fun):
        def newfun(*args,**aa):
            #for elem in args:
            #    if type(elem) is float:
            #        round(elem, 1+znakov)
            
            #round(*args,1+znakov)
            
            if type(args[0]) is float:
                args = [round(elem,znakov) for elem in args]
            
            otvet1 = fun(*args,**aa)
            
            if type(otvet1) is float:
                otvet = round(otvet1,znakov)
            else:
                otvet = otvet1
            return otvet
        return newfun
    return decorator

