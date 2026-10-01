import random
import string

def demo_of_functionality():
    print('''
Чем Вам помочь?
    
1. Сгенерировать пароль 
2. Порекомендуй фильм 
3. Порекомендуй блюдо на ужин 
4. Включи калькулятор 
5. Сыграем в орёл и решка 
6. Сыграем в камень, ножницы, бумага
''')

def function_1():
    chars = string.ascii_letters + string.digits + string.punctuation
    pass_len = int(input('Введите длину пароля: '))
    password = ''.join(random.choices(chars, k=pass_len))
    print(f'Ваш пароль: {password}')


def function_2():
    movies = [
        "Интерстеллар", "Матрица", "Бегущий по лезвию 2049", "Начало",
        "Безумный Макс: Дорога ярости", "Терминатор 2: Судный день", "Криминальное чтиво", "Карты, деньги, два ствола",
        "Большой куш", "Бешеные псы", "Драйв", "Леон",
        "Бойцовский клуб", "Остров проклятых", "Престиж", "Семь",
        "Молчание ягнят", "Помни", "Темный рыцарь", "Побег из Шоушенка",
        "Гладиатор", "Джанго освобожденный", "Таксист", "Большой Лебовски"
    ]
    selected_movie = random.choice(movies)
    print(f'Рекомендуем посмотреть: {selected_movie}2')

def function_3():
    return

def function_4():
    return

def function_5():
    return

def function_6():
    return

actions = {
    '1': function_1,
    '2': function_2,
    '3': function_3,
    '4': function_4,
    '5': function_5,
    '6': function_6
}

print('Добро пожаловать в многофункцонального передового отечественного нейросетевого бота LLM 5G!')

while True:
    demo_of_functionality()
    num_of_function = input('Введите номер необходимой функции: ')
    func = actions.get(num_of_function)
    if func:
        func()
    else:
        print('Некорректный ввод, повторите попытку')