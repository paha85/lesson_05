# def num_nums(numer):
#     for num in range(1, numer + 1):
#         if num % 2 != 0:
#             yield num
#     return 'done'
#
# number_15 = num_nums(15)
# while number_15:
#     print(next(number_15))

num_nums = (num for num in range(1, 15 + 1) if num % 2 != 0)

while num_nums:
    print(next(num_nums))
