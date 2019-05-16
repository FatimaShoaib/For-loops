num = int(input('enter no:'))
if num == 1 or num == 0 or num <= 0:
    print(num,' is not prime')
elif num == 2 :
    print(num, 'is prime')
else:
    iter = 2
    for i in range(2,num):
        iter += 1
        if num % i == 0:
            break
    if iter == num:
        print(num,'is prime')
    else:
        print(num, 'is not prime')

