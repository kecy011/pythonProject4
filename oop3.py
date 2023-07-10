
class MLT:
    max_student = 70
    population = 0
    students = []
    course = "MLT"
    cut_off_mark = 80
    study_years = 5

    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score
        for instance in self.score:
            if self.score >= MLT.cut_off_mark and MLT.population < MLT.max_student:
                MLT.students.append(self)
                MLT.population += 1

    @classmethod
    def add_student(cls):
        if MLT.population < MLT.max_student:
            return True
        return False

    @staticmethod
    def display_students():
        for instance in MLT.students:
            print(instance.name)

    def __repr__(self):
        return f"Course('{self.name}', {self.year}, {self.score})"

    def admission_status(self):
        if self.score >= MLT.cut_off_mark:
            status = "admitted"
        else:
            status = "not admitted"
        return status


class PHARMACY:
    max_student = 60
    population = 0
    students = []
    course = "PHARMACY"
    cut_off_mark = 75
    study_years = 5

    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score
        for instance in self.score:
            if self.score >= PHARMACY.cut_off_mark and PHARMACY.population < PHARMACY.max_student:
                PHARMACY.students.append(self)
                PHARMACY.population += 1

    @classmethod
    def add_student(cls):
        if PHARMACY.population < PHARMACY.max_student:
            return True
        return False

    @staticmethod
    def display_students():
        for instance in PHARMACY.students:
            print(instance.name)

    def __repr__(self):
        return f"Course('{self.name}', {self.year}, {self.score})"

    def admission_status(self):
        if self.score >= PHARMACY.cut_off_mark:
            status = "admitted"
        else:
            status = "not admitted"
        return status


class HIM:
    max_student = 80
    population = 0
    students = []
    course = "HIM"
    cut_off_mark = 55
    study_years = 4

    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score
        for instance in self.score:
            if self.score >= HIM.cut_off_mark and HIM.population < HIM.max_student:
                HIM.students.append(self)
                HIM.population += 1

    @staticmethod
    def display_students():
        for instance in HIM.students:
            print(instance.name)

    def __repr__(self):
        return f"Course('{self.name}', {self.year}, {self.score})"

    def admission_status(self):
        if self.score >= HIM.cut_off_mark:
            status = "admitted"
        else:
            status = "not admitted"
        return status


class CHEW:
    max_student = 40
    population = 0
    students = []
    course = "CHEW"
    cut_off_mark = 60
    study_years = 4

    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score
        for instance in self.score:
            if self.score >= CHEW.cut_off_mark and CHEW.population < CHEW.max_student:
                CHEW.students.append(self)
                CHEW.population += 1

    @classmethod
    def add_student(cls):
        if CHEW.population < CHEW.max_student:
            return True
        return False

    @staticmethod
    def display_students():
        for instance in CHEW.students:
            print(instance.name)

    def __repr__(self):
        return f"Course('{self.name}', {self.year}, {self.score})"

    def admission_status(self):
        if self.score >= CHEW.cut_off_mark:
            status = "admitted"
        else:
            status = "not admitted"
        return status


class JCHEW:
    max_student = 45
    population = 0
    students = []
    course = "JCHEW"
    cut_off_mark = 50
    study_years = 2

    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score
        for instance in self.score:
            if self.score >= JCHEW.cut_off_mark and JCHEW.population < JCHEW.max_student:
                JCHEW.students.append(self)
                JCHEW.population += 1

    @classmethod
    def add_student(cls):
        if JCHEW.population < JCHEW.max_student:
            return True
        return False

    @staticmethod
    def display_students():
        for instance in JCHEW.students:
            print(instance.name)

    def __repr__(self):
        return f"Course('{self.name}', {self.year}, {self.score})"

    def admission_status(self):
        if self.score >= JCHEW.cut_off_mark:
            status = "admitted"
        else:
            status = "not admitted"
        return status


class EHT:
    max_student = 100
    population = 0
    students = []
    course = "EHT"
    cut_off_mark = 45
    study_years = 4

    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score
        for instance in self.score:
            if self.score >= EHT.cut_off_mark and EHT.population < EHT.max_student:
                EHT.students.append(self)
                EHT.population += 1

    @classmethod
    def add_student(cls):
        if EHT.population < EHT.max_student:
            return True
        return False

    @staticmethod
    def display_students():
        for instance in EHT.students:
            print(instance.name)

    def __repr__(self):
        return f"Course('{self.name}', {self.year}, {self.score})"

    def admission_status(self):
        if self.score >= EHT.cut_off_mark:
            status = "admitted"
        else:
            status = "not admitted"
        return status


class COMP:
    max_student = 50
    population = 0
    students = []
    course = "JCHEW"
    cut_off_mark = 60
    study_years = 4

    def __init__(self, name, year, score):
        self.name = name
        self.year = year
        self.score = score
        for instance in self.score:
            if self.score >= COMP.cut_off_mark and COMP.population < JCHEW.max_student:
                COMP.students.append(self)
                COMP.population += 1

    @classmethod
    def add_student(cls):
        if COMP.population < COMP.max_student:
            return True
        return False

    @staticmethod
    def display_students():
        for instance in COMP.students:
            print(instance.name)

    def __repr__(self):
        return f"Course('{self.name}', {self.year}, {self.score})"

    def admission_status(self):
        if self.score >= COMP.cut_off_mark:
            status = "admitted"
        else:
            status = "not admitted"
        return status

