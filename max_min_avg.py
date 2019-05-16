import random
arr= []  #declaring empty array 
s=0
a = 0     # max
b = 1001  # min


for x in range(10):  
    #append  
    arr.append(random.randint(10,1000))
    #max min
    if x>0:
        
        if arr[x] > arr [x-1] and arr[x] > a: 
            a = arr[x]
            i_max= x
            if arr[x] > arr[x-1] and arr[x-1] < b:
                b = arr[x-1]
                i_min = x

        elif arr[x] < arr[x-1] and arr[x] < b: 
            b = arr[x]
            i_min = x

  #printing and calculating mean 
print('VALUES')
for num in arr:
    print(num)
    s = s + num
mean = s/ len(arr)

print('Sum = ' , s)
print('Mean = ' , mean)
print('Max value = ' , a , "   Index = [" , i_max, ']')
print('Min value = ' , b , '    Index = [', i_min,']')