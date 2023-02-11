import time

import pytest
from sdbqawithdbapi.src.pages.HomePage import HomePage
from sdbqawithdbapi.src.pages.Header import Header
from sdbqawithdbapi.src.pages.CartPage import CartPage
from sdbqawithdbapi.src.pages.CheckoutPage import CheckoutPage
from sdbqawithdbapi.src.pages.OrderReceivedPage import OrderReceivedPage
from sdbqawithdbapi.src.configs.generic_configs import GenericConfigs


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        home_p = HomePage(self.driver)  # self.driver comes from this fixture --> @pytest.mark.usefixtures('init_driver')
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)


        # go to home page
        home_p.go_to_home_page()

        # add 1 item to cart
        home_p.click_first_add_to_cart_button()
        home_p.click_view_cart()

        # make sure the cart is updated before going to cart
        header.wait_until_cart_item_count(1)

        # go to cart
        header.click_on_cart_on_right_header()

        product_names = cart_p.get_all_product_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"

        # apply free coupon SSQA100
        coupon_code = GenericConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)

        # select free shipping
        cart_p.click_on_local_pickup_radio_btn()

        # click on checkout
        cart_p.click_on_proceed_to_checkout()

        # fill in form
        checkout_p.fill_in_billing_info()

        # click on place order
        #checkout_p.click_place_order()

        # verify order is received
        order_received_p.verify_order_received_page_loaded()

        # verify order is recorded in db (via SQL or via api)