# decorator_v1
# def decorator(some_function):
#     print("This decorator works correctly!")
#
#     def wrapper(*args, **kwargs):
#         return some_function(*args, **kwargs)
#     return wrapper
#
#
# @decorator
# def multiple_two(some_number):
#     return some_number * 2
#
#
# def add_seven(some_number):
#     return some_number + 7
#
#
# print("Result of adding: ", add_seven(7))
# print("Result of multiplication: ", multiple_two(33))

# ------------------------------------------

# decorator_v2
# learning = {'course': 'python', 'number of lessons': '32 lessons', 'mentor': 'Igor'}
#
#
# def route(key):
#     """
#     Implement simple routing
#     :param key:
#     :return:
#     """
#     def decorator(some_function):
#         learning[key] = some_function
#
#         def wrapper(*args, **kwargs):
#             return some_function(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @route('duration')
# def add_new_pair():
#     learning['duration'] = '2 hours'
#     print("Decorator works!")
#
#
# print(learning['duration']())
# print(learning)

# ------------------------------------------

# decorator_v3
# numbers = {"One": 1, "Two": 2, "Three": 3}
#
#
# def route(value):
#     def decorator(some_function):
#         numbers[value] = some_function
#
#         def wrapper(*args, **kwargs):
#             return some_function(*args, **kwargs)
#         return wrapper
#     return decorator
#
#
# @route('One')
# def changing_value():
#     numbers["One"] = 15
#     print("Decorator works!")
#     return numbers
#
#
# changing_value()
# print(numbers['Two'])
# print(numbers)

# ------------------------------------------
# ------------------------------------------
