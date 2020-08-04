from .pages.product_page import ProductPage
import pytest


# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0

# @pytest.mark.parametrize('offer', range(10))
@pytest.mark.parametrize('offer', [0, 1, 2, 3, 4, 5, 6, 
                                   pytest.param(7, marks=pytest.mark.xfail(
                                                   reason="BUG: product name in basket not correct")),
                                   8, 9],
                        )
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = ProductPage(browser, link)
    page.open()
    print(f"\n{link}")
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_in_basket()
