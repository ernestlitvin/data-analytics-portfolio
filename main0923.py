# # class Solution:
# #     def __init__(self, api):
# #         self.api = api
# #         print("A new challenge is ready!")
# #
# #     def get_total_sum(self):
# #         numbers = self.api.get_prices()
# #         return sum(numbers)
#
#
#
# class Solution:
#     def __init__(self, api):
#         self.api = api
#         print("Challenge: Find the top student!")
#
#     def find_top_student(self):
#         students = self.api.get_students()
#         highest_score = 0
#         student_name = ""
#         for student in students:
#             if student["score"] > highest_score:
#                 highest_score = student["score"]
#                 student_name = student["name"]
#         return student_name
#
# class MockApi:
#     def get_students(self):
#         students_data = [
#             {'name': 'Alice', 'score': 88},
#             {'name': 'Bob', 'score': 95},
#             {'name': 'Charlie', 'score': 92},
#             {'name': 'Diana', 'score': 92},
#             {'name': 'Evan', 'score': 76}
#         ]
#         print(f"Mock API: Returns the list of {len(students_data)} students.")
#         return students_data
#
# if __name__ == '__main__':
#     mock_api = MockApi()
#
#     solution = Solution(mock_api)
#
#     top_student = solution.find_top_student()
#     print(f"Top student: {top_student}")
#
#
# class Solution:
#     def __init__(self, api):
#         self.api = api
#         print("RUN")
#
#     def popular_sze(self):
#         size = self.api.get_size()
#         return size

def remove_chars(str_in):
    chars = ["@", "*", "%"]
    if str_in in chars:
        return True
    else:
        return False

sentence = "#Discount=50% flat"
k = filter(remove_chars, list(sentence))
for j in k:
    print(j, end="")

print(~~~~5 + ~~~~4)


def func(arg, *args, **kwargs):
    print(type(arg), type(args), type(kwargs))
func(33,34,name="sam")


py_list = ["hi", "jack"]
print(list(map(list, py_list)))


principle = 300
_yield = 15
time = 3

print("Interest = {}".format(principle * _yield * time / 100))


def print_this(args, *box):
    print(args + 1)
    for item in box:
        print(item)
    return
print_this (25,30,35)

a = 30
b = 15
g = 2
b <<= g
print(b)

print("--")

from collections import deque
q=deque([6,1,2,5,4])
q.pop()
q.popleft()
q.insert(1,2)
q.insert(1,2)
print(q[0])
print("----")
l1 = [37,88,43,89]
l2 = [37,43,89,88]

if l1==l2:
    print("l1 equal to l2")
elif l1>l2:
    print("l1 greater than l2")
else:
    print("l2 is greater than l1")

print("----")
from typing import Union
name = "Bob"
print(isinstance(name, Union[str,float, bytes]))
print(isinstance(name, str | float | bytes))

tuple