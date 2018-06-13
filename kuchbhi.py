mydict={}
while input("Type something to coutinue:"):
    d=input("enter key=value pair:").split('=')
    if d[0] in mydict:
        print("error:key already exist")
        print("try again")
    else:
        mydict.update((d,))

print(mydict)
