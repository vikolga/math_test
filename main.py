# import re
import re
import signal
import sys
import pandas as pd
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By


# НЕ ЗАБЫВАЕМ СМЕНИТЬ НАЗВАНИЕ ФАЙЛА
QUESTIONS_FILE = 'Antidemidovich_1_1.md'


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
def split_string_into_chunks(string, chunk_size=100):
    start = 0
    result = ''

    while start < len(string):
        end = start + chunk_size
        chunk = string[start:end]
        new_str = upload_string_to_chat(chunk)
        result += new_str
        start = end
    return result


# функция чтения файла
def read_file(question_file):
    with open(question_file, 'r', encoding='utf-8') as file:
        questions = file.readlines()
    return questions


# функция получения данных файла
def get_oglavlenie_from_markdown(questions):
    # считываем файл
    length = len(questions)
    oglavlenie = []
    start_point = None  # Инициализация переменной start_point

    # формируем список с оглавлением
    for i in range(length):
        line = questions[i]  # Обработка только текущей строки
        match = re.match(r'§\d+\.\s+[\u4e00-\u9fff\s]+\.{3,}\s+\d+\n', line)  # Добавим захватывающую группу
        if match:
            q = match.group(0).strip().upper()
            q = ' '.join(q.split(' ')[1:-1])
            q = q.strip('. ')
            ans = upload_string_to_chat(q)
            oglavlenie.append(ans)
        elif oglavlenie and start_point is None:
            start_point = i + 1  # Зафиксируем точку старта
            break
        else:
            continue

    return (oglavlenie, start_point)


def signal_handler(sig, frame):
    # Обработка прерывания
    print("Программа была прервана вручную. Сохраняем результат...")


def get_data_from_markdown(questions, start_point):

    signal.signal(signal.SIGINT, signal_handler)

    # входим в главу
    result = []
    capter = 0
    image = 'Отсутствует'
    answer = ''
    zadacha = ''
    numb_zadachi = 1
    length = len(questions)
    # Для парсинга части файла новые значения
    # номер задачи должен быть с той задачи, которая идет первая в файле
    # numb_zadachi = 4401
    try:
        for i in range(start_point, length):
            # получаем номер параграфа
            if i == length - 1:
                if len(answer) < 100:
                    answer = upload_string_to_chat(answer)
                else:
                    answer = split_string_into_chunks(answer)
                result.append([capter, str(numb_zadachi - 1), zadacha, answer, image])
            elif questions[i].startswith('## §'):
                if capter != 0 and answer != '':
                    if len(answer) < 100:
                        answer = upload_string_to_chat(answer)
                    else:
                        answer = split_string_into_chunks(answer)
                    result.append([capter, str(numb_zadachi - 1), zadacha, answer, image])
                    answer = ''
                    image = 'Отсутствует'
                q = questions[i].split('.')
                capter = q[0][4:]
                print(f'Глава {capter}')
            # получаем номер задачи и саму задачу
            elif questions[i].startswith(str(numb_zadachi) + '.'):
                print(numb_zadachi)
                if zadacha != '':
                    if len(answer) < 100:
                        answer = upload_string_to_chat(answer)
                    else:
                        answer = split_string_into_chunks(answer)
                    result.append([capter, str(numb_zadachi - 1), zadacha, answer, image])
                    answer = ''
                    image = 'Отсутствует'
                q = questions[i].split('.')
                zadacha = q[1].strip(' ')
                if len(zadacha) < 100:
                    zadacha = upload_string_to_chat(zadacha)
                else:
                    zadacha = split_string_into_chunks(zadacha)
                numb_zadachi += 1
            # получаем рисунок если он есть
            elif questions[i].startswith('![]'):
                if image == 'Отсутствует':
                    image = questions[i].strip('![]')
                else:
                    image += questions[i].strip('![]')
            # получаем ответ и переводим его
            elif zadacha != '':
                ans = questions[i]
                if ans == '' or ans == '\n':
                    continue
                else:
                    answer += (ans + '\n')
            else:
                continue
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        # Логирование ошибки (можно сделать лучше, например, писать в файл)
    finally:
        return result


# функция записи результата в файл
def writing_the_result_to_excel(listing_result, oglavlenie, start_point):
    # переводим вложенный список в список словарей
    keys = ['часть', 'номер задачи', 'задача', 'ответ', 'рисунок', ]
    data = []
    for item in listing_result:
        dict_item = {keys[i]: item[i] for i in range(len(keys))}
        data.append(dict_item)

    table_of_contents = {
        'id': [i for i in range(1, len(oglavlenie) + 1)],
        'Название': oglavlenie,
        'parent': [1 for _ in range(len(oglavlenie))]
    }
    df_toc = pd.DataFrame(table_of_contents)
    df = pd.DataFrame(listing_result, columns=(['часть', 'номер вопроса', 'вопрос', 'ответ', 'рисунок']))

    writer = pd.ExcelWriter('answer_md_2_chine.xlsx')
    df_toc.to_excel(writer, sheet_name='Оглавление', index=False)

    for part in df['часть'].unique():
        part_df = df[df['часть'] == part]
        part_df.to_excel(writer, sheet_name=f'Часть {part}', index=False)
    writer._save()


def main():

    listing_result = []
    oglavlenie = []
    start_point = 0

    questions = read_file(QUESTIONS_FILE)
    oglavlenie, start_point = get_oglavlenie_from_markdown(questions)
    listing_result = get_data_from_markdown(questions, start_point)
    writing_the_result_to_excel(listing_result, oglavlenie, start_point)


if __name__ == '__main__':
    main()
