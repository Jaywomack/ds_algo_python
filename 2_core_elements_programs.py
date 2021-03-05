# In this problem you'll be given a chance to practice writing some while loops.
#
# 1. Convert the following into code that uses a while loop.
#
# prints 2
# prints 4
# prints 6
# prints 8
# prints 10
# prints Goodbye!

num = 0

while num < 10:
    num += 2
    print(num)
print('Goodbye!')


#
#
#
# Exercise: while exercise 2
# 5.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 5 minutes
#
# 2. Convert the following into code that uses a while loop.
#
# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2
num = 10
print('Hello')
while num >0:
    print(num)
    num -= 2
#
#
# 3. Write a while loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So, for example, if we define end to be 6, your code should print out the result:
#
# 21
# which is 1 + 2 + 3 + 4 + 5 + 6.

num = 1
count = 0
end=20
while num <= end:
    count += num
    num += 1

print(count)

'''
1. Convert the following code into code that uses a for loop.

prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
'''

for i in range(0,10,-2):
    print(i)
print('Goodbye!')

# 2. Convert the following code into code that uses a for loop.
#
# prints Hello!
# prints 10
# prints 8
# prints 6
# prints 4
# prints 2
#

print('Hello!')
for i in range(10,0,-2):
    print(i)


print('Hello!')
for i in range(10,0,-2):
    print(i)

# 3. Write a for loop that sums the values 1 through end, inclusive. end is a variable that we define for you. So,
# for example, if we define end to be 6, your code should print out the result:

count= 0
end = 6
for i in range(end + 1):
    count += i

print(count)