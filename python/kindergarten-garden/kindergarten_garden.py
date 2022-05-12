student_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid",
                "Larry"]

plant_list = {"R": "Radishes", "C": "Clover", "V": "Violets", "G": "Grass"}


class Garden:

    def __init__(self, diagram, students=student_list):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student) * 2
        plants = []
        for row in self.diagram:
            for letter in row[index:index+2]:
                plants.append(plant_list[letter])
        return plants
