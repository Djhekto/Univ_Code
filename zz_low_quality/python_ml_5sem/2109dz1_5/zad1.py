#print(hello()) # Hello!
#print(hello('')) # Hello!
#print(hello('Masha')) # Hello, Masha!


def hello(x):
    if x== None:
        return "Hello!" 
    if x=='':
        return "Hello!"
    a="Hello,"+x+"!"
    return a

#if __name__ == '__main__':#??????
#    print(hello())
#    print(hello(""))
#    print(hello("ML zadania"))
print(hello(None))
print(hello(""))
print(hello("ML zadania"))