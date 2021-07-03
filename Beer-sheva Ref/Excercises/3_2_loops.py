# This script is part of lecture number 2 of introduction of computer science for EE students.
# Uncomment the parts that you want to run.
# explain sLoops
# explain strings

N = 6
while N:
    print(N)
    N -= 1      # abbreviation of N = N - 1
print("Blastoff!!\n\n")

# sqrt example
# see what happens for a positive and a negative number.
#what happens for zero?
#input_num = int(input('enter a number:'))
input_num = 3
#input_num = -9
estimate_pre = 1
estimate_post = 3
while True:
    estimate_post = (estimate_pre + input_num/estimate_pre)/2
    if estimate_post == estimate_pre:
        print('final estimate:', estimate_pre)
        break
    print('sqrt estimate:', estimate_pre)
    estimate_pre = estimate_post

print("\n\nNext Example!!\n\n")


# continue example
Num = 11
# print odd numbers
while Num:
    Num -= 1
    if not Num % 2:
        continue
    print(Num)
    print(Num-1)
    print(Num-2)
    "--"


# for loop
for i in range(6):
    print(i)

for i in range(1, 16, 3):
    print(i)

s1 = 'Spam' * 5
for i in s1:
    print(i, end="*")
print('')

# Example

Num = 5
# while Num >= 0:
#      if Num > 0:
#          print(2 ** Num)
#          Num -= 1
#      else:
#         continue
# print("Done!")
