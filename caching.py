import requests_cache

QUESTION = 'x%5E%7B2%7D-3x%2B2%3D0'
MAIN_URL_MATH = 'https://mathsolver.microsoft.com/ru/solve-problem/'


if __name__ == '__main__':
    session = requests_cache.CachedSession()
    session.cache.clear()
    response = session.get(MAIN_URL_MATH + QUESTION)
    print(session.cache.urls())
