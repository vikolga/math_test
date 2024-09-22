import requests
import json
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from constants import MAIN_URL_MATH, QUESTION


def main():
    response = requests.get(MAIN_URL_MATH + QUESTION)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    reshenie = soup.find('div', class_='TemplateSelector_solutionOptions__yKoQF TemplateSelector_multi__1lZyB')
    result = reshenie.find_all('div', class_='TemplateSelector_name__6oev8')
    result_names = []
    for ans in result:
        result_names.append(ans.text)
    result_answers = []
    driver = webdriver.Chrome()
    driver.get(MAIN_URL_MATH + QUESTION)
    driver.find_element(By.CLASS_NAME, 'ms-Button.ms-Button--primary.CardButton_cardButton__KYZhg.root-164').click()
    for answer in result_names:
        driver.find_element(By.XPATH, f'//button[normalize-space()="{answer}"]').click()
        result = driver.find_element(By.CLASS_NAME, 'Steps_solutionSteps__a7lQq')
        result_answers.append(result.text)
    answers = dict(zip(result_names, result_answers))
    return answers


if __name__ == '__main__':
    answers = main()
    FILE_JSON = 'answers.json'
    with open(FILE_JSON, 'w', encoding='utf-8') as outfile:
        json.dump(answers, outfile, ensure_ascii=False, indent=4) 
