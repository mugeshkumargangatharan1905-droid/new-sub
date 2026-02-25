class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("\nName:", self.name)
        print("Roll No:", self.roll)
        print("Marks:", self.marks)

    def average(self):
        return sum(self.marks) / len(self.marks)


students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        roll = int(input("Enter roll number: "))
        marks = list(map(int, input("Enter marks (space separated): ").split()))
        students.append(Student(name, roll, marks))

    elif choice == 2:
        for s in students:
            s.display()
            print("Average:", s.average())

    elif choice == 3:
        break
