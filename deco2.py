def dec(old_func):
    def make_up(x,y):
        print("value of x=:",x)
        print("value of y=:",y)
        print("Result=",x+y)
        print("thanks")
    return make_up
@dec
def new(x,y):
    pass
new(3,4)
