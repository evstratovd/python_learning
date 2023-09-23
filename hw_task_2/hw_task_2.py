# hw_task_2.1

def stop_words(str_1):
    print(f"Задание №1\n{str_1}")

    new_list = str_1.split()
    new_list.remove('Python')
    new_list.remove('go')
    new_list.remove('php')
    new_list.remove('C')
    print(' '.join(new_list))

stop_words("word1 Python word2 go word3 C word4 word5 php")


# hw_task_2.2

def multiply_list(list_1, m):
    n_list=[]
    for element in list_1:
        if element % m == 0:
            n_list.append(element)
    print(f"\nЗадание№2\nИсходный список:{list_1}\nСписок элементов кратных {m}: {n_list}")

multiply_list([1,4,5,8,9,124,55,2,99], 2)


# hw_task_2.3

def input_string(*args):
    cort_1 = tuple(arg for arg in args if isinstance(arg, str))
    return cort_1

result = input_string('python', 123, 'php', 345, 12.3, 'C')

print(f"\nЗадание№3\n{result}")


# hw_task_2.4


def compare(list_1,list_2):
    new_list = []
    for element in list_1:
        if element in list_2:
            new_list.append(element)

    print(f"\nЗадание№4\n{new_list}")

compare([1,2,3,4,5], [4,5,6,7,8])


# hw_task_2.5
#
#def stairs(kubik):
#    if kubik > 1:
#        j = 0
#        for i in range(1, kubik + 1):
#            j += int(stairs(kubik - i))
#        return j
#    else:
#        return 1


#n = 5
#result = stairs(n)
#print(result)


def kubiki(n, k):
    if n == 0:
        return 1
    count = 0

    for i in range(k + 1, n + 1):
        count += kubiki(n - i, i)
    return count

print("\nЗадание№5")
n = int(input("Введите количество кубиков: "))
if n in range (1,100):
    print(kubiki(n, 0))
else:
    print("Недопустимое число кубиков")


# hw_task_2.6
print("\nЗадание№6")
def check(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, int):
            print("Возвращаемое значение не int")
        return result
    return wrapper

@check
def multi(a, b):
    return a * b

@check
def add(a, b):
    return a + b

result_1 = multi(20, 5)
print(result_1)

result_2 = add(31, 23)
print(result_2)

result_3 = multi("ne int", 2)
print(result_3)

# hw_task_2.7

print('\nЗадание№7')

def try_one_more(func):

    def wrap(*args, **kwargs):
        while True:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as exc:
                print("Исключение:", exc, ". Повторный запуск.")
                continue
    return wrap

#тестовые функции

@try_one_more
def divide(x, y):
    return x / y

@try_one_more
def square_root(number):
    return number ** 0.5

result_5 = divide(10, 2)
print(result_5)  # Выведет 5.0

result_6 = divide(10, 0)
print(result_6)  # Повторный запуск функции, выведет сообщение об исключении

result_7 = square_root(25)
print(result_7)  # Выведет 5.0

result_8 = square_root(-4)
print(result_8)  # Повторный запуск функции, выведет сообщение об исключении


# hw_task_2.8



# hw_task_2.9