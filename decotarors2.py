#decorators finctios:
def discount(func):
    def offer(a,b):
        if a >= 1000:
            print("You Have eligiable for 30% of diccount on your bill, on a product only")
            amount = (a - 30)/100
            print("Discount with bill is :",amount)
        elif b >= 500:
            print("You Have eligiable for 15 % of diccount on your bill, on b product only") 
            amount = (b - 15)/100 
            print("Discount with bill is :",amount)               
        else:
            return func(a,b)
            print("Sorry Discconutis not appllicabe  for you.....")  
    return offer         
@discount 
def amazon(a,b):
    print("Thanks for amazon shopping a value sis {} and b value is {}".format(a,b))
    return a+b
print(amazon(10,89898))
