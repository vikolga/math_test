
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import re
import pandas as pd


QUESTIONS_FILE = 'questions copy.csv'
bad_escape_re = re.compile(r'\\(?=[^\n\\\'"abfnrtv0-7xNuU])')
FILE_JSON = 'answers.xls'
result_answer = {}

with open(QUESTIONS_FILE, 'r', encoding='utf-8') as file:
    questions = file.readlines()
result = {}
for i in range(1, len(questions)):
    question = questions[i].strip('\n').split('"')
    id = question[0].strip(',')
    zadacha = question[1]
    if ':' in zadacha:
        z = re.split(r'\w: ', zadacha)
        if len(z) > 1:
            zadacha = re.split(r'\w: ', zadacha)[1]
            zadacha = bad_escape_re.sub('', zadacha).strip()
    result[id] = zadacha

option = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=option)
for key, value in result.items():
    if '%' in value or value[0].isalpha():
        continue
    browser.get(f'https://mathsolver.microsoft.com/ru/solve-problem/{value}')
    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')

# находим скрипты
    element = soup.find('script', id='__NEXT_DATA__')
    mess = soup.find('div', class_='MathErrorMessage_message__H_NQf')
    if mess == 'Мы не можем решить такой тип уравнения, или, возможно, в нем содержится ошибка':
        continue
    js_el = json.loads(element.text)
    if len(js_el['props']['pageProps']['response']['mathSolverResult']['actions']) == 0:
        continue
    else:
        js_equa = js_el['props']['pageProps']['response']['mathSolverResult']['actions'][0]['templateSteps']
        if js_equa != []:
            result_answer.setdefault('id', []).append(key)
            result_answer.setdefault('solve', []).append(js_equa)
df = pd.DataFrame(result_answer)
df.to_excel('./answers.xlsx')
