class School:
    def __init__(self):
        self.grades = {}

    def add_student(self, name, grade):
        if grade not in self.grades:
            self.grades[grade] = []
            self.grades[grade].append(name)
        else:
            self.grades[grade].append(name)

    def roster(self):
        result = []
        for grade in sorted(self.grades):
            result = result + self.grade(grade)

        return result

    def grade(self, grade_number):
        if grade_number in self.grades:
            return (sorted(self.grades[grade_number]))
        else:
            return []
