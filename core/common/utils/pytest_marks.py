import functools
import warnings

import allure
import pytest

# web browser
web_browser = pytest.mark.usefixtures('web_browser')
web_browser_for_class = pytest.mark.usefixtures('web_browser_for_class')

skip = pytest.mark.skipif(True, reason='Временно не запускаем')
not_ready = pytest.mark.skipif(True, reason='Тест находится в разработке')

serial = pytest.mark.serial  # запуск тестов последовательно
smoke = pytest.mark.smoke  # набор для smoke-тестирования
regress = pytest.mark.regress  # набор для regress-тестирования

data_provider = pytest.mark.parametrize  # параметризированные тесты
flaky = pytest.mark.flaky  # нестабильные тесты # params: reruns: int, reruns_delay: int
