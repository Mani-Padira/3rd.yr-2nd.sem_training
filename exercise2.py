#write a python program to get output 5,4,3,2,1 using slicing
numbers = [1, 2, 3, 4, 5]
result = numbers[::-1]
print(','.join(map(str, result)))

#print multiplication table for the given number from input
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
#print multiplication table for the given number from input using function
#print multiplication table for the given number from input using function
def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
num = int(input("Enter a number to print its multiplication table: "))
table(num)