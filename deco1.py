def hello(name):
    return "hello ,"+name
def dec(old_func):
    def make_up(x):
        s="Hello world! welcome to python\n"
        s+=old_func(x)
        s+="\nhi this is a decorator"
        return s
    return make_up
hello=dec(hello)

k=hello("prashant")
print(k)
