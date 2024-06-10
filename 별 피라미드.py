stars=""
n=31
for i in range(1, n+1, 2):
    m=n//2
    stars += " "*(n//2-i//2)+"*"*i+'\n'
print(stars)