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
        response = requests.get("https://api.hh.ru/vacancies")
        return response.status_code

    def getting_vacations(self):
        response = requests.get("https://api.hh.ru/vacancies")
        return response.json().get("items")

