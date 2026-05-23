# """def multiply(*nums):
#     total = 1
#     for num in nums:
#         total *= num
#     return total
# print("START")
# print(multiply(1,2,3,4))"""


# def fizz_buzz(input):
#     if input % 3 == 0 and input % 5 == 0:
#         print("FizzBuzz")
#         return
#
#     if input % 3 == 0:
#         print("FIZZ")
#     elif input % 5 == 0:
#         print("BUZZ")
#     else:
#         print(input)
#
#
# fizz_buzz(15)


# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("Echo", command)

# numb = 0
# for i in range(1,10):
#     if i%2 ==0:
#         print(i)
#         numb += 1
#     else:
#         continue
# print(f"we have {numb} even numbers")


# def dic(**user):
#     print(user)
#
#
# dic(name="Aryan Singh", uid="22BAI70751", age=21)


# string_list = list("Python")
# print(string_list)
#
# # Check the number os item in a list
# item_in_string_list = len(string_list)
# print(item_in_string_list)


# numbers = list(range(20))
# # print(numbers)

# # Like string this is o slice a list [first item : last item: step] all argumente are optinal
# numbers_slice = numbers[2:15:2]
# print(numbers_slice)
#
# # with this we are able to reverse the order of the list
# numbers_revers = numbers[::-1]
# print(numbers_revers)


# numbers_0_19 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#                 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# print(numbers_0_19)
# first, second, *others = numbers_0_19
# print(first)
# print(second)
# print(others)
#
# # For example if we want the unpack the first and the the last item
# first, *others, last = numbers_0_19
# print(first)
# print(others)
# print(last)


# letters = ["a", "b", "c", "d"]
#
# for i in letters:
#     print(i)


# letters = ['a','b','c','d','e','f']
# letters.pop(3)
# print(letters)
# for index, letter in enumerate(letters):
#     print(index, letter)
# letters.append('h')
# print(letters)
# letters.insert(2,'---------')
# print(letters)

#
# li = ["a","b","b","b","c","c","d","e","f","g",]
#
# for i in li:
#     if i == "b":
#         li.remove("b")
#     elif i == "c":
#         li.remove("c")
# print(li)


numbers = [5, 51, 2, 15, 6]

# # sort numbers in use the sort() method
# numbers.sort()
# # print(numbers)
#
# numbers.sort(reverse=True)
# # print(numbers)
# numbers.reverse()
# # print(numbers)

# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
