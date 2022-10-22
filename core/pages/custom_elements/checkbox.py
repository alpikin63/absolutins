import allure
from selene.api import Element, be, query, have
from waiting import wait

from core.common import BaseElement


class Checkbox(BaseElement):
    """Чекбокс."""

    def __init__(
            self, locator_or_element_or_by: str | tuple | Element,
            input_loc: str = 'input'
    ):
        super().__init__(locator_or_element_or_by)
        self._input = self._element.s(input_loc)

    def set(self, status: bool) -> 'Checkbox':
        current_status = self.is_checked()
        if status != current_status:
            self._element.click()
        return self

    def is_checked(self) -> bool:
        return bool(self._input.get(query.js_property('checked')))

    def is_enabled(self) -> bool:
        return self._element.matching(be.enabled)

    def assure_checkbox_status(self, value: bool):
        wait(lambda: self.is_checked() == value, timeout_seconds=2,
             waiting_for=f'Чекбокс {"не выбран" if value else "выбран"}')

    @allure.step('Проверить, что свитчер активен')
    def assure_switcher_is_active(self):
        self._element.should(have.attribute('class', 'switch checked'))

    @allure.step('Проверить, что свитчер неактивен')
    def assure_switcher_is_not_active(self):
        self._element.should(have.no.attribute('class', 'switch checked'))

    @property
    def label(self) -> str:
        return self._element.get(query.text)
