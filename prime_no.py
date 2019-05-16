num = int(input('enter no:'))
if num == 1 or num == 0 or num <= 0:
    print(num,' is not prime')
elif num == 2 :
    print(num, 'is prime')
else:
    is_prime = True
    for i in range (2, num):
        print(i)
        if num % i == 0:
           is_prime = False
           break   #completely divide so it is not prime cond false
    if is_prime:
        print(num,'is prime')
    else:
        print(num, 'is not prime')

