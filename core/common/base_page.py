import allure
from selene.api import browser, have
from selene.core.exceptions import TimeoutException
from waiting import TimeoutExpired, wait


class BasePage:
    """
    Базовый класс, непривязанный к тестируемой системе.

    Должен содержать методы и параметры, которые не относятся к тестируемой системе напрямую.
    """

    def __init__(self):
        pass

    @staticmethod
    @allure.step('Проверить текст в адресе страницы')
    def assure_current_page_url_contains_text(expected_text: str, timeout: int = 4):
        try:
            browser.with_(timeout=timeout).should(have.url_containing(expected_text))
        except TimeoutException as e:
            raise AssertionError(f'Не удалось перейти на страницу:\n{e}')

    @staticmethod
    @allure.step('Обновить страницу')
    def refresh():
        browser.driver.refresh()

    @staticmethod
    @allure.step('Получить текущий адрес страницы')
    def get_current_url() -> str:
        return browser.driver.current_url

    def navigate(self, url: str):
        with allure.step(f'Переход по адресу: "{url}"'):
            browser.open(url)
        return self

    @staticmethod
    @allure.step('Открыть новую вкладку в браузере')
    def open_new_tab():
        browser.execute_script('window.open()')

    @staticmethod
    @allure.step('Перейти к новой вкладке в браузере')
    def switch_to_another_tab():
        current_tab = browser.driver.current_window_handle
        try:
            wait(lambda: len(browser.driver.window_handles) == 2, timeout_seconds=5)
            all_tabs = browser.driver.window_handles
            all_tabs.remove(current_tab)
            new_tab = all_tabs[0]
            browser.driver.switch_to.window(new_tab)
        except TimeoutExpired:
            raise AssertionError('Two tabs must be present')

    @staticmethod
    @allure.step('Закрыть все вкладки, кроме текущей')
    def close_other_tabs():
        all_tabs = browser.driver.window_handles
        current_tab = browser.driver.current_window_handle
        all_tabs.remove(current_tab)
        for tab in all_tabs:
            browser.driver.switch_to.window(tab)
            browser.close()
        browser.driver.switch_to.window(current_tab)

    @staticmethod
    @allure.step('Принять предупреждение')
    def accept_alert():
        browser.driver.switch_to.alert.accept()

    @staticmethod
    @allure.step('Скролл к началу страницы')
    def scroll_to_page_up():
        browser.driver().execute_script('window.scrollTo(0, 0)')

    @staticmethod
    @allure.step('Скролл к концу страницы')
    def scroll_to_page_down():
        browser.driver().execute_script('window.scrollTo(10000, 10000)')
