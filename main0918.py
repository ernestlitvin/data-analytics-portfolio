# class - main word for creating a class
class DataReport:
    # __init__ - constructor, which initialize new object
    def __init__(self, title, author, data_list):
        self.title = title          # name of report
        self.author = author        # author of report
        self.data = data_list       # data list
        self.record_count = len(data_list) # quantity of records

    # display_info - it is a method, i.e. function inside a class
    def display_info(self):
        """Shows basic information about report"""
        print("--- Report's information ---")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Record's quantity: {self.record_count}")

    def calculate_mean(self):
        """Mean's method """
        if self.record_count > 0:
            return sum(self.data) / self.record_count
        else:
            return 0

# Our data
sales_data = [120, 150, 135, 200, 180, 210]
user_activity_data = [25, 30, 22, 45, 33]

# Creating first object in DataReport class
sales_report = DataReport(title="Sales report", author="John", data_list=sales_data)

# Creating second object
user_report = DataReport(title="Users activity", author="Jane", data_list=user_activity_data)

# Calling method for first report
sales_report.display_info()
mean_sales = sales_report.calculate_mean()
print(f"Mean sales: {mean_sales:.2f}\n") # .2f - round until 2 digits after ,

# Calling the same method for second report
user_report.display_info()
mean_activity = user_report.calculate_mean()
print(f"Mean acitivity: {mean_activity:.2f}")

