import allure
from selene.api import Element, be
from selene.core.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from core.common import BaseElement
from core.common.utils.service_utils import print_and_logging


class Loader(BaseElement):
    """Кастомный элемент для иконки прогрузки."""

    def __init__(
            self,
            locator_or_element_or_by: str | tuple | Element = '.loader'
    ):
        super().__init__(locator_or_element_or_by)

    def __call__(self, start_timeout: int = 1, end_timeout: int = 120):
        self._start_timeout = start_timeout
        self._end_timeout = end_timeout
        self._wait()

    @allure.step('Ожидание прогрузки страницы')
    def _wait(self):
        try:
            self._element.with_(timeout=self._start_timeout).should(be.visible)
            try:
                self._element.with_(timeout=self._end_timeout).should(be.hidden)
            except TimeoutException:
                raise AssertionError(f'Прогрузка не завершилась за {self._end_timeout} секунд.')
        except (NoSuchElementException, StaleElementReferenceException, TimeoutException) as e:
            print_and_logging(f'Иконка прогрузки не отображалась. Ошибка:\n{e}')
        return self
