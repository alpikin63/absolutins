import random
from datetime import datetime, timedelta
from typing import Any

from dateutil.parser import parse
from zoneinfo import ZoneInfo

from core.common.base_randomizer import BaseRandomizer

__all__ = ['data_helper']


class DataHelper(BaseRandomizer):

    @staticmethod
    def get_random_date(start: datetime, end: datetime = None, format_string: str = '%d.%m.%Y'):
        """Return a random datetime between two datetime objects."""
        if end is None:
            end = datetime.now()
        delta = end - start
        random_value = random.choice(range(delta.days)) if delta.days > 0 else random.choice(range(delta.days, 0))
        _date = start + timedelta(random_value)
        return _date.strftime(format_string)

    @staticmethod
    def get_current_date(format_string: str = '%d.%m.%Y') -> str:
        return datetime.now().strftime(format_string)

    @staticmethod
    def get_next_date(format_string: str = '%d.%m.%Y') -> str:
        """Получить следующую дату от текущего дня."""
        return (datetime.now() + timedelta(days=1)).strftime(format_string)

    @staticmethod
    def parse_date(date_string: str, **kwargs) -> datetime:
        """
        Парсит строку с датой и переводит в объект datetime.

        Внимание! Если дата в формате "dd.mm.YYYY", то нужно указывать аргумент dayfirst=True
        timezone issue: https://www.linux.org.ru/forum/development/13640755
        :param date_string: str
        :return: datetime
        """
        return parse(date_string, **kwargs).replace(tzinfo=ZoneInfo('Europe/Moscow'))

    def reformat_date(self, date_string: str, format_string: str = '%d.%m.%Y %H:%M:%S', **kwargs: Any) -> str:
        """
        Принимает строку с датой, переформатирует в указанный формат.

        Внимание! Если дата в формате "dd.mm.YYYY", то нужно указывать аргумент dayfirst=True
        """
        return self.parse_date(date_string, **kwargs).strftime(format_string)


data_helper = DataHelper()
