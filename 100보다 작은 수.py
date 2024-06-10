odds=[]
while True:
    num = input("100보다 작은 수를 입력하세요(끝내려면 N을 입력하세요): ")
    if num == 'n':break
    num = int(num)
    if num > 100:
            print("100보다 작은 수를 입력하세요")
            continue
    if num % 2 !=0:
            odds.append(num)
print(odds)