import random
import string
import time
from datetime import datetime
from typing import Any

from faker import Faker

garbage = '"¦O>”,“”‘~!@#$%^&*()?>,./<][/*<!–”\",“${code}”;–>\\"'
ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
cyrillic_letters = ru + RU


class BaseRandomizer:

    def __init__(self):
        self._faker = Faker('ru-RU')

    @staticmethod
    def unique_postfix() -> str:
        """Получить уникальный постфикс."""
        return str(time.time_ns())

    def large_text(self) -> str:
        """Получить большой текст."""
        return self._faker.text(max_nb_chars=2000)

    @staticmethod
    def random_number(start: int = 1000, end: int = 9999999) -> int:
        """Получить случайное целое число."""
        return random.randint(start, end)

    def random_ru_string(self, char_count: int) -> str:
        """Получить случайный набор кириллических символов."""
        return self.random_id(length=char_count, is_latin=False, only_letters=True)

    def random_en_string(self, char_count: int) -> str:
        """Получить случайный набор латинских символов."""
        return self.random_id(length=char_count, is_latin=True, only_letters=True)

    def random_id(
            self,
            length: int = 8,
            strong: bool = False,
            is_latin: bool = True,
            only_letters: bool = False,
            only_digits: bool = False,
            is_unique: bool = False
    ) -> str:
        """Получить случайный идентификатор, состоящий из цифр, букв или символов."""
        def mix_string(text: str) -> str:
            """Перемешать строку."""
            list_of_char = list(text)
            random.shuffle(list_of_char)
            return ''.join(list_of_char)

        rid = ''
        for _ in range(length):
            rid += random.choice(
                mix_string(
                    ('!@#$%^&*()_-+=' if strong else '')
                    + ((string.ascii_letters if is_latin else cyrillic_letters) if not only_digits else '')
                    + (string.digits if not only_letters else '')
                )
            )
        if is_unique:
            rid = f'{rid}{self.unique_postfix()}'
        return rid

    def generate_name(self, mask: str) -> str:
        """Сгенерировать случайное имя с префиксом."""
        return '{mask}_{stamp}_{rand_id}'.format(mask=mask, stamp=int(datetime.now().timestamp()),
                                                 rand_id=self.random_id(length=6))

    def guid(self) -> str:
        return self._faker.uuid4()

    def md5(self) -> str:
        return self._faker.md5()

    @staticmethod
    def random_choice(array) -> Any:
        """Получить случайный элемент из списка."""
        return random.choice(array)

    @staticmethod
    def random_choice_with_exclude(iterable, exclude=None) -> Any:
        """Получить случайный элемент из списка с возможностью задать список исключаемых элементов."""
        if not isinstance(exclude, list):
            exclude = [exclude]
        return random.choice([item for item in iterable if item not in exclude])

    def email(self) -> str:
        return self._faker.ascii_free_email()

    def unique_test_email(self, prefix: str = 'autotest') -> str:
        """Получить уникальное значение email."""
        return f'{prefix}_{self.unique_postfix()}@test.ru'

    def phone(self, mask: str = None) -> str:
        """Get random phone number.

        Return phone in random format or in format according to specified mask.
        :param mask: string in format like '+7(9xx)-xxx-xx-xx' where X will be replaced to random digit
        :return: random phone as string
        """
        if mask:
            return ''.join([(c, str(random.randint(0, 9)))[c == 'x'] for c in mask])
        return self._faker.phone_number()
