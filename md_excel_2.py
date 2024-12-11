import pandas as pd


QUESTIONS_FILE = 'output_file2.md'

# считываем файл
with open(QUESTIONS_FILE, 'r', encoding='utf-8') as file:
    questions = file.readlines()
length = len(questions)
oglavlenie = []
for i in range(length):
    if questions[i].startswith('## ПРЕ'):
        start_point = i + 1
    if questions[i].startswith('## ОГЛ'):
        oglavlenie_point = i + 1
        break
    if questions[i].startswith('## ОТВ'):
        otvet_point = i + 1

# фоормируем список с оглавлением
for i in range(oglavlenie_point, length):
    if questions[i][:1].isdigit():
        q = questions[i].strip('1234567890. \n')
        oglavlenie.append(q.upper())
    elif oglavlenie != []:
        break

# входим в главу
result = []
i = start_point
numb_r = ''
pre_key = 100
count_zadach = [0 for _ in range(len(oglavlenie))]
while i <= oglavlenie_point - 1:
    string = questions[i]
    if string.startswith('##'):
        string = string.split()
        numb = string[1].strip('.')
        nazvanie = ' '.join(string[2:])
        if nazvanie.upper() in oglavlenie:
            i += 1
            numb_r = numb
        else:
            i += 1
    elif string.startswith(f'{numb_r}.'):
        image = 'Отсутствует'
        answer = 'Отсутствует'
        string = string.split()
        capter = numb_r
        len_capter = len(capter)
        quest = questions[i].rstrip()
        # проверяем что строка является задачей
        if quest.startswith(f'{capter}.'):
            key = ''
            for char in quest[len_capter+1:]:
                if char.isdigit() or char == '.':
                    key += char
                elif char == ' ':
                    break
                else:
                    key = ''
                    break
            if key != '':
                len_key = len(capter + '.' + key) + 1
                value = quest[len_key:]
                key = key.strip('.')
                if int(key) < pre_key and result != [] and capter == result[-1][0]:
                    break
                else:
                    result.append([capter, key, value, image, answer])
                    count_zadach[int(capter) - 1] = int(key)
                    pre_key = int(key)
        i += 1
    elif string.startswith('![]'):
        string = string.split()
        quest = questions[i].rstrip()
        image = quest[3:]
        el = result.pop()
        el[3] = image
        result.append(el)
        i += 1        
    else:
        i += 1

i = otvet_point + 1
result_answer = []
answer = ''
r_gl = 0
r_zad = 0
k = 1
# выбираем номер главы
for gl in range(1, len(oglavlenie) + 1):
    # выбираем номер задачи из списка с количеством задач
    for zad in range(1, count_zadach[gl - 1] + 1):
        i = otvet_point + k
        if answer != '':
            result_answer.append([r_gl, r_zad, answer])
            answer = ''
            r_gl = 0
        # проверяем с чего начинается строка
        while i <= oglavlenie_point - 1:
            # берем строку
            string = questions[i]
            # очищаем строку от /n
            quest = questions[i].rstrip()
            if quest.startswith(f'{str(gl)}.{str(zad)}.') and r_gl == 0:
                # запоминаем номер главы и задачи
                r_gl = gl
                r_zad = zad
                # записываем в ответ ответ
                len_quest = len(f'{str(gl)}.{str(zad)}.')
                answer = quest[len_quest:]
                i += 1
            elif (quest.startswith(f'{str(gl)}.') or quest.startswith(f'{str(gl+1)}.')) and r_gl != 0:
                k = i - otvet_point
                break
            elif quest == '':
                i += 1
            elif answer != '':
                answer += quest
                i += 1
            else:
                break


#добавляем ответы в итоговый результат
for i in range(len(result)):
    for j in range(len(result_answer)):
        if int(result[i][0]) == int(result_answer[j][0]) and int(result[i][1]) == int(result_answer[j][1]):
            result[i][4] = result_answer[j][2]


# переводим вложенный список в список словарей
keys = ['часть', 'номер вопроса', 'вопрос', 'рисунок', 'ответ']
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
df = pd.DataFrame(result, columns=(['часть', 'номер вопроса', 'вопрос', 'рисунок', 'ответ']))

writer = pd.ExcelWriter('answer_md_2.xlsx')
df_toc.to_excel(writer, sheet_name='Оглавление', index=False)

for part in df['часть'].unique():
    part_df = df[df['часть'] == part]
    part_df.to_excel(writer, sheet_name=f'Часть {part}', index=False)
writer._save()
