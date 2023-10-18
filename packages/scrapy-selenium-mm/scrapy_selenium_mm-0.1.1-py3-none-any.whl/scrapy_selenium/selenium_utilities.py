from typing import (List, Dict, Union, Callable, Any)
from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver import Firefox
from selenium.webdriver import Ie
from selenium.webdriver import Safari
from selenium.webdriver.support.ui import WebDriverWait
from scrapy.http import HtmlResponse

from .http import SeleniumRequest
import time

SeleniumWebDriver = Union[Chrome, Firefox, Safari, Ie, Edge]
wait_until_type = Callable[[SeleniumWebDriver], Any]
script_val = Union[int, str, wait_until_type]
ScriptDict = Dict[str, script_val]
ScriptDictList = List[ScriptDict]

class SeleniumUtilities(object):

  @classmethod
  def handle_selenium_scripts(cls, driver: SeleniumWebDriver, script_dict_list: ScriptDictList) -> SeleniumWebDriver:
    """
    The `handle_selenium_scripts` function executes a series of scripts using a Selenium
    driver, with optional waiting and pausing between each script.

    :param cls: The `cls` parameter is a reference to the class itself. It is used
    when defining a class method
    :param driver: The `driver` parameter is an instance of a Selenium WebDriver.
    It is used to interact with a web browser and perform actions such as
    navigating to URLs, clicking elements, and executing JavaScript code
    :type driver: SeleniumWebDriver
    :param script_dict_list: The `script_dict_list` parameter is a list of dictionaries. Each
    dictionary represents a script to be executed by the Selenium driver. Each
    dictionary in the list can have the following keys: script, wait, pause
    :type script_dict_list: ScriptDictList
    :return: The method is returning the driver object.
    """
    for item in script_dict_list:
        if not item.get('script'):
            break
        driver.execute_script(item.get('script'))
        if item.get('wait'):
            WebDriverWait(driver, item.get('wait')).until(item.get('wait_until'))
        if item.get('pause'):
            time.sleep(item.get('pause'))
    return driver

  @classmethod
  def generate_scrapy_response(cls, driver: SeleniumWebDriver, request: SeleniumRequest) -> HtmlResponse:
    """
    The function `generate_scrapy_response` generates a Scrapy `HtmlResponse`
    object from a Selenium driver and request.

    :param cls: The `cls` parameter is a reference to the class itself. In this
    case, it is used as a decorator for the method, indicating that it is a class
    method
    :param driver: The `driver` parameter is an instance of a web driver, such as
    `webdriver.Chrome()` or `webdriver.Firefox()`. It is used to interact with the
    web page and retrieve its source code
    :type driver: SeleniumWebDriver
    :param request: The `request` parameter is an instance of the
    `SeleniumRequest` class. It represents a request made by Scrapy to a website
    using Selenium. It contains information such as the URL to be requested,
    headers, cookies, and other metadata
    :type request: SeleniumRequest
    :return: The method is returning an instance of the `HtmlResponse` class.
    """
    body = str.encode(driver.page_source)
    request.meta.update({'driver': driver})
    return HtmlResponse(
        driver.current_url,
        body=body,
        encoding='utf-8',
        request=request
    )

