from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    def click_ingredient_in_constructor(self, ingredient):
        self.scroll_to_element(self.locators.get_ingredient_locator(ingredient))
        self.wait_clickable_of_element(self.locators.get_ingredient_locator(ingredient))
        self.click_on_element(self.locators.get_ingredient_locator(ingredient))

    def check_modal_window_appear(self):
        return self.wait_visibility_of_element(self.locators.ingredient_modal_window)

    def close_modal_window(self):
        self.wait_visibility_of_element(self.locators.modal_close)
        self.click_on_element(self.locators.modal_close)
        return self.wait_invisibility_of_element(self.locators.modal_close)

    def drag_ingredient_from_constructor_to_burger_constructor(self, ingredient):
        self.scroll_to_element(self.locators.get_ingredient_locator(ingredient))
        self.wait_clickable_of_element(self.locators.get_ingredient_locator(ingredient))

        self.move_element(self.locators.get_ingredient_locator(ingredient), self.locators.burger_constructor)


    def drag_ingredient_by_link(self, ingredient_id):
        self.scroll_to_element(self.locators.get_ingredient_by_href(ingredient_id))
        self.wait_clickable_of_element(self.locators.get_ingredient_by_href(ingredient_id))
        self.move_element(self.locators.get_ingredient_by_href(ingredient_id), self.locators.burger_constructor)

    def check_count_ingredients(self, ingredient_id):
        self.find_element(self.locators.get_counter_locator(ingredient_id))
        return self.get_text(self.locators.get_counter_locator(ingredient_id))

    def check_modal_window_order_id_appear(self):
        self.click_on_element(self.locators.make_order_button)
        return self.wait_visibility_of_element(self.locators.modal_window_order_id)


