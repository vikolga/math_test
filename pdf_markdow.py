import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()

url_pdf = 'https://api.mathpix.com/v3/pdf/'
url_converter = 'https://api.mathpix.com/v3/converter/'

APP_ID = os.getenv('APP_ID')
APP_KEY = os.getenv('APP_KEY')

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
    print(ans)


url = url_pdf + pdf_id + ".md"
response = requests.get(url,
                        headers={
                            'app_id': APP_ID,
                            'app_key': APP_KEY,
                            })
print(response.text)
with open(pdf_id + ".md", "w", encoding="utf-8") as f:
    f.write(response.text)
