x=int(input("Enter a value: "))
if x==0:
    print(1)
for i in range(x):
    if i==0:
        i=1
    else:
        n=i*(i-1)
print(x*n)
