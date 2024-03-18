from src.get_data.GetData import GetData
from src.WorkVacancyFile import WorkVacancy
from src.Vacancy import Vacancy


def hello_user() -> None:
    print('Здравствуйте, добро пожаловать на hh.ru!')
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ").split()

    hh_api = GetData()
    sort_vac = hh_api.getting_vacations(search_query)
    hh_vacancy = WorkVacancy()

    filter_salary = hh_vacancy.salary_sum(sort_vac)
    filter_vacancy = hh_vacancy.sorted_vacancy(filter_salary, filter_words)
    hh_vacancy.add_vacancy(filter_vacancy)

    selected_vacancies = hh_vacancy.__len__(filter_vacancy, top_n)

    info = Vacancy.new_obj_cls(selected_vacancies)
    print(info.__repr__())
    if True:
        end_job = input('Хотите удалить историю поиска? Y/n?')
        if end_job == 'Y' or 'y':
            hh_vacancy.del_vacancy()
            break
        elif end_job == 'n' or 'N':
            pass


if __name__ == '__main__':
    hello_user()
