def print_3_times():
    print("hello world")
    print("안녕하세요")
    print("99999")

def print_n_times(value,n):
    for i in range(n):
        print(value, end=" ")

# print_3_times()

#print_n_times("hello",4)

# def func(a,b=10,c=20):
#     print(a+b+c)
# func(10)
# func(a=10,b=50,c=100)

# def return_test():
#     print("Value A")
#     return 100
#     print("Value B")

# value=return_test()
# print(value)

def multi_all(start,end):
    output=1
    for i in range(start,end+1):
        output*=i
    return output

print(multi_all(1,10000))