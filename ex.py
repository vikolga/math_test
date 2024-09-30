
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


QUESTIONS_FILE = 'questions.csv'
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
    print(zadacha)
    if ':' in zadacha:
        zadacha = re.split(r'\w: ', zadacha)[1]
        zadacha = bad_escape_re.sub('', zadacha).strip()
    # if zadacha[:1].isdigit() or zadacha[:1] == '(':
    result[id] = zadacha


option = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=option)
for key, value in result.items():
    browser.get(f'https://mathsolver.microsoft.com/ru/solve-problem/{value}')
    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')

# находим скрипты
    element = soup.find('script', id='__NEXT_DATA__')
    js_el = json.loads(element.text)
    if len(js_el['props']['pageProps']['response']['mathSolverResult']['actions']) == 0:
        continue
    else:
        js_equa = js_el['props']['pageProps']['response']['mathSolverResult']['actions'][0]['templateSteps']
        result_answer.setdefault('id', []).append(id)
        result_answer.setdefault('solve', []).append(js_equa)
df = pd.DataFrame(result_answer)
df.to_excel('./answers.xlsx')
