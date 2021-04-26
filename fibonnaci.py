def fibo(number):
    if number < 1:
        raise Exception
    elif number==1 or number==2:
        return number-1
    else:
        return fibo(number-1)+fibo(number-2)

count=1
while count <= 9:
    print(f'{fibo(count)}',end=' ')
    count+=1