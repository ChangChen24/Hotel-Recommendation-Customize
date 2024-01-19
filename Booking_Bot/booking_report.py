from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
class BookingReport:
    def __int__(self, boxes_selection_element):
        self.boxes_selection_element = boxes_selection_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_selection_element.find_elements(By.CLASS_NAME, 'sr_property_block')

    def pull_titles(self):
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(
                By.CLASS_NAME, 'sr-hotel__name'
            ).get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element_by_class_name(
                'bui-price-display__value'
            ).get_attribute('innerHTML').strip()
            hotel_score = deal_box.get_attribute(
                'data-score'
            ).strip()




