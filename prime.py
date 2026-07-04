n=10
count=1
for i in range(2,n+1):
    if n%i ==0:
        count+=1
if count==1:
    print(f"{n} is the prime number")
else:
    print(f"{n}not a prime number")