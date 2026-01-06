number=[]
even=0
odd=0

for i in range(10):
    num=int(input("enter yor number:"))
    number.append(num)

if num%2==0:
    even+=1
else:
    odd+=1
print("even number:",even)
print("odd number:",odd)
print(number)