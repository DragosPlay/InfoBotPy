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
    password = ''


    print(password)

def function_2():
    return

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