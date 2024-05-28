from abc import ABC,abstractmethod
# ПЕРВЫЙ УРОК
"""class Animal:
    paws = 4
    def __init__(self, name):
        self.name = name
class Cat(Animal):
    def meow(self):
        print("Meow")
class Dog(Animal):
    def woof(self):
        print("Woof")
class Parrot(Animal):
    def __init__(self,name):
        Animal.__init__(self,name)
        self.paws = 2
    def chirp(self,num):
        if num == 1:
            print("Чик-Чирик")
        elif num == 2:
            print(Dog.woof(self.name))

my_dog1 = Dog("Bobik")
my_cat1 = Cat("Murzik")
my_parrot1 = Parrot("Гоша")
print(f"{my_dog1.name} has {my_dog1.paws} paws")
print(f"{my_cat1.name} has {my_cat1.paws} paws")
print(f"{my_parrot1.name} has {my_parrot1.paws}")
my_parrot1.chirp(2)"""



#ЗАДАНИЕ №2 ПЕРВЫЙ УРОК
"""class Figure:
    '''Список фигур'''

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        '''Вычисление периметра для фигур'''
        return self.a + self.b + self.c + self.d


class Triangle(Figure):
    '''Треугольник'''

    def __init__(self, a, b, c):




        super().__init__(a, b, c, 0)

    def perimeter(self):
        '''Вычисление периметра для треугольника'''
        return self.a + self.b + self.c


class Tetragon(Figure):
    '''Четырехугольник'''

    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)

    def perimeter(self):
        '''Вычисление периметра для четырехугольника'''
        return self.a + self.b + self.c + self.d


class Square(Tetragon):
    '''Квадрат'''

    def __init__(self, a):
        super().__init__(a, a, a, a)

    def perimeter(self):
        '''Вычисление периметра для квадрата'''
        return 4 * self.a


class Rectangle(Tetragon):
    '''Прямоугольник'''

    def __init__(self, a, b):
        super().__init__(a, b, a, b)

    def perimeter(self):
        '''Вычисление периметра для прямоугольника'''
        return 2 * (self.a + self.b)


def input_sides(prompt):
    '''Функция для ввода сторон фигуры'''
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Цыфра должна быть положительной.")
            return value
        except ValueError as error:
            print("Ошибка:", error)


def main():
    '''Основная функция'''
    while True:
        print("\nВыберите фигуру:")
        print("1. Треугольник")
        print("2. Квадрат")
        print("3. Прямоугольник")
        print("4. Выход")

        choice = input("Введите номер фигуры: ")

        if choice == "1":
            a = input_sides("Введите длину первой стороны треугольника: ")
            b = input_sides("Введите длину второй стороны треугольника: ")
            c = input_sides("Введите длину третьей стороны треугольника: ")
            triangle = Triangle(a, b, c)
            print("Периметр треугольника:", triangle.perimeter())
        elif choice == "2":
            side = input_sides("Введите длину стороны квадрата: ")
            square = Square(side)
            print("Периметр квадрата:", square.perimeter())
        elif choice == "3":
            a = input_sides("Введите длину первой стороны прямоугольника: ")
            b = input_sides("Введите длину второй стороны прямоугольника: ")
            rectangle = Rectangle(a, b)
            print("Периметр прямоугольника:", rectangle.perimeter())
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()"""



#ЗАДАНИЕ № ВТОРОЙ УРОК

# class Figure(ABC):
#     '''Список фигур'''
#
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#     @abstractmethod
#     isPossible():
#     '''проверка возмоюна ли фингура'''
#         pass
#
#
#
#     def perimeter(self):
#         '''Вычисление периметра для фигур'''
#         return self.a + self.b + self.c + self.d
#
#
# class Triangle(Figure):
#     '''Треугольник'''
#
#     def __init__(self, a, b, c):
#
#
#
#
#         super().__init__(a, b, c, 0)
#
#     def perimeter(self):
#         '''Вычисление периметра для треугольника'''
#         return self.a + self.b + self.c
#
#
# class Tetragon(Figure):
#     '''Четырехугольник'''
#
#     def __init__(self, a, b, c, d):
#         super().__init__(a, b, c, d)
#
#     def perimeter(self):
#         '''Вычисление периметра для четырехугольника'''
#         return self.a + self.b + self.c + self.d
# class Square(Tetragon):
#     '''Квадрат'''
#     def __init__(self, a):
#         super().__init__(a, a, a, a)
#     def perimeter(self):
#         '''Вычисление периметра для квадрата'''
#         return 4 * self.a
#
# class Rectangle(Tetragon):
#     '''Прямоугольник'''
#     def __init__(self, a, b):
#         super().__init__(a, b, a, b)
#     def perimeter(self):
#         '''Вычисление периметра для прямоугольника'''
#         return 2 * (self.a + self.b)






# #ПРАКТИКА OOP
''' Создание классов: Создайте класс Компонент. Включите в него атрибуты, такие как
название компонента, производитель и цена. Добавьте метод для вывода информации о
компоненте.
 Наследование: Создайте подклассы Процессор, Видеокарта и ЖесткийДиск,
наследующие от Компонент. Добавьте свои уникальные атрибуты и методы для
каждого подкласса.
 Перегрузка операторов: Реализуйте оператор > для класса Компонент, который будет
сравнивать компоненты по цене и возвращать True, если цена первого компонента
больше.'''

"""class Component:
    '''компонент'''
    def __init__(self, component_name, manufacturer, price):
        self.component_name = component_name
        self.manufacturer = manufacturer
        self.price = price
    def __gt__(self, other):
        return self.component_name > other.component_name and self.manufacturer > other.manufacture and self.price > other.price


class CPU(Component):
    '''Процессор'''
    def __init__(self, cores, thread_management, stream_processors_cores, memory, component_name, manufacturer, price):
        super().__init__(component_name, manufacturer, price)
        self.cores = cores
        self.thread_management = thread_management
        self.stream_processors_cores = stream_processors_cores
        self.memory = memory


class Video_card(Component):
    '''видео карта'''
    def __init__(self, model, cooling, maximum_resolution, connectors, clock_frequency, component_name, manufacturer, price, memory):
        super().__init__(component_name, manufacturer)
        self.model = model
        self.cooling = cooling
        self.maximum_resolution = maximum_resolution
        self.connectors = connectors
        self.clock_frequency = clock_frequency
        self.price = price
        self.memory = memory


class HDD(Component):
    '''жеский диск'''
    def __init__(self, performance, memory, component_name, manufacturer, price):
        super().__init__(component_name, manufacturer, price)
        self.performance = performance
        self.cmemory = memory
a = CPU(cores = 4, thread_management = 16, stream_processors_cores = "i7" , memory = 16,  component_name = "AMD", manufacturer = "ASUS", price = 300)
b = CPU(cores = 4, thread_management = 24, stream_processors_cores = "i9" , memory = 32,  component_name = "AMD", manufacturer = "ASUS", price = 500)

print(a > b)"""




'''Задание Абстракция для Управления Техникой в Доме
 Создайте абстрактный класс "УмноеУстройство" с методами:
 включить (включает устройство)
 выключить (выключает устройство)
 описание (возвращает описание устройства)
 Создайте два подкласса этого абстрактного класса:
 УмныйТермостат с атрибутами "модель" и "температура".
 УмныйСветильник с атрибутами "марка" и "яркость".
 Реализуйте методы включить, выключить и описание в подклассах.
 Создайте несколько экземпляров каждого подкласса и продемонстрируйте работу
методов.
 Реализуйте новый подкласс "УмныйЗамок" с атрибутами "модель" и "закрыт" (флаг,
указывающий, закрыт ли замок). Реализуйте методы включить, выключить и
описание.
 Выведите информацию о нескольких экземплярах каждого класса, используя метод
описание.'''
"""class SmartDevice(ABC):
    '''Абстрактный класс для умных устройств'''

    def __init__(self, device_description):
        self._device_description = device_description

    @abstractmethod
    def turn_on(self):
        '''Включить устройство'''
        pass

    @abstractmethod
    def turn_off(self):
        '''Выключить устройство'''
        pass

    def get_device_description(self):
        return self._device_description


class SmartThermostat(SmartDevice):
    '''Класс для умного термостата'''

    def __init__(self, model, temperature, device_description):
        super().__init__(device_description)
        self.model = model
        self.temperature = temperature
        self._is_on = False

    def turn_on(self):
        self._is_on = True
        print(f"Умный термостат {self.model} включен")

    def turn_off(self):
        self._is_on = False
        print(f"Умный термостат {self.model} выключен")

    def is_on(self):
        return self._is_on


class SmartLight(SmartDevice):
    '''Класс для умного светильника'''

    def __init__(self, brand, brightness, device_description):
        super().__init__(device_description)
        self.brand = brand
        self.brightness = brightness
        self._is_on = False

    def turn_on(self):
        self._is_on = True
        print(f"Умный светильник {self.brand} включен")

    def turn_off(self):
        self._is_on = False
        print(f"Умный светильник {self.brand} выключен")

    def is_on(self):
        return self._is_on


class SmartLock(SmartDevice):
    '''класс для умного замка'''
    def __init__(self, model, closed, device_description):
        super().__init__(device_description)
        self.model = model
        self.closed = closed

    def turn_on(self):
        print(f"Умный замок {self.model} включен")

    def turn_off(self):
        print(f"Умный замок {self.model} выключен")

    def is_locked(self):
        return self.closed

    def lock(self):
        self.closed = True

    def unlock(self):
        self.closed = False


# Создание экземпляров классов
thermostat1 = SmartThermostat("Nest", 22, "Умный термостат в ванной")
thermostat2 = SmartThermostat("Ecobee", 20, "Умный термостат в спальне")
light1 = SmartLight("Philips", "Яркий", "Умный светильник в прихожей")
light2 = SmartLight("Philips", "Теплый", "Умный светильник в гостиной")
lock1 = SmartLock("Xiaomi", True, "Умный замок на входной двери")
lock2 = SmartLock("Xiaomi", False, "Умный замок на задней двери")

# Включение и выключение устройств
thermostat1.turn_on()
thermostat2.turn_off()
light1.turn_on()
light2.turn_off()
lock1.turn_on()
lock2.turn_off()

# Вывод описания устройств
print(thermostat1.get_device_description())
print(thermostat2.get_device_description())
print(light1.get_device_description())
print(light2.get_device_description())
print(lock1.get_device_description())
print(lock2.get_device_description())"""




'''Задание: Школьные предметы
 Создание классов: Создайте класс Предмет. Включите в него атрибуты, такие как
название предмета, количество часов и учитель. Добавьте метод для вывода
информации о предмете.

 Наследование: Создайте подклассы Математика, Литература и Физика,
наследующие от Предмет. Добавьте свои уникальные атрибуты и методы для каждого
подкласса.

 Перегрузка операторов: Реализуйте оператор == для класса Предмет, который будет
возвращать True, если у двух предметов совпадает название и учитель.'''


"""class Subject:
    '''школьные предметы'''

    def __init__(self, item_name, number_of_hours, teacher):
        self.item_name = item_name
        self.number_of_hours = number_of_hours
        self.teacher = teacher

    def __eq__(self, other):
        '''сравнение'''
        return self.item_name == other.item_name and self.teacher == other.teacher


class Mathematics(Subject):
    '''Математика'''

    def __init__(self, item_name, number_of_hours, teacher, versatility, accuracy, beauty):
        super().__init__(item_name, number_of_hours, teacher)
        self.versatility = versatility
        self.accuracy = accuracy
        self.beauty = beauty


class Literature(Subject):
    '''Литература'''

    def __init__(self, item_name, number_of_hours, teacher, creative_expression, developing_empathy, cultural_heritage):
        super().__init__(item_name, number_of_hours, teacher)
        self.creative_expression = creative_expression
        self.developing_empathy = developing_empathy
        self.cultural_heritage = cultural_heritage


class Physics(Subject):
    '''Физика'''

    def __init__(self, item_name, number_of_hours, teacher, understanding_world, interdisciplinarity, technological_applications):
        super().__init__(item_name, number_of_hours, teacher)
        self.understanding_world = understanding_world
        self.interdisciplinarity = interdisciplinarity
        self.technological_applications = technological_applications




mathematics1 = Mathematics("Математика", 5, "Иванов", "Всеобъемлющесть", "Правильность", "Привлекательность")
mathematics2 = Mathematics("Математика", 4, "Петров", "Всесторонность", "Аккуратность", "Гармония")
literature1 = Literature("Литература", 3, "Сидоров", "Художественное творчество", "Понимание и сочувствие", "Историческое наследие")
literature2 = Literature("Литература", 3, "Сидоров", "Творческая самореализация", "Эмоциональная интеллигентность", "Культурное богатство")


print(mathematics1 == mathematics2)
print(literature1 == literature2)"""


#УРОК ЧЕТЫРИ
"""class Test:
    def __init__(self, test_1, test_2):
        self.test_1 = test_1
        self.test_2 = test_2
    def __str__(self):
        return f"{self.test_1} {self.test_2}"
    def __repr__(self):
        return f"{self.test_1} {self.test_2}"


test_pr_1 = Test(1, 2)
test_pr_2 = Test(3,4)
# print(test_pr_1)
# print(test_pr_2)
# setattr(test_pr_1, 'test_1' ,12)
# print(test_pr_1)
# print(test_pr_2)
#print(dir(test_pr_1))"""

"""class Test:
    def __call__(self, message):
        print(message.upper(), ' ', message.lower())
        return True
test_1 = Test()
test_1("Hello world")

print(test_1)"""

#ПРАКТИКА 4

'''1. Создайте класс MyTime. Конструктор должен принимать на вход
строку вида ЧЧ:ММ (часы:минуты) и преобразовывать их в
отдельные атрибуты hour и min. Обратите внимание, и часы,
минуты могут быть указаны с незначащим нулём, например,
05:35.

2. Определите метод __int__, выводящий на экран целое число –
полное количество минут (например, int(02:05) = 125).

3. Определите метод, преобразующий полученное время в 12-
часовой формат (с указанием AM (до полудня) или PM (после
полудня).'''


"""class MyTime:
    '''Время'''
    def __init__(self, time_str):
        '''Конструктор'''

        time_str = time_str.split(':')
        self.hours = int(time_str[0])
        self.minutes = int(time_str[1])

    def __str__(self):
        '''Преобразования объекта времени в строку'''
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __int__(self):
        '''Преобразования объекта времени в целое число'''
        return self.hours * 60 + self.minutes

    def format_12_hour(self):
        '''Форматирования времени в 12-часовой формат с AM/PM'''
        period = "AM"
        hours12 = self.hours
        if self.hours >= 12:
            period = "PM"
            if self.hours > 12:
                hours12 = self.hours - 12
        if hours12 == 0:
            hours12 = 12
        return f"{hours12:02d}:{self.minutes:02d} {period}"


time_test_1 = MyTime("02:05")
print(int(time_test_1))

time_test_2 = MyTime("14:30")
print(int(time_test_2))

print(time_test_1.format_12_hour())
print(time_test_2.format_12_hour())"""


#УРОК ПЯТЬ

"""class Animal:
    def __init__(self, name):
        self.name = name

class Zoo:
    def __init__(self):
        self.cage = []

myzoo1 = Zoo()
tiger01 = Animal("Tiger 1")
tiger02 = Animal("Tiger 2")
myzoo1.cage.append(tiger01)
myzoo1.cage.append(tiger02)
for t in myzoo1.cage:
    print(t.name)

class Animal:
    paws = 4
    tail = 1
    eyes = 2
    def __init__(self):
        self.paws = Animal.paws
        self.tail = Animal.tail
        self.eyes = Animal.eyes
class Cat(Animal):
    def printProperties(self):
        print(self.paws,self.tail, self.eyes)
class Zoo:
    def __init__(self):
        self.cage = [Animal(), Cat()]
        print(self.cage[0].paws,self.cage[0].tail, self.cage[0].eyes)
mycat1 = Cat()
mycat1.printProperties() # 4 1 2
myzoo1 = Zoo() # 4 1

class Engine:
    def start(self):
        print("Двигатель заведен")
class Car:
    def __init__(self):
        self.engine = Engine()  # Создаем объект двигателя при создании машины
    def start_car(self):
        self.engine.start()  # Запускаем двигатель машины
# Создаем машину
my_car = Car()
# Запускаем машину
my_car.start_car()  # Вывод: 'Двигатель заведен'"""


#ПРАКТИКА 5

'''Практика. Часть 1
Задание: Классы "Учебная программа" и "Курс"
Создай класс Курс (Course) со следующими атрибутами:
• название (название курса)
• продолжительность (продолжительность курса в неделях)
• преподаватель (имя преподавателя)

Создай класс УчебнаяПрограмма (Curriculum) со следующими атрибутами:
• название (название учебной программы)
• курсы (список объектов класса Курс, входящих в учебную программу)
Кроме того, у класса УчебнаяПрограмма должен быть метод добавить_курс,
который принимает объект класса Курс и добавляет его в список курсов учебной
программы. 
Создай несколько объектов класса Курс и несколько объектов класса
УчебнаяПрограмма. Добавь курсы в учебные программы с использованием метода
добавить_курс.
Выведи информацию о курсах в каждой учебной программе.

Практика . Часть 2
Задание: Классы "Банк", "Счет" и "Клиент"
Создай класс Счет (Account) со следующими атрибутами:
• номер_счета (уникальный номер счета)
• баланс (текущий баланс на счете)
•Создай класс Клиент (Client) со следующими атрибутами:
• имя (имя клиента)
• счет (объект класса Счет, который принадлежит клиенту)
•Создай класс Банк (Bank) со следующими атрибутами:
• название (название банка)
• клиенты (список объектов класса Клиент, которые являются клиентами банка)
Кроме того, у класса Банк должен быть метод создать_счет (create_account), который
принимает имя клиента, создает новый счет для клиента и добавляет клиента в список клиентов
банка.
Создай несколько объектов класса Банк, несколько объектов класса Клиент и используй метод
создать_счет, чтобы добавить счета клиентам.
Реализуйте методы внести_на_счет и снять_со_счета в классе Счет, чтобы можно было изменять
баланс счета.
Выведи информацию о клиентах и их счетах.'''

"""class Course:
    '''Курс'''
    def __init__(self, name, lasting, teacher):
        '''Название курса, продолжительность курса в неделях, имя преподавателя'''
        self.name = name
        self.lasting = lasting
        self.teacher = teacher

class Curriculum:
    '''Учебная Программа'''
    def __init__(self):
        '''Список объектов класса Курс, входящих в учебную программу'''
        self.courses = []
my_curriculum = Curriculum()
course_1 = Course('online', 12, 'Mr. Smith')
course_2 = Course('offline', 10, 'Mr. Anderson')
my_curriculum.courses.append(course_1)
my_curriculum.courses.append(course_2)
for course in my_curriculum.courses:
    print(f"Название учебной программы {course.name}, Название курса {course.lasting} недель, Имя учителя {course.teacher}")"""

#ЗАДАНИЕ 2

'''Создай класс Счет (Account) со следующими атрибутами:
• номер_счета (уникальный номер счета)
• баланс (текущий баланс на счете)

•Создай класс Клиент (Client) со следующими атрибутами:
• имя (имя клиента)
• счет (объект класса Счет, который принадлежит клиенту)

•Создай класс Банк (Bank) со следующими атрибутами:
• название (название банка)
• клиенты (список объектов класса Клиент, которые являются клиентами банка)

Кроме того, у класса Банк должен быть метод создать_счет (create_account), который
принимает имя клиента, создает новый счет для клиента и добавляет клиента в список клиентов
банка.

Создай несколько объектов класса Банк, несколько объектов класса Клиент и используй метод
создать_счет, чтобы добавить счета клиентам.
Реализуйте методы внести_на_счет и снять_со_счета в классе Счет, чтобы можно было изменять
баланс счета.
Выведи информацию о клиентах и их счетах.'''

# class Account:
#     '''Счет'''
#     def __init__(self, account_number, balance):
#         '''Уникальный номер счета, текущий баланс на счете'''
#         self.account_number = account_number
#         self.balance = balance
#
#     def deposit(self, amount):
#         '''Внести на счет'''
#         self.balance += amount
#
#     def withdraw(self, amount):
#         '''Снять со счета'''
#         if amount <= self.balance:
#             self.balance -= amount
#             return True
#         else:
#             print("Недостаточно средств на счете.")
#             return False
#
# class Client:
#     '''Клиент'''
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
# class Bank:
#     '''Банк'''
#     def __init__(self, bank_name):
#         self.bank_name = bank_name
#         self.clients = []
#
#     def create_account(self, client_name, initial_balance=0):
#         '''Создает новый счет и добавляет клиента в список клиентов банка'''
#         account_number = len(self.clients) + 1
#         new_account = Account(account_number, initial_balance)
#         new_client = Client(client_name, new_account)
#         self.clients.append(new_client)
#         return new_account
#
#
# # Банк
# bank1 = Bank("Bank of A")
# bank2 = Bank("Bank of B")
#
# #Клиент
# client1 = Client("Олег", "VIP")
# client2 = Client("Настя", "Обычный")
#
# # Добавление счетов
# account1 = bank1.create_account(client1.name, 1000)
# account2 = bank2.create_account(client2.name, 500)
#
# # Внесение и снятие
# account1.deposit(500)
# account2.withdraw(200)
#
# # Вывод информации о клиентах и их счетах
# for client in bank1.clients:
#     print(f"Клиент: {client.name}, Баланс счета: {client.score.balance} Сом")
#
# for client in bank2.clients:
#     print(f"Клиент: {client.name}, Баланс счета: {client.score.balance} Сом")





#ПРАКТИКА 27 МАЯ



# class Aircraft:
#     '''Самолет'''
#     def __init__(self, model, seats, route=None):
#         self.model = model
#         self.seats = seats
#         self.flight = False
#         self.route = route
#
#     def take_off(self):
#         '''Взлет самолета'''
#         if not self.flight:
#             self.flight = True
#             print(f"{self.model} взлетел.")
#         else:
#             print(f"{self.model} уже в полете.")
#
#     def land(self):
#         '''Земля'''
#         if self.flight:
#             self.flight = False
#             print(f"{self.model} приземлился.")
#         else:
#             print(f"{self.model} уже на земле.")
#
#     def change_route(self, new_route):
#         '''Изменение маршрута'''
#         if self.flight:
#             self.route = new_route
#             print(f"Маршрут изменен на {new_route}.")
#         else:
#             print(f"{self.model} на земле. Маршрут изменен на {new_route}, но самолет еще не в полете.")
#
#     def display_info(self):
#         '''Отобразить информацию'''
#         state = "в полете" if self.flight else "на земле"
#         route_info = f"Маршрут: {self.route}" if self.route else "Маршрут не задан"
#         print(f"Модель: {self.model}\nКоличество мест: {self.seats}\nСостояние: {state}\n{route_info}")
#
#
# class Passenger:
#     '''Пассажир'''
#     def __init__(self, name, ticket_number=None, destination=None):
#         self.name = name
#         self.ticket_number = ticket_number
#         self.destination = destination
#
#     def buy_ticket(self, ticket_number, destination):
#         '''Покупка билета'''
#         if self.ticket_number is None:
#             self.ticket_number = ticket_number
#             self.destination = destination
#             print(f"Пассажир {self.name} купил билет номер {self.ticket_number} до {self.destination}.")
#         else:
#             print(f"Пассажир {self.name} уже имеет билет номер {self.ticket_number} до {self.destination}.")
#
#     def cancel_booking(self):
#         '''Отмена бронирования'''
#         if self.ticket_number is not None:
#             print(f"Пассажир {self.name} отменил билет номер {self.ticket_number} до {self.destination}.")
#             self.ticket_number = None
#             self.destination = None
#         else:
#             print(f"У пассажира {self.name} нет активного бронирования.")
#
#     def display_info(self):
#         if self.ticket_number is not None:
#             print(f"Имя: {self.name}\nНомер билета: {self.ticket_number}\nМесто назначения: {self.destination}")
#         else:
#             print(f"Имя: {self.name}\nБилет не куплен")
#
#
# class Ticket:
#     '''Билет'''
#     def __init__(self, ticket_number, passenger_info, destination):
#         self.ticket_number = ticket_number
#         self.passenger_info = passenger_info
#         self.destination = destination
#
#     def display_info(self):
#         print(f"Номер билета: {self.ticket_number}")
#         print(f"Информация о пассажире: {self.passenger_info}")
#         print(f"Место назначения: {self.destination}")
#
#
# # Примеры использования:
# print("Пример использования класса Aircraft:")
#
# aircraft = Aircraft("Боинг 747", 416)
# aircraft.display_info()
# aircraft.take_off()
# aircraft.change_route("Бишкек - Москва")
# aircraft.display_info()
# aircraft.land()
# aircraft.display_info()
#
# print("\nПример использования класса Passenger:")
#
# passenger = Passenger("Иван Иванович")
# passenger.display_info()
# passenger.buy_ticket("12345", "Москва")
# passenger.display_info()
# passenger.cancel_booking()
# passenger.display_info()
#
# print("\nПример использования класса Ticket:")
#
# ticket1 = Ticket("123456", "Иван Иванович", "Москва")
# ticket1.display_info()


# class Project:
#     '''Проект'''
#
#     def __init__(self, name, description, deadline, current_project_status, list_participants=None):
#         self.name = name
#         self.description = description
#         self.deadline = deadline
#         self.current_project_status = current_project_status
#         self.list_participants = list_participants if list_participants is not None else []
#
#     def change_status(self, new_status):
#         '''Проверка статуса'''
#         valid_statuses = ['Не начат', 'В процессе', 'Завершен']
#         if new_status in valid_statuses:
#             self.current_project_status = new_status
#         else:
#             print(f"Некорректный статус: {new_status}. Допустимые статусы: {', '.join(valid_statuses)}")
#
#     def add_participant(self, participant):
#         '''Добавление участника'''
#         if participant not in self.list_participants:
#             self.list_participants.append(participant)
#         else:
#             print(f"{participant} уже является участником этого проекта.")
#
#     def remove_participant(self, participant):
#         '''Удаление участника'''
#         if participant in self.list_participants:
#             self.list_participants.remove(participant)
#                '''Удаление участника'''
#         if participant in self.list_participants:
#             self.list_participants.remove(participant)
#         else:
#             print(f"{participant} не является участником этого проекта.")
#
#     def display_info(self):
#         '''Отобразить информацию'''
#         print("Название проекта:", self.name)
#         print("Описание:", self.description)
#         print("Срок:", self.deadline)
#         print("Статус:", self.current_project_status)
#         print("Участники:", ", ".join(self.list_participants))
#
# # Пример использования:
# project = Project("Новый вебсайт", "Разработка нового вебсайта компании", "2024-12-31", "Не начат")
# project.add_participant("Алиса")
# project.add_participant("Бобсан")
# project.display_info()
# project.change_status("В процессе")
# project.remove_participant("Алиса")
# project.display_info()


# class ProjectMember:
#     '''Участник проекта'''
#     def __init__(self, name, role, responsibility, status=None):
#         self.name = name
#         self.role = role
#         self.responsibility = responsibility
#         self.status = status
#
#     def change_status(self, new_status):
#         '''Проверка статуса'''
#         self.status = new_status
#
#
#     def display_info(self):
#         '''Отобразить информацию'''
#         print("Имя:", self.name)
#         print("Роль:", self.role)
#         print("Ответственность:", self.responsibility)
#         print("Статус:", self.status)
# # Пример для класса ProjectManager
# member1 = ProjectMember("Иванов Иван", "Разработчик", "Разработка пользовательского интерфейса")
# member1.display_info()
# member1.change_status("Неактивен")
# member1.display_info()


# class Task:
#     '''Представления задачи в проекте'''
#     def __init__(self, title, description, status='Не начата', assignee=None):
#         self.title = title
#         self.description = description
#         self.status = status
#         self.assignee = assignee
#
#     def change_status(self, new_status):
#         '''Изменение статуса выполнения задачи'''
#         self.status = new_status
#         print(f"Статус задачи '{self.title}' изменен на '{self.status}'.")
#
#     def assign(self, assignee):
#         '''Назначение ответственного участника'''
#         self.assignee = assignee
#         print(f"Задача '{self.title}' назначена на {self.assignee}.")
#
#     def display_info(self):
#         '''Отображение информации о задаче'''
#         assignee_info = f"Ответственный участник: {self.assignee}" if self.assignee else "Ответственный участник не назначен"
#         print(f"Название: {self.title}\nОписание: {self.description}\nСтатус: {self.status}\n{assignee_info}")
#
#
# # Пример использования:
# task1 = Task("Разработка интерфейса", "Создать пользовательский интерфейс для нового приложения.")
# task1.display_info()
# task1.change_status("В процессе")
# task1.assign("Алеша")
# task1.display_info()
# task1.change_status("Завершена")
# task1.display_info()
#
# task2 = Task("Написание документации", "Создать техническую документацию для проекта.")
# task2.display_info()
# task2.assign("Маша")
# task2.change_status("Начата")
# task2.display_info()

# class Task:
#     '''Класс для представления задачи в проекте'''
#     def __init__(self, title, description, status='Не начата', assignee=None):
#         self.title = title
#         self.description = description
#         self.status = status
#         self.assignee = assignee
#
#     def change_status(self, new_status):
#         '''Изменение статуса выполнения задачи'''
#         self.status = new_status
#         print(f"Статус задачи '{self.title}' изменен на '{self.status}'.")
#
#     def assign(self, assignee):
#         '''Назначение ответственного участника'''
#         self.assignee = assignee
#         print(f"Задача '{self.title}' назначена на {self.assignee}.")
#
#     def display_info(self):
#         '''Отображение информации о задаче'''
#         assignee_info = f"Ответственный участник: {self.assignee}" if self.assignee else "Ответственный участник не назначен"
#         print(f"Название: {self.title}\nОписание: {self.description}\nСтатус: {self.status}\n{assignee_info}")
#
#
# class Project:
#     '''Класс для представления проекта'''
#     def __init__(self, name):
#         self.name = name
#         self.tasks = []
#         self.participants = []
#
#     def add_task(self, task):
#         '''Добавление задачи в проект'''
#         self.tasks.append(task)
#         print(f"Задача '{task.title}' добавлена в проект '{self.name}'.")
#
#     def add_participant(self, participant):
#         '''Добавление участника в проект'''
#         self.participants.append(participant)
#         print(f"Участник '{participant}' добавлен в проект '{self.name}'.")
#
#     def display_info(self):
#         '''Отображение информации о проекте'''
#         print(f"Проект: {self.name}")
#         print("Участники:")
#         for participant in self.participants:
#             print(f" - {participant}")
#         print("Задачи:")
#         for task in self.tasks:
#             task.display_info()
#
#
# class ProjectManager:
#     '''Класс для управления проектами'''
#     def __init__(self):
#         self.projects = {}
#
#     def create_project(self, project_name):
#         '''Создание нового проекта'''
#         if project_name not in self.projects:
#             self.projects[project_name] = Project(project_name)
#             print(f"Проект '{project_name}' создан.")
#         else:
#             print(f"Проект с названием '{project_name}' уже существует.")
#
#     def add_task_to_project(self, project_name, task):
#         '''Добавление задачи в проект'''
#         if project_name in self.projects:
#             self.projects[project_name].add_task(task)
#         else:
#             print(f"Проект с названием '{project_name}' не найден.")
#
#     def add_participant_to_project(self, project_name, participant):
#         '''Добавление участника в проект'''
#         if project_name in self.projects:
#             self.projects[project_name].add_participant(participant)
#         else:
#             print(f"Проект с названием '{project_name}' не найден.")
#
#     def change_task_status(self, project_name, task_title, new_status):
#         '''Изменение статуса задачи в проекте'''
#         if project_name in self.projects:
#             project = self.projects[project_name]
#             for task in project.tasks:
#                 if task.title == task_title:
#                     task.change_status(new_status)
#                     return
#             print(f"Задача с названием '{task_title}' не найдена в проекте '{project_name}'.")
#         else:
#             print(f"Проект с названием '{project_name}' не найден.")
#
#     def display_project_info(self, project_name):
#         '''Отображение информации о проекте'''
#         if project_name in self.projects:
#             self.projects[project_name].display_info()
#         else:
#             print(f"Проект с названием '{project_name}' не найден.")
#
#
# # Пример использования:
# manager = ProjectManager()
# manager.create_project("Разработка ПО")
# manager.add_participant_to_project("Разработка ПО", "Иван Иванович")
# manager.add_participant_to_project("Разработка ПО", "Мария Иванова")
#
# task1 = Task("Разработка интерфейса", "Создать пользовательский интерфейс для нового приложения.")
# manager.add_task_to_project("Разработка ПО", task1)
#
# task2 = Task("Написание документации", "Создать техническую документацию для проекта.")
# manager.add_task_to_project("Разработка ПО", task2)
#
# manager.display_project_info("Разработка ПО")
#
# manager.change_task_status("Разработка ПО", "Разработка интерфейса", "В процессе")
# manager.display_project_info("Разработка ПО")


