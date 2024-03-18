class Vacancy:

    def __init__(self, name, city, requirements, salary_min, salary_max, currency, url):
        self.name = name
        self.city = city
        self.requirements = requirements
        self.url = url
        self.currency = currency

        if salary_min:
            self.salary_min = salary_min
        else:
            self.salary_min = 0

        if salary_max:
            self.salary_max = salary_max
        else:
            self.salary_max = 0

    def __repr__(self):
        """
        Магический метод, возвращающий информацию в понятном для пользоавателя виде
        :return:
        """
        return f'''{self.name} - город: {self.city}.
        Заработная плата: {self.salary_min} - {self.salary_max} {self.currency}.
        Требования: {self.requirements}
        Сссфлка: {self.url}'''

    def __eq__(self, other: object) -> bool:
        """
        Магический метод который проверяет
        равны ли два объекта

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_min == other.salary_min

    def __lt__(self, other):
        """
        Магический метод который проверяет
        какой из объектов больше

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_min < other.salary_min

    def __gt__(self, other):
        """
        Магический метод который проверяет
        какой из объектов меньше

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_min > other.salary_min

    def salary_sum(self, list_vacancy, salary_range):
        new_list_vacancy = []
        for i in list_vacancy:
            if lambda: salary_range in list_vacancy:
                new_list_vacancy.append(i)
            elif i['salary'] == None:
                continue
            else:
                new_list_vacancy.append(i)


    @classmethod
    def new_obj_cls(cls, vacancies: list[dict, ...]):
        """
        Создает объект по полученным данным о вакансиях с hh.ru
        :param vacancies: (list[dict, ...] входные данные
        :return: (list[object, ...] список объектов
        """
        vacancies_list = []
        try:
            for i in vacancies:
                if i.get('salary'):
                    vacancies_list.append(cls(name=i.get('name'),
                                            city=i.get('area').get('name'),
                                            requirements=i.get('snippet').get('requirement'),
                                            salary_max= i.get('salary').get('to'),
                                            salary_min=i.get('salary').get('from'),
                                            currency=i.get('salary').get('currency'),
                                            url=i.get('alternate_url')
                                            ))
                else:
                    vacancies_list.append(cls(name=i.get('name'),
                                      city=i.get('area').get('name'),
                                      requirements=i.get('snippet').get('requirement'),
                                      salary_max=0,
                                      salary_min=0,
                                      currency=None,
                                      url=i.get('alternate_url')
                                      ))
        except TypeError:
            pass

            return vacancies_list

