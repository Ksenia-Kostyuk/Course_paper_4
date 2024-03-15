from abc import ABC, abstractmethod


class AbctrWorkVacancy(ABC):
    """Реализует методы добавления вакансий в файл, выводит данные и удаляет их"""
    @abstractmethod
    def add_vacancy(self):
        """Добавляет вакансию в файл"""
        pass

    @abstractmethod
    def out_data_vacancy(self):
        """Выводит информацию о вакансиях по указанным критериям"""
        pass

    def del_vacancy(self):
        """Удаляет вакансию из файла"""
        pass


class WorkVacancy(AbctrWorkVacancy):

    def add_vacancy(self):
        pass

    def sorted_vacancy(self, list_class: list, param: list):
        """
        Сортирует список объектов по параметрами полученным от пользователя
        :param list_class: (list) список объектов c hh.ru
        :param param: (list) список параметров
        :return:
        """
        vacancy_list = []
        for i in list_class:
            if lambda: param in list_class:
                vacancy_list.append(i)
        return vacancy_list

    def out_data_vacancy(self, value):
        pass

    def del_vacancy(self):
        pass
