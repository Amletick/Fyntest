class Counter:
    def __init__(self):
        self.value = 0
        self.opened = False

    def add(self):
        self.value += 1

    def __enter__(self):
        if self.opened:
            raise RuntimeError("Ресурс уже открыт")
        self.opened = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.opened = False
        if exc_type:
            return False
        if self.value > 0:
            print("Необходимо завершить работу с объектом в блоке try-with-resources.")
            return False
        return True


class AnimalRegistry:
    def __init__(self):
        self.animals = []
        self.counter = Counter()

    def add_animal(self, name, animal_type, commands):
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
        self.counter.add()

    def list_commands(self, name):
        found = False
        for animal in self.animals:
            if animal.name == name:
                print(f"Список команд для животного {name}: {animal.commands}")
                found = True
                break
        if not found:
            print(f"Животное с именем {name} не найдено в реестре.")

    def teach_command(self, name, new_command):
        found = False
        for animal in self.animals:
            if animal.name == name:
                animal.teach_command(new_command)
                found = True
                break
        if not found:
            print(f"Животное с именем {name} не найдено в реестре.")

    def print_registry(self):
        print("Реестр домашних животных:")
        for animal in self.animals:
            print(f"{animal.name} ({type(animal).__name__}) - Команды: {animal.commands}")


class Animal:
    def __init__(self, name, commands):
        self.name = name
        self.commands = commands

    def teach_command(self, new_command):
        self.commands.append(new_command)


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class Hamster(Animal):
    pass


# Главная программа с навигацией по меню
def main():
    registry = AnimalRegistry()

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
