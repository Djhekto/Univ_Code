class init(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        new_cls = super(init, mcs).__new__(mcs, name, bases, namespace, **kwargs)
        user_init = new_cls.__init__
        
        def __init__(self, *args, **kwargs):
            print("New __init__ called")
            user_init(self, *args, **kwargs)
            self.extra()
            
        print("Replacing __init__")
        setattr(new_cls, '__init__', __init__)
        return new_cls


class C(metaclass=init):
    def __init__(self, var: int, rng: range, lst: list[int], defined: str = "defined"):
        self.data = f"{var}/{rng}/{lst}/{defined}"

c = C()
print(c.data)
c = C(1, range(3))
print(c.data)
c = C(rng=range(4, 7))
print(c.data)
c = C(lst=[1, 2, 3], defined=3)
print(c.data)