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

Для выхода напишите '项目完成' (или 'Выход')
''')

def function_1():
    chars = string.ascii_letters + string.digits + string.punctuation
    pass_len = input('Введите длину пароля: ')

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
    dinners = [
        "Паста Карбонара с гуанчале и пекорино", "Лазанья Болоньезе",
        "Ризотто с белыми грибами и пармезаном", "Пицца «Четыре сыра»",
        "Паста с креветками в сливочно-чесночном соусе", "Орекьетте с вялеными томатами и базиликом",
        "Капрезе с песто и чиабаттой", "Ньокки в томатном соусе с моцареллой",
        "Удон с говядиной и овощами в соусе терияки", "Рамен со свининой тясю и яйцом",
        "Курица Гунбао с арахисом и рисом", "Пад Тай с креветками и лаймом",
        "Фунчоза с овощами и хрустящей курочкой", "Том Ям с морепродуктами",
        "Стейк Рибай со спаржей", "Запеченный лосось с розмарином",
        "Утиная грудка магрэ с ягодным соусом", "Бефстроганов с картофельным пюре",
        "Куриное филе Кордон Блю", "Боул с авокадо, лососем и киноа",
        "Греческий салат с фетой и багетом", "Салат Цезарь с креветками на гриле",
        "Киш с курицей и грибами", "Запеченные овощи с сыром халуми"
    ]

    dinner = random.choice(dinners)
    print(f'Как насчёт: {dinner}?')

def function_4():
    print("""
Доступные действия: '+', '-', '*', '**', '/', '//', '%'
Для завершения введите: 'Exit' или 'Выход'
""")

    exits = ['Exit', 'exit', 'Выход', 'выход']

    num_1 = input('Введите первое число: ')
    if num_1 in exits:
        return
    action = input('Введите действие: ')
    if num_1 in exits:
        return
    num_2 = input('Введите второе число: ')
    if num_1 in exits:
        return

    num_1, num_2 = int(num_1), int(num_2)

    if action == '+':
        print(num_1 + num_2)
    elif action == '-':
        print(num_1 - num_2)
    elif action == '*':
        print(num_1 * num_2)
    elif action == '**':
        print(num_1 ** num_2)
    elif action == '/' or action == '//' or action == '%':
        if num_2 == 0:
            print('Делить на ноль нельзя!')
        else:
            if action == '/':
                print(num_1 / num_2)
            elif action == '//':
                print(num_1 // num_2)
            elif action == '%':
                print(num_1 % num_2)


def function_5():
    coin_faces = [
        "Орёл", "Решка"
    ]
    coin_faces_all = [
        "Орёл", "Решка", "Орел", "орел", "решка"
    ]
    selected_face = random.choice(coin_faces)
    player_face = ''
    while player_face not in coin_faces_all:
        player_face = input('Орёл или решка? ')
    if player_face.lower() == selected_face.lower() or (selected_face == 'О5рёл' and player_face.lower() == 'орел'):
        print(f'{selected_face}! Вы выиграли!')
    else:
        print(f'{selected_face}! Вы проиграли(')

def function_6():
    actions = [
        "Камень", "Ножницы", "Бумага"
    ]
    actions_all = [
        "Камень", "Ножницы", "Бумага", "камень", "ножницы", "бумага"
    ]
    selected_action = random.choice(actions)
    print('Введите действие')
    player_action = ''
    while player_action not in actions_all:
        player_action = input('Камень, ножницы, бумага: раз-два-три...  ')

    if player_action.lower() == selected_action.lower():
        print(f'{player_action.capitalize()} vs {selected_action}! Ничья!')
    elif player_action.lower() == 'камень' and selected_action.lower() == 'ножницы':
        print(f'{player_action.capitalize()} vs {selected_action}! Вы выиграли!')
    elif player_action.lower() == 'камень' and selected_action.lower() == 'бумага':
        print(f'{player_action.capitalize()} vs {selected_action}! Вы проиграли(')
    elif  player_action.lower() == 'ножницы' and selected_action.lower() == 'бумага':
        print(f'{player_action.capitalize()} vs {selected_action}! Вы выиграли!')
    elif player_action.lower() == 'ножницы' and selected_action.lower() == 'камень':
        print(f'{player_action.capitalize()} vs {selected_action}! Вы проиграли(')
    elif  player_action.lower() == 'бумага' and selected_action.lower() == 'камень':
        print(f'{player_action.capitalize()} vs {selected_action}! Вы выиграли!')
    elif player_action.lower() == 'бумага' and selected_action.lower() == 'ножницы':
        print(f'{player_action.capitalize()} vs {selected_action}! Вы проиграли(')


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
    if num_of_function == 'Выход' or num_of_function == 'выход' or num_of_function == '项目完成':
        break
    func = actions.get(num_of_function)
    if func:
        func()
    else:
        print('Некорректный ввод, повторите попытку')