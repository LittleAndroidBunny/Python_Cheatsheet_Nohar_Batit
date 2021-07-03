def get_int(x):
    y=x+10
    return y
b= get_int(5)
#1.
#get an integer from the user and say if divided by 2 or 3 or both
print ("Exercise 1:")
num = int(input("Please enter an integer number: "))
if num%2 == 0 and num%3 == 0 :
   print(num , "is devided by 2 and 3")
elif num%2 == 0 :
    print(num , "is devided by 2" )
elif num%3 == 0  :
    print(num , "is devided by 3")
else:
    print(num , "is not divided by 2, and is not divided by 3")
#2.
#Get 3 numbers and print the smallest
print ("Exercise 2:")
num1 = float(input("Please enter a first number: "))
num2 = float(input("Please enter a second number: "))
if num1<num2:
    num2=num1
num3 = float(input("Please enter a third number: "))
if num2<num3:
    num3=num2
print (num3 ,"is the smallest number")
#3.
#get two integers calculate lcm number that divided by both and print it (=!1) print ("Exercise 3:")
i=1
num1 = int(input("Please enter your first integer number: "))
num2 = int(input("Please enter your second integer number: "))
while (i<num1*num2):
    if (i%num1==0 and i%num2==0):
        break
    i+=1
print(i, "is the LCM (least common multiple) of",num1,"and",num2)
#4.
#get 20 integers and print the largest even
print ("Exercise 4:")
x=int(input("Please enter an integer number 1: "))
for i in range (19):
    z=int(input(f"Please enter an integer number {i+2}: "))
    if z%2==0 and (z>x or x%2!=0):
        x=z
if x%2==0:
    print(x, "is the greatest even number")
else:
    print("All the numbers are odd")
#5.
 #get integer a and print b & c, b**c=a, 0<c<6
print("Exercise 5:")
a = int(input("Please enter an integer number: "))
print ("a=",a)
print ("Solutions to the equation b**c=a with b an integer and 0<c<6 are: ")
print("a=b,c=1")
for b in range (-abs(a),abs(a)):
    for c in range (2,6):
        if b**c==a:
            print("And: b="+str(b),"c="+str(c))
#6.
# Get numbers separated by commas and print the sum
print ("Exercise 6:")
s=input("Please insert numbers separated by commas: ")
s=s+","
k="" # an empty string
sum=0
for l in s:
    if l!=",":
        k=k+l
    else:
        sum=sum+float(k)
        k="" # reset k
print("The sum is: ", sum)
#7.
# Get a list, get fav number, get location, change fav in the location, print both lists and each sum
print ("Exercise 7:")
lst1 = []
while len(lst1) < 5:
    lst1 = [int(item) for item in input("Enter more than 5 integers separated by space: ").split()]
Num_Fav = int(input("What is your favourite integer? "))
(Num_Loc) = len(lst1)+1
while int(Num_Loc) > len(lst1):
    Num_Loc = int(input(f"enter location between 1 & {len(lst1)}: "))
print(f"the first list is: {lst1} & the first list sum is: {sum(lst1)}")
lst1.pop(Num_Loc-1)
lst1.insert(Num_Loc-1,Num_Fav)
print(f"the second list is: {lst1} & the second list sum is: {sum(lst1)}")
