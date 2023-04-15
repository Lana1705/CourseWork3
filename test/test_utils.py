from utils import get_data, filter_data, sort_data, format_data


def test_filter_data(test_data):
    filtered_data = filter_data(test_data)
    assert [x['state'] for x in filtered_data] == ['EXECUTED', 'EXECUTED']


def test_sort_data(test_data):
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2020-07-03T18:35:29.512364', '2019-08-26T10:50:58.294041', '2018-06-30T02:08:58.425572']


def test_format_data(test_data):
    formatted_data = format_data(test_data)
    assert [formatted_data[0]] == ['\n'
 '26.08.2019 Перевод организации\n'
 'Maestro 1596 83** **** 5199 -> Счет **9589\n'
 '31957.58 руб.        ']
