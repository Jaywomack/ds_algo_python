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

# check if is a perfect cube
# # x = int(input('please input an integer'))
# ans = 0
# while ans ** 3 < x:
#     ans = ans + 1
# if ans **3 != x:
#     print(str(x) + ' is not a perfect cube')
# else:
#     print('Cube root of ' + str(x) + ' is ' + str(ans) )

# to make this code work with negative numbers as well abs and an if statement can be used to modify it
x= int(input('please input an integer'))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect match')
else:
    if x < 0:
        ans = - ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))


# using a for loop to find a cube
cube = 8
for guess in range(abs(cube) + 1):
    if guess**3  >= abs(cube):
        break
if guess**3 != abs(cube):
    print(str(cube) + ' is not a perfect cube')
else:
    if cube < 0 :
        guess = -guess
    print('Cube root of ' + str(cube) + ' is ' +  str(guess))

# Problem Set
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o',
# and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
s= 'asoidfnoawienoiwernf'
vowels = 'aeiou'
counter = 0
for char in s:
    if char in vowels:
        counter +=1
print(f'Number of vowels: {counter}')