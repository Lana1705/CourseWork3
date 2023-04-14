import json
from datetime import datetime


def get_data():
    """
    Получение данных из файла
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filter_data(data):
    """
    Фильтрация данных по параметру EXECUTED
    """
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return data


def sorted_key(x):
    return x['date']


def sort_data(data):
    """
    Сортировка данных по дате и получение первых 5
    """
    data = sorted(data, key=sorted_key, reverse=True)
    return data[:5]


def format_data(data):
    """
    Форматирование и вывод результата
    """
    formated_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime("%d.%m.%Y")
        description = row['description']
        amount = row['operationAmount']['amount']
        name = row['operationAmount']['currency']['name']
        if "from" in row:
            from_arrow = "->"
            sender = row['from'].split()
            sender_bill = sender.pop(-1)
            sender_info = " ".join(sender)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            account_number = row['to'].split()
            to_bill = account_number.pop(-1)
            to_bill = f"Счет **{to_bill[-4:]}"
        else:
            sender_info = "Новый счет"
            sender_bill = ""
            from_arrow = ""
            account_number = row['to'].split()
            to_bill = account_number.pop(-1)
            to_bill = f"**{to_bill[-4:]}"

        formated_data.append(f"""
{date} {description}
{sender_info} {sender_bill} {from_arrow} {to_bill}
{amount} {name}\
        """)
    return formated_data
