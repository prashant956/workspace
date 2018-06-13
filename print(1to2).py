name=input("enter a string:").strip()
name=name.lower()
if name =='foo':
    print('bar')
elif name=='bar':
    print('foo')
else:
    print('invalid choice')
