from abc import ABC, abstractmethod
import requests


class AbctrGetData(ABC):
    """Определяет будущий функционал классов"""

    @abstractmethod
    def connection_api(self):
        """Подключается к API"""
        pass

    @abstractmethod
    def getting_vacations(self):
        """Получение вакансий с удаленного сервера"""
        pass


class GetData(AbctrGetData):
    """Подключается к серверу поиска вакансий"""

    def connection_api(self):
        """
        Осуществляет подключение к сервису
        :return:(int) статус подключения
        """
        response = requests.get("https://api.hh.ru/vacancies")
        return response.status_code

    def getting_vacations(self, param: str):
        """
        Возвращает вакансии с удаленного сервиса
        если параметр не передан, осуществляет посик по умолчанию
        :param param: (str) Параметр поиска вакансий
        :return: (str) файл json
        """
        if param:
            response = requests.get("https://api.hh.ru/vacancies", params = {"text": param})
            return response.json().get("items")
        else:
            response = requests.get("https://api.hh.ru/vacancies")
            return response.json().get("items")
