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


# question 3:

# random_text = "pynative"
# print("original text:",random_text)
# print("printing only even index chars")
# for i in range(len(random_text)):
#     if i % 2 ==0:
#         print(random_text[i])


# Question 4:

# text = str("pynative")
# print(text)
# n = int(input("type the index:"))
# print(text[n:])

# question 5:

# a = 5
# b = 10
# print(f"before swap: a = {a}, b = {b}")
# a = b
# b = a
# print(f"after swap: a = {a}, b = {b}")

# # question 6:
# number = int(5)
# factorial = 1
# for i in range(number):
#     factorial *= i+1
# print(factorial)

# question 7:
# list_one = ["apple","banana","cherry","date","elderberry"]
# list_one.pop(1)
# list_one.insert(4,"fig")
# print(list_one)

# question 8:
# name = str("Python")
# print(f"orignal text: {name}")
# for i in range(len(name)):
#     print(i,name[i] )
# print("reverse order of text:",name[::-1])

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

# question 10:
# nums = [45, 2, 89, 12, 7]
# nums.sort(reverse = False)
# print(f"the sorted order : {nums}")
# print(f"Smallest number:{nums[0]}")
# print(f"largest number:{nums[-1]}")

# question 11
# data = [1, 2, 2, 3, 4, 4, 4, 5]
# data.sort()
# print(f"the sorted order is : {data}")
# unique_data = list(set(data))
# print(f"the unique data is : {unique_data}")



