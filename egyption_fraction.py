from math import ceil

def egyptian(n,d):
    print("The Egyptian Fraction of {}/{}".format(n,d))
    ans = []
    while(n>0):
        x = ceil(d/n)       #minimal larger denominator
        #print (x)
        ans.append(x)       #append it to numerator list
        n,d = x*n-d, d*x    #update the remainder to n and d
    for a in ans:
        print("1/{}".format(a), end=" ")

print (egyptian(5, 121))
#answer: 1/25 1/757 1/763309 1/873960180913 1/1527612795642093385023488
print (egyptian(7, 15))
#answer:1/3 1/8 1/120

print (egyptian(23, 34))
#answer:1/2 1/6 1/102

print (egyptian(121, 321))
#answer:1/3 1/23 1/7383

print (egyptian(5, 123))
#answer:1/25 1/1538 1/4729350

