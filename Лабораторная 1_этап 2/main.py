import doctest
class Object:
    """Базовый класс для всех объектов."""

    def __init__(self, name: str, description: str = None):
        """Инициализировать новый объект.

        Args:
            name (str): Уникальное имя объекта.
            description (str, optional): Необязательное описание объекта.
        """
        self.name = name
        self.description = description

    def get_name(self) -> str:
        """Возвращает имя объекта."""
        return self.name

    def set_description(self, description: str) -> None:
        """Устанавливает описание объекта.

        Args:
            description (str): Описание объекта.
        """
        self.description = description

    def print_info(self) -> None:
        """Выводит информацию об объекте."""
        print(f"Имя: {self.name}")
        if self.description:
            print(f"Описание: {self.description}")


class PhysicalObject(Object):
    """Класс для материальных объектов."""

    def __init__(self, name: str, description: str = None, mass: float = 0.0, volume: float = 0.0):
        """Инициализировать новый материальный объект.

        Args:
            name (str): Уникальное имя объекта.
            description (str, optional): Необязательное описание объекта.
            mass (float, optional): Масса объекта (в килограммах).
            volume (float, optional): Объем объекта (в кубических метрах).
        """
        super().__init__(name, description)
        self.mass = mass
        self.volume = volume

    def get_mass(self) -> float:
        """Возвращает массу объекта."""
        return self.mass

    def get_volume(self) -> float:
        """Возвращает объем объекта."""
        return self.volume

    def calculate_density(self) -> float:
        """Рассчитывает и возвращает плотность объекта."""
        return self.mass / self.volume

class NonPhysicalObject(Object):
    """Класс для нематериальных объектов."""

    def __init__(self, name: str, description: str = None, creator: str = None, date_created: str = None):
        """Инициализировать новый нематериальный объект.

        Args:
            name (str): Уникальное имя объекта.
            description (str, optional): Необязательное описание объекта.
            creator (str, optional): Создатель объекта.
            date_created (str, optional): Дата создания объекта.
        """
        super().__init__(name, description)
        self.creator = creator
        self.date_created = date_created

    def get_creator(self) -> str:
        """Возвращает создателя объекта."""
        return self.creator

    def get_date_created(self) -> str:
        """Возвращает дату создания объекта."""
        return self.date_created

    def delete(self) -> None:
        """Удаляет объект."""
        # Реализация удаления будет зависеть от конкретного приложения.
        pass


# Тестирование классов с помощью doctest
def load_tests(tests):
    tests.addTests(doctest.DocTestSuite(Object))
    tests.addTests(doctest.DocTestSuite(PhysicalObject))
    tests.addTests(doctest.DocTestSuite(NonPhysicalObject))
    return tests


if __name__ == "__main__":
    # Создание экземпляров классов
    table = PhysicalObject("Table", "Деревянный стол", 25.0, 0.5)
    tree = PhysicalObject("Tree", "Дуб", 1000.0, 10.0)
    stack = NonPhysicalObject("Stack", "Куча", "Python", "2008-03-10")

    # Вывод информации об объектах
    table.print_info()
    tree.print_info()
    stack.print_info()

    # Проверка методов
    assert table.get_name() == "Table"
    assert tree.get_mass() == 1000.0
    assert stack.get_creator() == "Python"
