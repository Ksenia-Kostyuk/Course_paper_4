from src.get_data.GetData import GetData
from src.WorkVacancyFile import WorkVacancy

def hello_user() -> None:
    print('Здравствуйте, добро пожаловать на hh.ru!')
    search_query = input("Введите поисковый запрос: ")
    #top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    #salary_range = input("Введите диапазон зарплат: ")

    hh_api = GetData()
    op = WorkVacancy()
    print(op.sorted_vacancy(hh_api.getting_vacations(search_query), filter_words))

if __name__ == '__main__':
    hello_user()