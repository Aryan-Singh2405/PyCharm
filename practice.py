# QUESTION 1
# def product(a, b):
#     return a * b
#
#
# def sum(a, b):
#     return a + b
#
#
# a = int(input("Type the value of A: "))
# b = int(input("Type the value of B: "))
# if a * b <= 1000:
#     print("Product of A & B : ",product(a, b))
# else:
#     print("sum of A & B : ",sum(a, b))
# from calendar import error
#
# QUESTION 2:
# print("Printing current and previous number sum in a range(10)")
#
# def operation():
#     for value in range(0, 10):
#         previous_value = value - 1
#         current_value = value
#         if previous_value == -1:
#             previous_value = 0
#         else:
#             result = current_value + previous_value
#             print(f"current value : {current_value}, previous value : {previous_value}, result : {result}")
# operation()
#
#
# question 3:
#
# random_text = "pynative"
# print("original text:",random_text)
# print("printing only even index chars")
# for i in range(len(random_text)):
#     if i % 2 ==0:
#         print(random_text[i])
#
#
# Question 4:
#
# text = str("pynative")
# print(text)
# n = int(input("type the index:"))
# print(text[n:])
#
# question 5:
#
# a = 5
# b = 10
# print(f"before swap: a = {a}, b = {b}")
# a = b
# b = a
# print(f"after swap: a = {a}, b = {b}")
#
# # question 6:
# number = int(5)
# factorial = 1
# for i in range(number):
#     factorial *= i+1
# print(factorial)
#
# question 7:
# list_one = ["apple","banana","cherry","date","elderberry"]
# list_one.pop(1)
# list_one.insert(4,"fig")
# print(list_one)
#
# question 8:
# name = str("Python")
# print(f"orignal text: {name}")
# for i in range(len(name)):
#     print(i,name[i] )
# print("reverse order of text:",name[::-1])
#
# question 9:
# sentence = str("Learning python is fun")
# vowels = "aeiou"
# count = 0
# for char in sentence.lower():
#     if char in vowels:
#         count += 1
#     else:
#         continue
# print(f"Number of vowels: {count}")
#
# question 10:
# nums = [45, 2, 89, 12, 7]
# nums.sort(reverse = False)
# print(f"the sorted order : {nums}")
# print(f"Smallest number:{nums[0]}")
# print(f"largest number:{nums[-1]}")
#
# question 11
# data = [1, 2, 2, 3, 4, 4, 4, 5]
# data.sort()
# print(f"the sorted order is : {data}")
# unique_data = list(set(data))
# print(f"the unique data is : {unique_data}")
#
# question 12:
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
#
# def matchx (numbers_x):
#     first_digit = numbers_x[0]
#     last_digit = numbers_x[-1]
#     if first_digit == last_digit:
#         return True
#     else:
#         return False
# def matchy (numbers_y):
#     first_digit = numbers_y[0]
#     last_digit = numbers_y[-1]
#     if first_digit == last_digit:
#         return True
#     else:
#         return False
# print(matchx(numbers_x))
# print(matchy(numbers_y))
#
# question 13:
# num_list = [10, 20, 33, 46, 55]
# for num in num_list:
#     if num % 5 == 0:
#         print(num)
#     else:
#         continue
#
#
# question 14:
# str_x = "Emma is good developer. Emma is a writer, Emma is a boy, and Emma is an artist."
# count = str_x.lower().count('emma')
# print(f"Emma appeard {count} times.")
#
# question 15:
# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print('\n')
#
# # or
# for i in range(1,10):
#     print((str(i)+"")*i)
#
# question 16:
# num1 = str(141)
# num2 = str(123)
# def main (num):
#     first_char = num[0]
#     last_char = num[-1]
#     if first_char == last_char:
#         print(f"{num} is a palindrome")
#     else:
#         print(f"{num} is not a palindrome")
# main(str(123))
#
# def palindrome(text):
#     for i in range(0,len(text)):
#         if text[i] == text[-i-1]:
#             print(f"{text} is a palindrome")
#             return
#         else:
#             if text[i] != text[-i-1]:
#                 print(f"{text} is a not a palindrome")
#                 return
# print(f"type the number or text to check for palindrome:")
# text = input()
# palindrome(str(text))
#
# questioin 17:
#
# def parity_filter(list1,list2,list_expected):
#     for num in list1:
#         if num %2 != 0:
#             list_expected.append(num)
#
#     for num in list2:
#         if num %2 == 0:
#             list_expected.append(num)
#
# list_expected =[]
# parity_filter([10,20,25,30,35],[40,45,60,75,90],list_expected)
# print(list_expected)
#
# question 18:
# num = int(123456789)
#
# while num > 0:
#     digit = num % 10
#     print(digit, end="")
#     num = num // 10
#
# QUESTION 19:
# income = int(input("enter your income in $ :"))
# tax = 0
# if income <= 10000:
#     print('you do not come under tax bracket')
#
# elif income <= 20000:
#     tax = (income - 10000) * 0.10
#     print(f"applied text will be 10% for 10k< income < 20k: {tax}")
# else:
#     tax = (10000 * 0.10) + ((income-20000) * 0.20)
#     print(f"applied text will be 20% for income > 20k : {tax}")
#
# question 20:
#
# for i in range(1, 11):
#     print(i, end="\t")
# print('\n')
# for i in range(1,21):
#     print(i)
#     for j in range(1,11):
#         print(i*j, end="\t")
#     print("\n")
#
# question 21:
#
# for i in range (5,0,-1):
#     print("* "* i)
#
#
# question 22:
# def exponent(base,exp):
#     return base**exp
# exponent(2,3)
# print(exponent(2,3))
#
# # question 23:
# num = str(11111113)
# for i in range (len(num)):
#     if num[i] == num[i-1]:
#         print(f"{num} is a palindrome ")
#         break
#     else:
#         print(f"{num} is not a palindrome ")
#         break
#
# question 24:
# def fib(n):
#     a, b = 0 ,1
#     if n == 0:
#         print(a)
#     else:
#         print(a,b, end=' ')
#
#         for i in range (1,n):
#             c = a + b
#             a = b
#             b = c
#             print(c,end=" ")
# fib(15)
#
# question 25:
# year = 2034
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")
#
# question 26:
# dict1 = {'name':"alice", 'age':"25"}
# dict2 = {'city':"New York", 'job':"engineer"}
# combine = dict1 | dict2
# print(combine)
#
# question 27:
#
# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# list1 = set(list1)
# list2 = set(list2)
# list3 = set(list1 | list2)
# print(list3)
# print(list1 & list2)
#
# Question 28:
# numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
# even = []
# odd = []
# for number in numbers:
#     if number%2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
# print(f"Even numbers:{even} Odd numbers: {odd}")
#
# question 29:
# words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# # print(len(words[3]))
# for i in range(len(words)):
#     print(f"{words[i]}-{len(words[i])}", end=" ")
#
# Question 30:
# text = "apple banana apple cherry banana apple"
# words = text.split()
# print(text)
# frequency = {}
# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
# print(frequency)
#
# Question 31:
# Function to check prime number
# def is_prime(n):
#
#     if n < 2:
#         return False
#
#     for i in range(2, n):
#
#         if n % i == 0:
#             return False
#
#     return True
#
#
# Function to get alternate prime numbers
# def alternate_primes(limit):
#
#     primes = []
#
#     # Find all prime numbers
#     for num in range(2, limit + 1):
#
#         if is_prime(num):
#             primes.append(num)
#
#     # Return every second prime
#     return primes[1::2]
#
#
# # Function call
# result = alternate_primes(20)
#
# print(result)
#
# mislanious
#
# numbers_0_19 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#                 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(numbers_0_19)
# first, *others, last = numbers_0_19
# print(first)
# print(others)
# print(last)
# letters = ["a", "b", "c", "d"]
#
# for letter in letters:
#     print(letter)
# for letter in enumerate(letters):
#         print(letter)
# for index, letter in enumerate(letters):
#     print(index, letter)
# numbers = [5, 51, 2, 15, 6]
# numbers.sort(reverse= True)
# print(numbers)               # this is a orignal list
# print(sorted(numbers))       # this will create a new list from the original list
# print(sorted(numbers, reverse = True))

# complex_num = [("xbox_x", 75000), ("xbox_s", 65000), ("PS5_pro", 95000), ("PS5_slim", 50000)]
#
#
# def get_price(complex_num):
#     return complex_num[1]
#
#
# complex_num.sort(key=get_price, reverse=True)
# print(complex_num)
#
# price = []
# for value in complex_num:
#     price.append(value[1])
# print(price)

