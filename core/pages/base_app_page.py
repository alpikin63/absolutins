import allure

from core.common import BasePage
from core.data.page_data import PageData
from core.pages.custom_elements.loader import Loader


class BaseAppPage(BasePage):

    def __init__(self):
        super().__init__()
        self._loader = Loader()  # иконка загрузки на страницах

    def assure_current_page_url_contains_text(self, page_data: PageData, timeout: int = 4) -> None:
        super().assure_current_page_url_contains_text(page_data.relative_url, timeout=timeout)
