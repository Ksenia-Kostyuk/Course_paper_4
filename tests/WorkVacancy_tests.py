import pytest
from src.WorkVacancyFile import WorkVacancy


def test_sorted_vacancy():
    assert WorkVacancy.__len__([1, 2, 3], [1, 2, 3], 2) == [1, 2]
    assert WorkVacancy.__len__([1, 2, 3], [1, 2, 3], 1) == [1]

def test_sorted_vacancy():
    assert WorkVacancy.sorted_vacancy([1, 2, 3, 4, 5], [1, 2]) == [1, 2, 3, 4, 5]
    assert WorkVacancy.sorted_vacancy([1, 2, 3, 4, 5], [6, 7]) == [1, 2, 3, 4, 5]

def test_salary_sum():
    assert WorkVacancy.sorted_vacancy([{'salary': 1}, {'salary': 2}, {'salary': None}], 1) == [{'salary': 1}]
