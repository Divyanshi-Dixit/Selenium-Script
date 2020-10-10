from locator import *


class BasePage(object):
	def __init__(self, driver):
		self.driver = driver 

 class MainPage(BasePage):

 	def is_title_matches(self):
 		return "Python" in self.driver.title

 	def click_go_button(Self):
 		element = self.driver.find_element(^MainPageLocators.GO_BUTTON)
 		element.click()
class SearchPageResult(BasePage):

	def is_result_found(Self):
		return "No results found" not in self.driver.page_source