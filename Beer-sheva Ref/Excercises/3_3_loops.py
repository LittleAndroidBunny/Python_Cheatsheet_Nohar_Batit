# This script is part of tutorial number 3 of introduction of computer science for EE students at BGU.
# Uncomment the parts that you want to run.
# Topics:
#    - break statement
#    - continue statement

# sqrt example
# see what happens for a positive and a negative number.
# what happens for zero?
# input_num = int(input('enter a number:'))
input_num = 5
# input_num = -9
estimate_pre = 3
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
Num = 5
while Num >= 0:
    if Num > 0:
        print(2 ** Num)
        Num -= 1
    else:
        continue
print("Done!")

# for loop
for i in range(6):
    print(i)

for i in range(1, 16, 3):
    print(i)
