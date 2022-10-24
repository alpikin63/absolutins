import allure
from selene.api import Element, query, browser

from core.common import BaseElement


class Calendar(BaseElement):
    """Поле для ввода даты."""

    def __init__(
            self, locator_or_element_or_by: str | tuple | Element,
    ):
        super().__init__(locator_or_element_or_by)

    def set(self, value: str):
        with allure.step(f'Ввести значение: {value}'):
            js_id = self._element.get(query.attribute('id'))
            browser.driver.execute_script(f'$("#{js_id}").datepicker("setDate", "{value}")')
