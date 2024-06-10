numbers=[3,5,4,3,7,5,7,8,5,7,9,2,3,1,6,9,4]
counter={}

for n in numbers:
    if n in counter:
        counter[n] += 1
    else:
        counter[n] =1
print(counter)