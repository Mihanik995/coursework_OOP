class Vacancy:

    def __init__(self, vacancy: dict):
        self.json = vacancy
        if type(vacancy['id']) is int:
            self.name = vacancy['profession']
            self.salary_from = vacancy['payment_from']
            self.salary_to = vacancy['payment_to']
        else:
            self.name = vacancy['name']
            self.salary_from = 0 if vacancy['salary'] is None else int(vacancy['salary']['from'] or 0)
            self.salary_to = 0 if vacancy['salary'] is None else int(vacancy['salary']['to'] or 0)

    def __str__(self):
        result = self.name
        match self.salary_from == 0, self.salary_to == 0:
            case True, True:
                result += "\nЗарплата не указана"
            case True, False:
                result += f"\nЗарплата до {self.salary_to} руб."
            case False, True:
                result += f"\nЗарплата от {self.salary_from} руб."
            case False, False:
                result += f"\nЗарплата от {self.salary_from} до {self.salary_to} руб."
        return result
