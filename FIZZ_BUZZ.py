# """def multiply(*nums):
#     total = 1
#     for num in nums:
#         total *= num
#     return total
# print("START")
# print(multiply(1,2,3,4))"""


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print("FizzBuzz")
        return

    if input % 3 == 0:
        print("FIZZ")
    elif input % 5 == 0:
        print("BUZZ")
    else:
        print(input)


fizz_buzz(15)
