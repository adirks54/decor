from datetime import datetime

FILE_PATH = 'logs1.txt'

def get_log(path):
    def decor(func):
        def foo(*args, **kwargs):
            date_time = datetime.now()
            func_name = func.__name__
            result = func(*args, **kwargs)
            with open(path, 'w') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result
        return foo
    return decor

@get_log(FILE_PATH)
def cook_book_read():
    cook_book_list = {}
    with open('file.txt', 'r') as file:
        for line in file:
            dish_name = line.strip()
            count = int(file.readline())
            dish_ingr_list = []
            for item in range(count):
                ingreds = {}
                ingr = file.readline().strip()
                ingreds['ingredient_name'], ingreds['quantity'], ingreds['measure'] = ingr.split('|')
                dish_ingr_list.append(ingreds)
            file.readline()
            cook_book_list[dish_name] = dish_ingr_list
    return cook_book_list


cook_book = cook_book_read()