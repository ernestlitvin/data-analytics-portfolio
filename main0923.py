# class Solution:
#     def __init__(self, api):
#         self.api = api
#         print("A new challenge is ready!")
#
#     def get_total_sum(self):
#         numbers = self.api.get_prices()
#         return sum(numbers)



class Solution:
    def __init__(self, api):
        self.api = api
        print("Challenge: Find the top student!")

    def find_top_student(self):
        students = self.api.get_students()
        highest_score = 0
        student_name = ""
        for student in students:
            if student["score"] > highest_score:
                highest_score = student["score"]
                student_name = student["name"]
        return student_name

class MockApi:
    def get_students(self):
        students_data = [
            {'name': 'Alice', 'score': 88},
            {'name': 'Bob', 'score': 95},
            {'name': 'Charlie', 'score': 92},
            {'name': 'Diana', 'score': 92},
            {'name': 'Evan', 'score': 76}
        ]
        print(f"Mock API: Returns the list of {len(students_data)} students.")
        return students_data

if __name__ == '__main__':
    mock_api = MockApi()

    solution = Solution(mock_api)

    top_student = solution.find_top_student()
    print(f"Top student: {top_student}")
