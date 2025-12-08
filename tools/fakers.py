from faker import Faker

class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker.
    """
    def __init__(self, faker: Faker):
        """
        :param faker: Экземпляр класса Faker, который будет использоваться для генерации данных.
        """
        self.faker = faker

    def integer(self, start: int = 100, end: int= 10000) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.

        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное целое число.
        """
        return self.faker.random_int(start, end)
    
    def user_name(self) -> str:
        """
        Генерирует случайный username.
        
        :return: Случайный username.
        """
        return self.faker.user_name()
    
    def first_name(self) -> str:
        """
        Генерирует случайный first name.
        
        :return: Случайный first name.
        """
        return self.faker.first_name()
    
    def last_name(self) -> str:
        """
        Генерирует случайный last name.
        
        :return: Случайный last name.
        """
        return self.faker.last_name()
    
    def email(self) -> str:
        """
        Генерирует случайный email.
        
        :return: Случайный email.
        """
        return self.faker.email()
    
    def password(self) -> str:
        """
        Генерирует случайный password.
        
        :return: Случайный password.
        """
        return self.faker.password()
    
    def phone(self) -> str:
        """
        Генерирует случайный номер телефона.
        
        :return: Случайный номер телефона.
        """
        return self.faker.phone_number()
    
    def user_status(self, start: int = 1000, end: int= 100000) -> int:
        """
        Генерирует случайное целое число в заданном диапазоне.

        :param start: Начало диапазона (включительно).
        :param end: Конец диапазона (включительно).
        :return: Случайное целое число.
        """
        return self.faker.random_int(start, end)
    
fake = Fake(faker=Faker())
    
