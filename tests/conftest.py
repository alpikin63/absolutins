import json
import os

import allure
import pytest
from dotmap import DotMap
from selene.common.helpers import on_error_return_false
from selene.support.shared import config as selene_config, browser
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from core.common.enum import BrowserName
from settings import settings
from .fixtures import *  # noqa


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=BrowserName.CHROME)
    parser.addoption('--browser_ver', action='store', default='')
    parser.addoption('--remote', action='store_true', default=False)
    parser.addoption('--hub', action='store', default='172.17.21.145')
    parser.addoption('--port', action='store', default='4444')
    parser.addoption('--download_path', action='store', default=f'{os.path.join(os.getcwd(), "download")}')


@pytest.fixture(scope='session', autouse=True)
def config(request):
    browser_name = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    hub = request.config.getoption('--hub')
    port = request.config.getoption('--port')
    remote = request.config.getoption('--remote')
    download_path = request.config.getoption('--download_path')
    settings.stand.configuration = DotMap(
        {
            'browser': browser_name,
            'version': version,
            'hub': hub,
            'port': port,
            'remote': remote,
            'download_path': download_path,
        }
    )
    return settings.stand.configuration


def get_chrome_options(config):
    options = ChromeOptions()
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-notifications')
    options.add_argument('--kiosk-printing')
    options.add_argument(f'--print-to-pdf={config["download_path"]}')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-gpu')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-web-security')
    app_state = {
        'recentDestinations': [
            {
                'id': 'Save as PDF',
                'origin': 'local',
                'account': '',
            }
        ],
        'selectedDestinationId': 'Save as PDF',
        'version': 2
    }

    options.add_experimental_option('prefs', {
        'download.default_directory': config['download_path'] if not config['remote'] else '/home/selenium/Downloads',
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'printing.print_preview_sticky_settings.appState': json.dumps(app_state),
        'plugins.always_open_pdf_externally': True,
        'safebrowsing.enabled': True
    })
    return options


def create_local_driver(config):
    driver_manager = ChromeDriverManager()
    options = get_chrome_options(config)
    driver = webdriver.Chrome(executable_path=driver_manager.install(), options=options)
    return driver


def setup_browser(config):

    driver = create_local_driver(config)
    # config selene browser
    selene_config.save_screenshot_on_failure = False
    selene_config.save_page_source_on_failure = False
    selene_config.timeout = 4
    selene_config.driver = driver
    return


@pytest.fixture(scope='function')
def web_browser(config):
    setup_browser(config)
    yield
    # make screenshot and get logs
    from pprint import pformat

    allure.attach(browser.driver.get_screenshot_as_png(), name='failure-screenshot',
                  attachment_type=allure.attachment_type.PNG)
    allure.attach(pformat(browser.driver.get_log('browser')), name='js-console-log',
                  attachment_type=allure.attachment_type.TEXT)
    allure.attach(pformat(browser.driver.get_log('driver')), name='driver-log',
                  attachment_type=allure.attachment_type.TEXT)

    selene_config.reset_driver()


def pytest_exception_interact():
    from pprint import pformat
    # if driver is running, make screenshot and get logs
    if on_error_return_false(lambda: browser.driver.title is not None):
        allure.attach(browser.driver.get_screenshot_as_png(), name='failure-screenshot',
                      attachment_type=allure.attachment_type.PNG)
        allure.attach(pformat(browser.driver.get_log('browser')), name='js-console-log',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(pformat(browser.driver.get_log('driver')), name='driver-log',
                      attachment_type=allure.attachment_type.TEXT)
