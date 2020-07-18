#decorator
def smart(func):
    def inner(a,b):
        if b == 0:
            print("not possible to calcualted with zero....")
            return 
        else:
            return func(a,b)
    return inner 
@smart
def div(a,b):
    return(a/b)

print(div(23,45))
print(div(2345,0))
 


