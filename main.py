from time import sleep
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

from constants import MAIN_URL_MATH, QUESTION


if __name__ == '__main__':
    response = requests.get(MAIN_URL_MATH + QUESTION)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    reshenie = soup.find('div', class_='TemplateSelector_solutionOptions__yKoQF TemplateSelector_multi__1lZyB')
    result = reshenie.find_all('div', class_='TemplateSelector_name__6oev8')
    result_1 = []
    for ans in result:
        result_1.append(ans.text)
    result_2 = []
    sleep(3)
    driver = webdriver.Chrome()
    driver.get(MAIN_URL_MATH + QUESTION)
    driver.find_element(By.CLASS_NAME, 'ms-Button.ms-Button--primary.CardButton_cardButton__KYZhg.root-164').click()
    for answer in result_1:
        driver.find_element(By.XPATH, f'//button[normalize-space()="{answer}"]').click()
        sleep(3)
        result = soup.find('div', attrs={'class':'Step_stepPreview__pKL0W'})
        result_2.append(result)

    # result_2 = soup.find_all('div', attrs={'class':'Steps_solutionSteps__a7lQq'})
    dict_res = {}
    for i in range(len(result_2)):
        dict_res[result_1[i]] = result_2[i].text
    print(dict_res)
