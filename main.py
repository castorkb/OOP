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
class MyTime:
    def __init__(self, time_str):
        time_str = time_str.split(':')
        self.hours = int(time_str[0])
        self.minutes = int(time_str[1])

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __int__(self):
        return self.hours * 60 + self.minutes


time_test = MyTime("12:22")
print(time_test.hours)
print(time_test.minutes)
print(time_test)
print(int(time_test))



