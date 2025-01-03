import pandas as pd
import requests
import json
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


QUESTIONS_FILE = 'Antidemidovich_1.md'

# функция перевода строки в 200 символов
def upload_string_to_chat(stroka):
    driver = webdriver.Chrome()
    url = 'https://gptforwork.com/tools/translate'
    driver.get(url)
    textarea = driver.find_element(By.TAG_NAME, "textarea")
    textarea.send_keys(stroka)
    button = driver.find_element(By.CSS_SELECTOR, ".button_button__8MxK7.button_primary__c0iIz.translate_button__4YOtC")
    button.click()
    sleep(5)  # заменить на проверку готовности перевода
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    translated_text = soup.find_all('textarea', class_='textarea_textarea__6CKGx textarea-row_textarea__bHdjA')
    new_string = translated_text[1].text
    return new_string


# функция разбиения и перевода строки длиной болше 200 символов
def split_string_into_chunks(string, chunk_size=200):
    start = 0
    result = ''

    while start < len(string):
        end = start + chunk_size
        chunk = string[start:end]
        new_str = upload_string_to_chat(chunk)
        result += new_str
        start = end
    return result


# считываем файл
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as file:
    questions = file.readlines()
# считываем оглавление книги
length = len(questions)
oglavlenie = []

# фоормируем список с оглавлением
for i in range(length):
    if questions[i].startswith('§'):
        q = questions[i].split('.')[1]
        q = q.strip(' ')
        ans = upload_string_to_chat(q)
        oglavlenie.append(ans)
    elif oglavlenie != []:
        start_point = i + 1
        break
    else:
        continue

# входим в главу
result = []
capter = 0
image = 'Отсутствует'
answer = ''
zadacha = ''
numb_zadachi = 1
start_point = 10
for i in range(start_point, length):
    # получаем номер параграфа
    if questions[i].startswith('## §'):
        if capter != 0:
            if len(answer) <= 200:
                answer = upload_string_to_chat(answer)
            else:
                answer = split_string_into_chunks(answer)
            result.append([capter, str(numb_zadachi-1), zadacha, answer, image])
            answer = ''
            image = 'Отсутствует'
        q = questions[i].split('.')
        capter = q[0][4:]
    # получаем номер задачи и саму задачу
    elif questions[i].startswith(str(numb_zadachi) + '.'):
        if zadacha != '':
            if len(answer) <= 200:
                answer = upload_string_to_chat(answer)
            else:
                answer = split_string_into_chunks(answer)
            result.append([capter, str(numb_zadachi-1), zadacha, answer, image])
            answer = ''
            image = 'Отсутствует'
        q = questions[i].split('.')
        zadacha = q[1].strip(' ')
        zadacha = upload_string_to_chat(zadacha)
        numb_zadachi += 1
    # получаем рисунок если он есть
    elif questions[i].startswith('![]'):
        image = questions[i].strip('![]')
    # получаем ответ и переводим его
    elif zadacha != '':
        ans = questions[i]
        if ans == '' or ans == '\n':
            continue
        else:
            answer += (ans + '\n')
    else:
        continue


# переводим вложенный список в список словарей
keys = ['часть', 'номер задачи', 'задача', 'ответ', 'рисунок', ]
data = []
for item in result:
    dict_item = {keys[i]: item[i] for i in range(len(keys))}
    data.append(dict_item)

table_of_contents = {
    'id': [i for i in range(1, len(oglavlenie) + 1)],
    'Название': oglavlenie,
    'parent': [0 for _ in range(len(oglavlenie))]
}
df_toc = pd.DataFrame(table_of_contents)
df = pd.DataFrame(result, columns=(['часть', 'номер вопроса', 'вопрос', 'ответ', 'рисунок']))

writer = pd.ExcelWriter('answer_md_2_chine.xlsx')
df_toc.to_excel(writer, sheet_name='Оглавление', index=False)

for part in df['часть'].unique():
    part_df = df[df['часть'] == part]
    part_df.to_excel(writer, sheet_name=f'Часть {part}', index=False)
writer._save()

# # определяем, нужно ли переводить строку
# for strin in questions:
#     if strin == '' or strin == '\n':
#         continue
#     elif strin == '$$\n':
#         if check_in == False:
#             check_in = True
#         else:
#             check_in = False
#         with open(file_new, 'a', encoding='utf-8') as file:
#             file.write(strin + '\n')
#             continue
#     elif check_in:
#         with open(file_new, 'a', encoding='utf-8') as file:
#             file.write(strin + '\n')
#             continue
#     else:
#         new_string = upload_string_to_chat(strin)
#         with open(file_new, 'a', encoding='utf-8') as file:
#             file.write(new_string + '\n')
