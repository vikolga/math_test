import pandas as pd


QUESTIONS_FILE = 'output_file.md'

# считываем файл
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as file:
    questions = file.readlines()
result = []

# записываем данные во вложенный список
for i in range(len(questions)):
    image = None
    string = questions[i].rstrip()
    if string[:1] == '#':
        capter = string[-1]
    if '![]' in string:
        image = string[5:]
    key = string[:2]
    value = string[3:]
    if key[:1].isalpha() and key[:1].isupper() and key[1:].isdigit():
        result.append([capter, key, value, image])
    if image is not None:
        el = result.pop()
        el[3] = image
        result.append(el)

# переводим вложенный список в список словарей
keys = ['часть', 'номер вопроса', 'вопрос', 'рисунок']
data = []
for item in result:
    dict_item = {keys[i]: item[i] for i in range(len(keys))}
    data.append(dict_item)

# записываем данные в файл
df = pd.DataFrame(result, columns=(['часть', 'номер вопроса', 'вопрос', 'рисунок']))
df.to_excel('./answers_md.xlsx', index=False)
