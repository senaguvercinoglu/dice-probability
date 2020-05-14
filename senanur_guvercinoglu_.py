import random

throwing_number = 790
even_result=0

for i in range(throwing_number):
    d1, d2, d3 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
    sum= d1+d2+d3
    if sum%2==0:
        even_result+=1


    print "dice 1:", (d1), "dice 2:", d2, "dice 3:", d3
print "The probability of even sum is:",(float(even_result)/float(throwing_number)*100),"%"




