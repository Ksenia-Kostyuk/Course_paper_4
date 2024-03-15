class Vacancy:
    """"""

    def __init__(self, name, city, requirements, salary_min, salary_max, link):
        self.name = name
        self.city = city
        self.requirements = requirements

        if salary_min:
            self.salary_min = salary_min
        else:
            self.salary_min = 0

        if salary_max:
            self.salary_max = salary_max
        else:
            self.salary_max = 0

        self.link = link

