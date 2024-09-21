import requests
from bs4 import BeautifulSoup


QUESTION = 'x%5E%7B2%7D-3x%2B2%3D0'
MAIN_URL_MATH = 'https://mathsolver.microsoft.com/ru/solve-problem/'


if __name__ == '__main__':
    response = requests.get(MAIN_URL_MATH + QUESTION)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    reshenie = soup.find('div', class_='TemplateSelector_solutionOptions__yKoQF TemplateSelector_multi__1lZyB')
    result_1 = reshenie.find_all('div', class_='TemplateSelector_name__6oev8')
    for i in range(len(result_1)):
        print(result_1[i].text)
    result_2 = soup.find_all('div', attrs={'class':'Steps_solutionSteps__a7lQq'})
    for i in range(len(result_2)):
        print(result_2[i].text)
    dict_res = {}
    for i in range(len(result_2)):
        dict_res[result_1[i].text] = result_2[i].text
    print(dict_res)

