class Counter:
    def __init__(self):
        self.value = 0  # Внутренняя переменная для подсчета количества операций
        self.opened = False  # Флаг, указывающий на открытие ресурса

    def add(self):
        self.value += 1  # Увеличиваем счетчик при каждом вызове метода add()

    def __enter__(self):
        if self.opened:
            raise RuntimeError("Ресурс уже открыт")  # Вызываем исключение, если ресурс уже открыт
        self.opened = True  # Устанавливаем флаг открытия ресурса
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.opened = False  # Сбрасываем флаг открытия ресурса при выходе из контекста
        if exc_type:
            return False  # Возвращаем False, чтобы исключение продолжило всплывать
        if self.value > 0:
            print("Необходимо завершить работу с объектом в блоке try-with-resources.")
            return False  # Возвращаем False, чтобы исключение продолжило всплывать
        return True  # Возвращаем True, чтобы исключение было подавлено, если все в порядке


class AnimalRegistry:
    def __init__(self):
        self.animals = []  # Список зарегистрированных животных
        self.counter = Counter()  # Экземпляр счетчика операций

    def add_animal(self, name, animal_type, commands):
        """
        Добавляет новое животное в реестр.

        :param name: Имя животного
        :param animal_type: Тип животного (кошка, собака, хомяк)
        :param commands: Список команд, которые выполняет животное
        """
        animal = None
        if animal_type.lower() == 'кошка':
            animal = Cat(name, commands)
        elif animal_type.lower() == 'собака':
            animal = Dog(name, commands)
        elif animal_type.lower() == 'хомяк':
            animal = Hamster(name, commands)
        else:
            print(f"Неизвестный тип животного: {animal_type}")
            return

        if not commands or any(not cmd.strip() for cmd in commands):
            print("Ошибка: Команды не могут быть пустыми.")
            return

        self.animals.append(animal)
        print(f"Животное {name} добавлено в реестр.")
        self.counter.add()  # Увеличиваем счетчик при добавлении нового животного

    def list_commands(self, name):
        """
        Выводит список команд для заданного животного.

        :param name: Имя животного
        """
        found = False
        for animal in self.animals:
            if animal.name == name:
                print(f"Список команд для животного {name}: {animal.commands}")
                found = True
                break
        if not found:
            print(f"Животное с именем {name} не найдено в реестре.")

    def teach_command(self, name, new_command):
        """
        Обучает животное новой команде.

        :param name: Имя животного
        :param new_command: Новая команда для обучения
        """
        found = False
        for animal in self.animals:
            if animal.name == name:
                animal.teach_command(new_command)
                found = True
                break
        if not found:
            print(f"Животное с именем {name} не найдено в реестре.")

    def print_registry(self):
        """
        Выводит в консоль весь реестр зарегистрированных животных.
        """
        print("Реестр домашних животных:")
        for animal in self.animals:
            print(f"{animal.name} ({type(animal).__name__}) - Команды: {animal.commands}")


class Animal:
    def __init__(self, name, commands):
        self.name = name  # Имя животного
        self.commands = commands  # Список команд, которые выполняет животное

    def teach_command(self, new_command):
        """
        Добавляет новую команду для животного.

        :param new_command: Новая команда для обучения
        """
        self.commands.append(new_command)  # Добавляем новую команду в список


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Hamster(Animal):
    pass


# Главная программа с навигацией по меню
def main():
    registry = AnimalRegistry()  # Создаем экземпляр реестра животных

    while True:
        print("\nМеню:")
        print("1. Завести новое животное")
        print("2. Просмотреть список команд")
        print("3. Обучить животное новым командам")
        print("4. Вывести реестр животных")
        print("5. Выйти из программы")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            try:
                name = input("Введите имя животного: ")
                animal_type = input("Введите тип животного (кошка, собака, хомяк): ")
                commands = input("Введите команды, через запятую: ").split(',')
                with registry.counter:
                    registry.add_animal(name, animal_type, commands)
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            name = input("Введите имя животного: ")
            registry.list_commands(name)

        elif choice == '3':
            name = input("Введите имя животного: ")
            new_command = input("Введите новую команду: ")
            registry.teach_command(name, new_command)

        elif choice == '4':
            registry.print_registry()

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    main()
