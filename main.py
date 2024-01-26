import os.path

from src.API_services import HeadHunterAPI
from src.API_services import SuperJobAPI
from src.file_service import JSONService
from src.vacancy import Vacancy


def choose_one_of(question: str, *args: str):
    while True:
        print(question)
        i = 0
        for item in args:
            i += 1
            print(f"{i}. {item}")
        user_input = input()
        i = 0
        for item in args:
            i += 1
            if user_input.lower() in [str(i), item.lower()]:
                return args[i - 1]
        print("Sorry, I don't understand you. Let's try again.")


def search_session():
    vacancy = input("Input vacancy you're interested in: ")

    api_choice = choose_one_of("Choose the vacancy service you want to search through:",
                               'HeadHunter', 'SuperJobs')

    api = SuperJobAPI(vacancy) if api_choice == 'SuperJobs' else HeadHunterAPI(vacancy)

    api_vacancies = api.API_request()
    current_vacancies = []
    print('\nSearch results:')
    for item in api_vacancies['items']:
        new_vacancy = Vacancy(item)
        current_vacancies.append(new_vacancy)
        print(new_vacancy)

    answer = choose_one_of("Do you want to save search results? (yes/no)",
                           'yes', 'no')
    if answer == 'yes':
        while True:
            file_name = input('Insert file name: ')
            json_service = JSONService(os.path.join('search_history', f'{file_name}.json'))
            if json_service.file_exists():
                answer = choose_one_of("File with current name already exists. Do you want to rewrite it? (yes/no):",
                                       'yes', 'no')
                if answer == 'yes':
                    result = []
                    for item in current_vacancies:
                        result.append(item.json)
                    json_result = {
                        "request": vacancy,
                        "search_system": api_choice,
                        "response": result}
                    json_service.write_to_file(json_result)
                    break
