import time
import re
from behave import*
from selenium import webdriver

@given(u'User is able to launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(r"C:\Users\Revanth Kumar K\PycharmProjects\Goibibo_cabs\drivers\chromedriver.exe")
    context.driver.get(r"https://www.goibibo.com/cars/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)

@when(u'user is able to click on outstation one_way')
def click_on_outstation_one_way(context):
    context.driver.find_element("xpath", '(//span[@class="CustomRadioButtonUIstyles__Dot-sc-1ffkzia-2 hAzeQw"])[1]').click()
    time.sleep(2)


@then(u'user is able to enter "{from_location}" in from textfield')
def enter_from_textfield(context, from_location):
    context.driver.find_element("xpath", '//input[@id="downshift-1-input"]').send_keys(from_location)
    time.sleep(2)


@then(u'user is able to click on from autosuggestion')
def click_on_from_autosuggestion(context):
    context.driver.find_element("xpath", '//div[@id="downshift-1-item-0"]').click()
    time.sleep(2)


@then(u'user is able to enter "{to_location}" in to textfield')
def enter_to_textfield(context, to_location):
    context.driver.find_element("xpath", '(//input[@name="autosuggest"])[2]').send_keys(to_location)
    time.sleep(2)


@then(u'user is able to click on to autosuggestion')
def click_on_to_autosuggestion(context):
    context.driver.find_element("xpath", '(//li[@class="AutoSuggeststyles__ListItem-sc-1xb3zd-2 kOvBXW"])[1]').click()
    time.sleep(2)


@when(u'user is able to click on pickup date')
def click_on_pickup_date(context):
    context.driver.find_element("xpath", '(//span[@class="HomeSearchWidgetstyles__DateTxt-sc-1rvppov-7 eiggyI"])[1]').click()
    time.sleep(2)


@then(u'user is able to select the date')
def select_the_date(context):
    context.driver.find_element("xpath", '//span[text()="30"]').click()
    time.sleep(2)


@when(u'user is able to click on pickup time')
def click_on_pickup_time(context):
    context.driver.find_element("xpath", '(//span[@class="HomeSearchWidgetstyles__DateTxt-sc-1rvppov-7 eiggyI"])[2]').click()
    time.sleep(2)


@then(u'user is able to select time')
def select_time(context):
    context.driver.find_element("xpath", '//span[text()="05:00 PM"]').click()
    time.sleep(2)


@then(u'user is able to click on search cabs')
def click_on_search_cabs(context):
    context.driver.find_element("xpath", '//button[text()="SEARCH CABS"]').click()
    time.sleep(4)

@then(u'user is able to click on select button')
def click_on_select_button(context):
    context.driver.find_element("xpath", '(//div[@class="cabDtlhHeader"])[1]/../../..//button[@name="SELECT"]').click()
    time.sleep(2)


@then(u'user is able to enter "{pickup_location}" in pickup location textfield')
def pickup_location_textfield(context, pickup_location):
    context.driver.find_element("xpath", '(//input[@class="textInput"])[1]').send_keys(pickup_location)
    time.sleep(4)


@when(u'user is able to click on location autosuggestion')
def click_on_location_autosuggestion(context):
    context.driver.find_element("xpath", '(//p[@class="AutoSuggeststyles__MainTxt-sc-1xb3zd-4 fvzcbc"])[1]').click()
    time.sleep(4)

@then(u'user is able to enter "{full_name}" in full name textfield')
def enter_full_name_textfield(context, full_name):
    context.driver.find_element("xpath", '//input[@placeholder="Enter Full Name"]').send_keys(full_name)
    time.sleep(2)


@then(u'user is able to enter "{mobile_number}" in mobile number textfield')
def enter_mobile_number_textfield(context, mobile_number):
    context.driver.find_element("xpath", '//input[@placeholder="Enter Mobile Number"]').send_keys(mobile_number)
    time.sleep(2)


@then(u'user is able to enter "{email}" in email textfield')
def enter_email_textfield(context, email):
    context.driver.find_element("xpath", '//input[@placeholder="Enter Email"]').send_keys(email)
    time.sleep(2)


@then(u'user is able to click paynow button')
def click_paynow_button(context):
    context.driver.find_element("xpath", '(//label[@class="makeFlex spaceBetween"])[1]').click()
    time.sleep(4)


@then(u'user is able to click on payment button')
def click_on_payment_button(context):
    context.driver.find_element("id", 'paymentButton').click()
    time.sleep(4)
    context.driver.close()

