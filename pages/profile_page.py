
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfilePageLocators()



    def click_order_history_button(self):
        self.wait_invisibility_of_element(self.locators.modal_window)
        self.wait_clickable_of_element(self.locators.order_hystory_button)
        self.click_on_element(self.locators.order_hystory_button)
        self.wait_invisibility_of_element(self.locators.profile_form)

    def find_order_in_order_history(self, order_number):
        locator = self.locators.get_order_locator(order_number)

        return self.wait_visibility_of_element(locator)

    def log_out_from_profile(self):
        self.wait_invisibility_of_element(self.locators.modal_window)
        self.wait_clickable_of_element(self.locators.exit_button)
        self.click_on_element(self.locators.exit_button)

    def check_profile_form_invisible(self):
        return self.wait_invisibility_of_element(self.locators.profile_form)




