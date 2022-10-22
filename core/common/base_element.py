from __future__ import annotations

from typing import Union

from selene.api import Element, be, command, s


class BaseElement:
    """Базовый класс кастомных элементов страницы."""

    def __init__(self, locator_or_element_or_by: Union[str, tuple, Element]):
        if isinstance(locator_or_element_or_by, (str, tuple)):
            self._element = s(locator_or_element_or_by)
        elif isinstance(locator_or_element_or_by, Element):
            self._element = locator_or_element_or_by
        else:
            raise TypeError('Wrong argument type')

    def waiting_to_be_visible(self, timeout: int = 4) -> BaseElement:
        self._element.with_(timeout=timeout).should(be.visible)
        return self

    def waiting_to_be_present(self, timeout: int = 4) -> BaseElement:
        self._element.with_(timeout=timeout).should(be.present)
        return self

    def is_visible(self, timeout: int = 4) -> bool:
        return self._element.with_(timeout=timeout).wait_until(be.visible)

    @property
    def element(self) -> Element:
        return self._element

    def scroll_to(self) -> BaseElement:
        self._element.with_(timeout=10).should(be.present).perform(command.js.scroll_into_view)
        return self

    def click(self) -> BaseElement:
        self._element.click()
        return self
