import requests
import string

""" Необходимо получить HTML-код страницы www.python.org, 
и посчитать сколько раз какие символы встречается в коде страницы. 
Формат вывода определяете сами. Вывод программы разместите в файле readme.md. """


QUERY = requests.get('https://www.python.org')


def query_html(query: str) -> str:
    binary_str = query.content
    list_html_str = binary_str.decode('utf-8')
    return list_html_str


def create_templ_ascii() -> str:
    return string.printable



def count_liters() -> dict:
    all_dict={}
    count = 1

    a = query_html(QUERY)
    b = create_templ_ascii()


    ls_a = list(a)
    ls_b = list(b)
    
    for i in ls_b:
        count = 1
        for j in ls_a:
            if i == j:
                all_dict[i]=count
                count+=1
    return all_dict

print(count_liters())


