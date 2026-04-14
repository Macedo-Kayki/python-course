class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = float(grade)

    def get_dict(self):
        data = {
            "name": self.name,
            "grade": self.grade
        }

        return data
    
    def __repr__(self):
        return f"Nome: {self.nome}\nIdade: {self.grade}"