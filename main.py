import os.path

from src.API_services import HeadHunterAPI
from src.API_services import SuperJobAPI
from src.file_service import JSONService
from src.vacancy import Vacancy


def search_session():
    vacancy = input("Input vacancy you're interested in: ")

    while True:
        service = input("""Choose the vacancy service you want to search through:
                        1. HeadHunter
                        2. SuperJobs
                    """)
        match service.lower():
            case ['1', 'headhunter']:
                api = HeadHunterAPI(vacancy)
                break
            case ['2', 'superjobs']:
                api = SuperJobAPI(vacancy)
                break
            case _:
                print("Sorry, I don't understand you. Let's try again.")

    api_vacancies = api.API_request()
    current_vacancies = []
    print('\nSearch results:')
    for item in api_vacancies['items']:
        new_vacancy = Vacancy(item)
        current_vacancies.append(new_vacancy)
        print(new_vacancy)

    while True:
        answer = input("Do you want to save search results? (yes/no)")
        match answer.lower():
            case 'yes':
                while True:
                    file_name = input('Insert file name: ')
                    json_service = JSONService(os.path.join('search_history', f'{file_name}.json'))
                    if json_service.file_exists():
                        answer = input('File with current name already exists. Do you want to rewrite it? (yes/no): ')
                        match answer.lower():
                            case 'yes':
                                result = []
                                for item in current_vacancies:
                                    result.append(item.json)
                                json_result = {
                                    "request": vacancy,
                                    "search_system": 'headhunter' if service.lower() in ['headhunter',
                                                                                         '1'] else 'superjobs',
                                    "response": result}
                                json_service.write_to_file(json_result)
                            case 'no':
                                continue
            case 'no':
                pass
            case _:
                print("Sorry, I don't understand you. Let's try again.")
