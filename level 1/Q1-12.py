'''
note: for few of the problems, I solved them in brute force approach and then searched for optimized approach,
and then solved them in the optimized way.
'''


'''
1.Write a program in Python to perform the following
operation:
If a number is divisible by 3 it should print “SKILLBREW”
as a string
If a number is divisible by 5 it should print “BRUDITE” as a
string
If a number is divisible by both 3 and 5 it should print
“BRUDITE - NIRVANA” as a string.

'''

a = int(input("Enter your number"))

if a%3==0 and a%5==0 :
    print("BRUDITE - NIRVANA")
elif a%3==0 :
    print("SKILLBREW")
elif a%5==0 :
    print("BRUDITE")
else:
    print("The number is not divisible by 3 or 5")

'''
2. Write a program that accepts a string as input from
the user and calculates the number of digits and
letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3

'''
a = str(input("Enter your string: "))
letters = 0
digits = 0
for i in list(a):
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1


print(f"Number of letters: {letters} & Number of digits: {digits}")

'''3. Write a Python program to input marks for five
subjects Physics, Chemistry, Biology, Mathematics,
and Computer. Calculate the percentage and grade
according to the following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% : Grade F
'''

physics = int(input("Enter marks for Physics: "))
chemistry = int(input("Enter marks for Chemistry: "))
biology = int(input("Enter marks for Biology: "))
mathematics = int(input("Enter marks for Mathematics: "))
computer = int(input("Enter marks for Computer: "))

total_marks = physics + chemistry + biology + mathematics + computer
percentage = (total_marks / 500) * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "F"

print(f"your grade is {grade} ")

'''
4. Write a Python program to find the sum of all odd
numbers between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25
'''

start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))
sum=0
for i in range(start, stop + 1):
    if i % 2 != 0:
        sum += i

print(f"Sum of odd numbers between {start} and {stop} is {sum}")

'''
5. Write a Python program to find the factorial of a
number using a for loop
'''
num = int(input("Enter a number"))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")

'''6. Write a Python program to check if a given number
is a perfect number.
A Perfect number is a positive integer that is equal to the
sum of its proper divisors. For instance, 6 has divisors 1, 2,
and 3, and 1 + 2 + 3 = 6, so 6 is a perfect number.
Input: 5
Output: No
'''
num = int(input("Enter a number "))
sum=0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

'''
7. Write a Python program to check if a string is an
anagram of another string.
string1 = "listen", string2 = "silent"
Output: True

'''

def is_anagram(s1, s2):
    
    if len(s1)!=len(s2):
        return False
    c=[0]*26
    k=[0]*26
    s1 = s1.lower()
    s2 = s2.lower()
    for char in s1:
        c[ord(char)-ord('a')]+=1 
    for char in s2:
        k[ord(char)-ord('a')]+=1 
    for i  in range(26):
        if c[i]!=k[i]:
            return False
    return True
s1= str(input("Enter first string: "))
s2= str(input("Enter second string: "))
print(is_anagram(s1, s2))


#optimised approach

def is_anagram1(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(is_anagram1(s1, s2))


'''
8. Write a Python program to calculate the LCM (Least
Common Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36
'''
#brute force approach
def lcm(a, b):
    if a > b:
        greater = a 
    else:
        greater = b
    for i in range(greater, (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i
        
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
result = lcm(number1, number2)
print(f"LCM of {number1} and {number2} is: {result}")

#optimized approach
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm2(a, b):
    return (a * b) // gcd(a, b) 

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
result = lcm2(number1, number2)
print(f"LCM of {number1} and {number2} is: {result}")


'''
9.Write a Python program to count the frequency of
each element in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
'''

def count_frequency(input_list):
    frequency = {}
    for item in input_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency_count = count_frequency(input_list)
print(f"Frequency count: {frequency_count}")

'''
10. Write a Python program to reverse the order of
words in a given sentence.
Input_sentence = “Hello, World! Welcome to Python
programming.”
Output after reverse = “programming. Python to Welcome
World! Hello,

'''
def reverse_words(str):
    words = str.split(' ')
    reverse_str = ' '.join(reversed(words))
    return reverse_str

input_sentence = "Hello, World! Welcome to Python programming."
output_sentence = reverse_words(input_sentence)
print(f"Output after reverse = {output_sentence}")

'''
11. Write a Python program to calculate the sum of
digits of a given number until the sum becomes a
single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced
to
on single digit.
Final Output: 6
'''

def sum_of_digits1(num):
    while num % 10 >= 0:
        num = sum(int(digit) for digit in str(num))
    return num


num = int(input("Enter a number: "))
print(f"sum of digits: {sum_of_digits1(num)}")

'''
12. Write a Python program to reverse a number using
a while loop.
Sample Input: num = 12345
Sample Output: revnum = 54321
'''

def reverse_number(num):
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num=num // 10
    return rev_num

num = int(input("Enter a number: "))
print(f"Reversed number: {reverse_number(num)}")
