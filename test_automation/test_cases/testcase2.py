from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver

from test_automation.BASE.basepage import BaseDriver
from test_automation.PAGES.launchpage import LaunchPage
from test_automation.PAGES.searchResultPage import SearchResults
from test_automation.test_cases.utility import Test_uti


# LAUNCHING THE BROWSER AND OPENING THE TRAVEL WEBSITE:

@pytest.mark.usefixtures('setup')
class Test_script:
    def test_function(self):
        # launch browser and launching the website

        # provide depart from location
        lp = LaunchPage(self.driver)
        lp.departFrom('new delhi')
        sleep(2)

        # provide going to location
        lp.goingTo('new')
        sleep(4)
        # to select departure date
        lp.departDate('20/01/2023')
        sleep(2)
        # click on flight search button
        lp.searchButton()
        sleep(2)

        self.driver.set_page_load_timeout(100)
        self.driver.get(
            'https://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=10%2F01%2F2023&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&unqvaldesktop=1012116628059')
        # ele = self.driver.find_element(By.XPATH, "(//p[@class='font-lightgrey bold'])[2]")
        # self.wait.until(EC.visibility_of(ele))

        # to handle dynamic scroll button
        bp = BaseDriver(self.driver)
        bp.scrollButton()
        sleep(2)

        # select the filter one stop
        sp = SearchResults(self.driver)
        sp.filter(2)

        all_stops = lp.wait_untill_presence_all_element_located(By.XPATH, "//span[@class='dotted-borderbtm']")
        # verify that filtered results having 1 stop
        tu=Test_uti()
        tu.test_verify(all_stops,'1 stop')


        sleep(4)

# PROVIDE DEPART FROM LOCATION
# class Test_script:
#         depart_from=self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@name='flight_origin'])[1]")))
#         depart_from.click()
#         depart_from.send_keys('new delhi')
#         depart_from.send_keys(Keys.ENTER)
#
#     #PROVIDE GOING TO LOCATION
#         going_to=self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@id='BE_flight_arrival_city'])")))
#         going_to.click()
#         going_to.send_keys('new')
#         search_results=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='viewport']/div/div/li")))
#         for result in search_results:
#             if 'New York (LGA)' in result.text:
#                 result.click()
#                 break
#
#     #TO SELECT THE DEPARTURE DATE
#         self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_date']"))).click()
#         all_dates=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))\
#             .find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
#         for date in all_dates:
#             if date.get_attribute('data-date')=='22/01/2023':
#                 date.click()
#                 break
#
#     #CLICK ON FLIGHT SEARCH BUTTON
#         self.driver.find_element(By.XPATH,"//input[@id='BE_flight_flsearch_btn' and @value='Search Flights']").click()
#         sleep(4)
#         self.driver.set_page_load_timeout(100)
#         self.driver.get('https://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin=DEL&originCountry=IN&destination=BOM&destinationCountry=IN&flight_depart_date=10%2F01%2F2023&ADT=1&CHD=0&INF=0&class=Economy&source=fresco-home&unqvaldesktop=1012116628059')
#         ele=self.driver.find_element(By.XPATH,"(//p[@class='font-lightgrey bold'])[2]")
#         self.wait.until(EC.visibility_of(ele))
#
#     #TO HANDLE DYNAMIC SCROLL BUTTON
#         previous=driver.execute_script("return document.body.scrollHeight")
#         while True:
#             self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
#             sleep(3)
#             new_height=self.driver.execute_script('return document.body.scrollHeight')
#             if new_height==previous:
#                 break
#             previous=new_height
#         sleep(3)
#
#     #SELECT THE FILTER ONE STOP
#         self.driver.find_element(By.XPATH,"(//p[@class='font-lightgrey bold'])[2]").click()
#         all_stops=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//span[@class='dotted-borderbtm']")))
#         print(len(all_stops))
#         for i in all_stops:
#             assert i.text == "1 Stop"
#             print('assert pass')
