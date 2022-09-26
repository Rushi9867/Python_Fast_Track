def Fn1():
    print("This is my first function module")

def Fn2():
    print("This is my second function module")

def Fn3():
    print("This is my third function module")

def even_num(a):
    if type(a) == int:
        if a%2 == 0:
            print(f"{a} is a Even number")
        else:
            print(f"{a} is a odd number") 
    else:
        print("Please enter only integer value")

even = []
def even(*args):
    for i in args:
        if type(i) == int:
            if i%2 == 0:
                even.append(args)
            else:
                print(i," is not an even number")
        else:
            raise Exception("Error is: ",i)

try:
    even(*args)
except Exception as e:
        print(e)
finally:
    print("Even no: ",even)
    print("Code Executed")
