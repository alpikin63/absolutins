from pprint import pformat
from typing import Union

import allure


class PrintMixin:
    """Распечатка свойств объекта в читаемом виде."""

    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append('{class_name}.{key}={value}'.format(class_name=self.__class__.__name__.lower(),
                                                          key=key, value=self.__dict__[key]))
        return '\n'.join(sb)

    def __repr__(self):
        return self.__str__()


def wait_seconds(second: Union[int, float] = 1) -> None:
    """Обертка под time.sleep."""
    from time import sleep

    sleep(second)


def format_text_error(error: str | list[str]):
    """Возвращает отформатированный текст ошибки."""
    text_part = 'Обнаружены ошибки %s шт:\n%s'
    if isinstance(error, list):
        return text_part % (len(error), '\n'.join(error))
    return error


def screenshot_page():
    """Сделать скриншот страницы."""
    from selene.api import browser

    allure.attach(browser.driver.get_screenshot_as_png(), 'Screenshot', allure.attachment_type.PNG)


def print_and_logging(text: str | list[str], text_name: str = 'Комментарий'):
    """Объединены функции print и allure.attach."""
    import logging

    logger = logging.getLogger(__name__)
    if not isinstance(text, str):
        text = pformat(text)
    allure.attach(text, text_name, allure.attachment_type.TEXT)
    logger.info(text)


def action_on_error(
        text: str | list[str] = 'Проверка завершилась с ошибкой',
        title: str = 'Error',
        is_scr: bool = True
):
    """
    Вызывает исключение и печатает ошибку.

    :param text: {str | list[str]} текст ошибки или список с текстами ошибок.
    :param title: {str} название пункта в отчете
    :param is_scr: {bool}: делать ли скриншот
    """
    if is_scr:
        screenshot_page()
    text = format_text_error(text)
    print_and_logging(text, text_name=title)
    raise AssertionError(text)


def on_attribute_error_return_false(no_args_predicate):
    """Возвращает False, если вызывается исключение AttributeError.

    Пример использования:
        on_attribute_error_return_false(lambda: instance.attribute)
    """
    try:
        return no_args_predicate()
    except AttributeError:
        return False


def on_index_error_return_none(no_args_predicate):
    """Возвращает None, если вызывается исключение IndexError.

    Полезна при работе с данными возвращаемыми из бд.
    Пример использования:
        on_index_error_return_none(lambda: result[0])
    """
    try:
        return no_args_predicate()
    except IndexError:
        return None
