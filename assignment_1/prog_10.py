l=list(range(1,101))
odd=list()
sum = 0
for n in l:
    if n%2 !=0 :
        odd.append(n)
        sum += n

print(sum,"is the sum of odd number between 1 to 100")  