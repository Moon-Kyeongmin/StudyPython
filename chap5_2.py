import time

def factorial(n):
    output=1
    for i in range(1,n+1):
        output*=i
    return output

print(factorial(3)) 


def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(3))

dictionary={
    1:1,
    2:1,
}

def fibo(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output=fibo(n-1)+fibo(n-2)
        dictionary[n]=output
        return output



start=time.time()
print("fibo(35)",fibo(35))
print("실행시간 : ",time.time()-start,"sec")