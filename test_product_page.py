from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest, time


catalog = "http://selenium1py.pythonanywhere.com/catalogue"
book1 = "/coders-at-work_207"
book2 = "/the-city-and-the-stars_95"

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        user = str(time.time()) + "@fakemail.org", "preved_ʕ•ᴥ•ʔ_medved"
        page = ProductPage(browser, catalog)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user(*user)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = f"{catalog}{book1}"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = f"{catalog}{book1}"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_product_in_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('offer', [0, 1, 2, 3, 4, 5, 6, 
                                   pytest.param(7, marks=pytest.mark.xfail(
                                                   reason="BUG: product name in success message not correct")),
                                   8, 9],
                        )
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"{catalog}{book1}/?promo=offer{offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_in_basket()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = f"{catalog}{book2}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = f"{catalog}{book2}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()


@pytest.mark.skip(reason="negativ test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = f"{catalog}{book1}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = f"{catalog}{book1}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = f"{catalog}{book2}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip(reason="negativ test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = f"{catalog}{book1}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappearance_of_message()
