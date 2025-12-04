import os
import pytest
import allure
from pytest import fixture, hookimpl
from playwright.sync_api import sync_playwright
from page_objects.insiderApplication import App


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        playwright.selectors.set_test_id_attribute("data-id")
        yield playwright

@fixture(scope='session', params=['chromium', 'firefox'], ids=['chromium', 'firefox'])
def get_browser(get_playwright, request):
    
    browser = request.param
    os.environ['PWBROWSER']=browser
    headless = request.config.getini('headless')
    
    if headless == 'True':
        headless = True
    else:
        headless = False
        
    if browser == 'chromium':
        bro = get_playwright.chromium.launch(headless = headless, slow_mo = 2000)
    elif browser == 'firefox':
        bro = get_playwright.firefox.launch(headless = headless, slow_mo = 2000)
    elif browser == 'webkit':
        bro = get_playwright.webkit.launch(headless = headless)
    else:
        assert False, 'unsupported browser type'
    
    yield bro
    bro.close()
    del os.environ['PWBROWSER']


@fixture(scope='session')
def desktop_app(get_browser, request):
    base_url = request.config.getini('base_url')
    app = App(get_browser, base_url=base_url)
    app.goto('/')
    yield app
    app.close()
    
@fixture(scope='session', params=['iPhone 15', 'Pixel 7'])
def mobile_app(get_playwright, get_browser, request):
    if os.environ['PWBROWSER'] == 'firefox':
        pytest.skip()
    base_url = request.config.getini('base_url')
    device = request.param
    device_config = get_playwright.devices.get(device)

    if device_config is not None:
        device_config.update(**device_config)
    else:
        device_config = device

    app = App(get_browser, base_url= base_url, **device_config)
    app.goto('/')
    yield app
    app.close()

@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    #result.when = "setup" >> "call" >> "teardown"
    setattr(item, f'result_{result.when}', result)

@fixture(scope='function', autouse=True)
def make_screenshots(request):
    yield
    if request.node.result_call.failed:
        for arg in request.node.funcargs.values():
            if isinstance(arg, App):
                allure.attach(body=arg.page.screenshot(),
                              name='screenshot',
                              attachment_type=allure.attachment_type.PNG)
                
def pytest_addoption(parser):
    parser.addini('headless', help = "run browser in headless mode")