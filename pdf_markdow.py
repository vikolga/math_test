import requests
import json


url_pdf = 'https://api.mathpix.com/v3/pdf/'
url_converter = 'https://api.mathpix.com/v3/converter/'

APP_ID = '_100__0660c1_467c9e'
APP_KEY = 'dd95a749c9a33bd2e3626296303bc9349163e18b3437cc08e3017b039bcca0fd'

options = {
    "conversion_formats": {"docx": True, "tex.zip": True},
    "math_inline_delimiters": ["$", "$"],
    "rm_spaces": True
}
r = requests.post(url_pdf,
                  headers={
                      'app_id': APP_ID,
                      'app_key': APP_KEY,
                      },
                  data={"options_json": json.dumps(options)},
                  files={"file": open("pdf_file.pdf", "rb")}
)

value = r.text.encode("utf-8")
decoded_value = value.decode('utf-8').split(':')
pdf_id = decoded_value[1].strip('"}')

ans = ''
while ans != '"completed"':
    rez = requests.get('https://api.mathpix.com/v3/pdf/' + pdf_id,
                       headers={
                           'app_id': APP_ID,
                           'app_key': APP_KEY,
                           }
                           )
    ans = rez.text.split(',')[0].split(':')[1]


url = url_pdf + pdf_id + ".md"
response = requests.get(url,
                        headers={
                            'app_id': APP_ID,
                            'app_key': APP_KEY,
                            })
print(response.text)
with open(pdf_id + ".md", "w", encoding="utf-8") as f:
    f.write(response.text)
