import re

from behave import *

from pages.account_page import AccountPage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.orders_page import OrdersPage
from pages.product_page import ProductPage
from utils.assertion import assert_equals, assert_contains
from utils.screenshot import take_screenshot

use_step_matcher("parse")


@when('User navigates to the {product} product page')
def step_impl(context, product):
    account_page = AccountPage(context.browser)
    home_page = HomePage(context.browser)
    account_page.click_logo_button()
    home_page.click_product(product)


@step('User validates that a {discount} discount is applied')
def step_impl(context, discount):
    product_page = ProductPage(context.browser)
    discount = discount.replace("%", "")
    regular_price = product_page.get_regular_price()
    discounted_price = product_page.get_discounted_price()
    regular_price = re.sub("[^0-9.]", "", regular_price)
    discounted_price = re.sub("[^0-9.]", "", discounted_price)
    reg_price = float(regular_price)
    disc_price = float(discounted_price)
    discount_percentage = (reg_price - disc_price) / reg_price * 100
    actual_discount = round(discount_percentage)
    assert_equals(actual_discount, int(discount))


@step('User selects size {size}')
def step_impl(context, size):
    product_page = ProductPage(context.browser)
    product_page.select_size(size)


@step('User sets the product quantity to {amount}')
def step_impl(context, amount):
    product_page = ProductPage(context.browser)
    product_page.set_quantity(amount)


@step("User adds the item to the cart")
def step_impl(context):
    product_page = ProductPage(context.browser)
    product_page.click_add_to_cart_button()


@step("User proceeds to checkout")
def step_impl(context):
    product_page = ProductPage(context.browser)
    cart_page = CartPage(context.browser)
    product_page.click_proceed_to_checkout_button()
    cart_page.click_proceed_to_checkout_button()


@step("User continues with preselected address")
def step_impl(context):
    cart_page = CartPage(context.browser)
    cart_page.click_continue_address_button()


@step('User chooses the {delivery} delivery method')
def step_impl(context, delivery):
    cart_page = CartPage(context.browser)
    cart_page.select_delivery_option(delivery)


@step("User continues with selected delivery option")
def step_impl(context):
    cart_page = CartPage(context.browser)
    cart_page.click_continue_delivery_option_button()


@step('User opts for {option} and confirms the order')
def step_impl(context, option):
    cart_page = CartPage(context.browser)
    cart_page.select_payment_method(option)
    cart_page.click_terms_of_service_checkbox()
    cart_page.click_place_order_button()
    total_order_price = cart_page.get_total_price()
    reference_number = cart_page.get_order_reference()

    take_screenshot(context.browser, "order confirmation")
    context.total_order_price = total_order_price
    context.reference_number = reference_number


@then("User navigates to the order history")
def step_impl(context):
    cart_page = CartPage(context.browser)
    account_page = AccountPage(context.browser)
    cart_page.click_account_button()
    account_page.navigate_to_order_history()


@step('User verifies the order is listed with status {status}, correct price and reference')
def step_impl(context, status):
    orders_page = OrdersPage(context.browser)
    assert_equals(orders_page.get_first_order_status(), status)
    assert_equals(orders_page.get_first_order_total_price(), context.total_order_price)
    assert_contains(context.reference_number, orders_page.get_first_order_reference())
