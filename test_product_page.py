from .pages.product_page import ProductPage
import pytest


# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0
# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/

# @pytest.mark.parametrize('offer', range(10))
@pytest.mark.parametrize('offer', [0, 1, 2, 3, 4, 5, 6, 
                                   pytest.param(7, marks=pytest.mark.xfail(
                                                   reason="BUG: product name in success message not correct")),
                                   8, 9],
                        )
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = ProductPage(browser, link)
    page.open()
    print(f"\n{link}")
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_in_basket()


@pytest.mark.skip(reason="negativ test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip(reason="negativ test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappearance_of_message()