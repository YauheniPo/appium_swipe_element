from AppiumLibrary import AppiumLibrary
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from robot.libraries.BuiltIn import BuiltIn

SCROLL_MEASURE_PERCENT = {'LONG': 90, 'MIDDLE': 50, 'SHORT': 20}


def get_swipe_params(way, measure_percent, params):
    swipe_prams = {'start_x': None, 'start_y': None, 'end_x': None, 'end_y': None}
    if way == 'UP' or way == 'DOWN':
        swipe_prams['start_x'] = swipe_prams['end_x'] = params.get('x') + params.get('width') / 2
        if way == 'UP':
            swipe_prams['start_y'] = params.get('y') + params.get('height') / 100 * 16
            swipe_prams['end_y'] = params.get('y') + params.get('height') / 100 * measure_percent
        if way == 'DOWN':
            swipe_prams['start_y'] = params.get('y') + params.get('height') / 100 * measure_percent
            swipe_prams['end_y'] = params.get('y') + params.get('height') / 100 * 5
    if way == 'LEFT' or way == 'RIGHT':
        swipe_prams['start_y'] = swipe_prams['end_y'] = params.get('y') + params.get('height') / 2
        if way == 'LEFT':
            swipe_prams['start_x'] = params.get('x') + params.get('width') / 100 * 5
            swipe_prams['end_x'] = params.get('x') + params.get('width') / 100 * measure_percent
        if way == 'RIGHT':
            swipe_prams['start_x'] = params.get('x') + params.get('width') / 100 * measure_percent
            swipe_prams['end_x'] = params.get('x') + params.get('width') / 100 * 5
    return swipe_prams


class AppiumHelper(AppiumLibrary):
    built_in = BuiltIn()

    def _browser(self) -> WebDriver:
        return self._current_application()

    def _get_element(self, locator) -> WebElement:
        return self._browser().find_element(locator)

    def get_page_source(self) -> str:
        return self._browser().page_source

    def get_element_params(self, element_locator):
        """
        Get element parameters like a dict:
            - The location of the element in the renderable canvas:
                - x
                - y
            - The size of the element:
                - height
                - width
        """
        if element_locator:
            element = self._get_element(element_locator)
            element_location = element.location
            element_size = element.size
        else:
            element_location = {'x': 0, 'y': 0}
            element_size = self._browser().get_window_size()
        return {**element_location, **element_size}

    def scroll_element(self, way: str, measure="LONG", element_locator=None, duration=2200):
        measure_percent = SCROLL_MEASURE_PERCENT.get(measure)
        element_params = self.get_element_params(element_locator)
        scrolling_element_params = get_swipe_params(way=way.upper(),
                                                    measure_percent=measure_percent,
                                                    params=element_params)
        self._browser().swipe(**scrolling_element_params, duration=duration)
