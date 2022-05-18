"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
from hashlib import sha512
salt = "my salt".encode()


def cache(func):
    def wrapper(*args):
        cache_key = args
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args)
        return wrapper.cache[cache_key]
    wrapper.cache = {}
    return wrapper


@cache
def get_url_hash(url):
    print("Новая ссылка: ", end="")
    return sha512(salt + url.encode()).hexdigest()


if __name__ == "__main__":
    urls = [
        "yandex.ru",
        "google.com",
        "gb.ru",
        "mail.ru",
        "yandex.ru",
        "google.com",
        "gb.ru",
        "mail.ru"
    ]

    for url in urls:
        print(get_url_hash(url))
