import re
import time

from Library.excel_lib import ReadExcel
from Library.config import Config


class CabsModule:
    read_xl = ReadExcel()
    Cabs_Locator = read_xl.read_locators(Config.CABS_LOCATORS_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def outstation_oneway_radio_button(self):
        locator = self.Cabs_Locator["outstation_oneway_radio_button"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def from_textfield(self, enter_from_textfield):
        locator = self.Cabs_Locator["from_textfield"]
        self.driver.find_element(*locator).send_keys(enter_from_textfield)
        time.sleep(2)

    def from_autosuggestion(self):
        locator = self.Cabs_Locator["from_autosuggestion"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def to_textfield(self, enter_to_textfield):
        locator = self.Cabs_Locator["to_textfield"]
        self.driver.find_element(*locator).send_keys(enter_to_textfield)
        time.sleep(2)

    def to_autosuggestion(self):
        locator = self.Cabs_Locator["to_autosuggestion"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def pickup_date(self):
        locator = self.Cabs_Locator["pickup_date"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def select_date(self):
        locator = self.Cabs_Locator["select_date"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def pickup_time(self):
        locator = self.Cabs_Locator["pickup_time"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def select_time(self):
        locator = self.Cabs_Locator["select_time"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def search_button(self):
        locator = self.Cabs_Locator["search_button"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def select_cab(self):
        locator = self.Cabs_Locator["select_cab"]
        self.driver.find_element(*locator).click()
        time.sleep(4)

    def pickup_location(self, enter_pickup_location):
        locator = self.Cabs_Locator["pickup_location"]
        self.driver.find_element(*locator).send_keys(enter_pickup_location)
        time.sleep(2)

    def location_autosuggestion(self):
        locator = self.Cabs_Locator["location_autosuggestion"]
        self.driver.find_element(*locator).click()
        time.sleep(5)

    def full_name(self, enter_full_name):
        locator = self.Cabs_Locator["full_name"]
        self.driver.find_element(*locator).send_keys(enter_full_name)
        time.sleep(2)

    def mobile_number(self, enter_mobile_number):
        if isinstance(enter_mobile_number, float):
            enter_mobile_number = str(int(enter_mobile_number))
        assert len(enter_mobile_number) == 10
        locator = self.Cabs_Locator["mobile_number"]
        self.driver.find_element(*locator).send_keys(enter_mobile_number)
        time.sleep(2)

    def email(self, enter_email):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, enter_email)
        assert result != [], "invalid email"
        locator = self.Cabs_Locator["email"]
        self.driver.find_element(*locator).send_keys(enter_email)
        time.sleep(2)

    def paynow_radiobutton(self):
        locator = self.Cabs_Locator["paynow_radiobutton"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def payment_button(self):
        locator = self.Cabs_Locator["payment_button"]
        self.driver.find_element(*locator).click()
        time.sleep(2)
