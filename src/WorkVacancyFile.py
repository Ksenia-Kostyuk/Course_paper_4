from abc import ABC, abstractmethod
import json


class AbctrWorkVacancy(ABC):
    """
    Реализует методы добавления вакансий в файл,
    выводит данные и удаляет их
    """

    @abstractmethod
    def add_vacancy(self, value):
        """
        Добавляет список интересующих вакансий в файл
        :param value: (list) список вакансий с hh.ru
        :return: None
        """
        pass

    @abstractmethod
    def out_data_vacancy(self, value):
        """
         Выводит список интересующих профессий
        :param value: (list) список данных
        :return: list_data (list) содержимое файла
        """
        pass

    def del_vacancy(self):
        """
        Очищает файл по окончании работы с ним
        :return: None
        """
        pass


class WorkVacancy(AbctrWorkVacancy):

    def add_vacancy(self, list_vacation: list):
        with open("hh_vacancy.json", "w", encoding='utf-8') as file:
            json.dump(list_vacation, file)

    def out_data_vacancy(self, list_vacation):
        with open("hh_vacancy.json", "w", encoding='utf-8') as file:
            file_json = json.load(file)
            return file_json

    def del_vacancy(self):
        with open("hh_vacancy.json", "w", encoding='utf-8') as file:
            file.truncate()

    def __len__(self, list_class, other):
        """
        Возвращает топ вакансий, выбранных пользователем
        :param list_class: список вакансий
        :param other: число вакансий
        :return: list_class (list) срез листа вакансий
        """
        return list_class[:other]

    @staticmethod
    def sorted_vacancy(list_class: list, param: list):
        """
        Сортирует список объектов по параметрами полученным от пользователя
        :param list_class: (list) список объектов c hh.ru
        :param param: (list) список параметров
        :return: vacancy_list (list) список отсортированных профессий
        """
        vacancy_list = []
        for i in list_class:
            if lambda: param in list_class:
                vacancy_list.append(i)
            else:
                continue
        return vacancy_list

    def salary_sum(self, list_vacancy, salary_range):
        """
        Сортирует список вакансий по указанной пользователем заработной плате,
        если пользователь не указал заработную плату, то вакансия с зарплатой с типом данных None не добавляется в список рекоментуедмых
        :param list_vacancy: (list) список вакансий с hh.ru
        :param salary_range: (list) диапазон зарплат
        :return: new_list_vacancy (list) отсортированный список вакансий
        """
        new_list_vacancy = []
        for i in list_vacancy:
            if lambda: salary_range in list_vacancy:
                new_list_vacancy.append(i)
            elif i['salary'] == None:
                continue
            else:
                new_list_vacancy.append(i)