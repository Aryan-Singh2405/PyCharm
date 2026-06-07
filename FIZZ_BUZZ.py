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


# numbers = [5, 51, 2, 15, 6]

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



# items = [('item_1',20),
#          ('item_2',40),
#          ('item_3',70),
#          ('item_4',35),
#          ('item_5',25),
#          ('item_6',12),
#          ('item_7',10),
#          ('item_8',24),
#          ('item_9',69),
#          ('item_10',5)]
# print(items)
#
# def sort_items_by_price(index):
#     return index[1]
# items.sort(key=sort_items_by_price)
# print(items)



# def f_to_c(temp):
#     return (9/5)*temp + 32
#
# temp_in_F = [0,10,20,30,40,50,60,70,80,90,100]
# temp_in_C = map(f_to_c, temp_in_F)
# temp_in_C = list(map(f_to_c, temp_in_F))
# print(temp_in_C)
#
# temp_in_F = [0,10,20,30,40,50,60,70,80,90,100]
# temp_in_c = list(map(lambda temp :(9/5)*temp + 32, temp_in_F))
# print(temp_in_c)


# grades = [15,70,34,40,56,21,86,85,99,100,22,32,55,67,89,13,67,77,88]
# pass_or_not = list(filter(lambda grade:grade >=32,grades))
# print(pass_or_not, len(pass_or_not))

# product = [("jersey",6000),
#            ("shin pads",1200),
#            ("cleats",37000),("football",7000),
#            ("tape",300),
#            ("grip socks",800)]
# product.sort(key = lambda index : index[1])
# filtered_price= list(filter(lambda index: index[1] < 1000,product))
# print(product)
# print(filtered_price)


# fruits= ["apple","mango","papaya","banana","kiwi","strawberry",]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# products = [
#     ("Product1", 15),
#     ("Product2", 50),
#     ("Product3", 5)
# ]
# prices = [price[1] for price in products]
# print(prices)
#
# by_mapping = list(map(lambda price : price[1], products))
# print(by_mapping)

# list_1 = [1, 2, 3, 4]
# list_2 = [10, 20, 30, 40, 50, 60]
#
# combined_list = list(zip(list_1, list_2))
# print(combined_list)

# fruits = ["apple","mango","banana"]
# print(help(fruits))
#
# from array import array
#
# numbers = array("i", [1, 2, 3])
# f


# def read_file(file_path):
#     with open(file_path) as file:
#         for line in file:
#             yield line.strip()
# file_path = "C:\\Users\\Aryan\\OneDrive\\Desktop\\test.txt"
# for line in read_file(file_path):
#     print(line)
#
# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers)
# print(*numbers)
#
# values = [*range(10)]
# print(values)

# myname = [*"hello world"]
# print(myname)

for num in range(2, 20):
    if num == 10:
        continue  # Skip table of 10

    for i in range(1, 11):
        print(num * i, end=" ")
    print()  # Move to next line after each table