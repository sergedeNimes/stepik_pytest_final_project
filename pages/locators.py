from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")


class BasketPageLocators():
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, "#basket_totals")
    EMPTY_BASKET_TEXT = (By.XPATH, "//*[@id='content_inner']/p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")       # .alert-success strong
    COST_MESSAGE = (By.XPATH, "//*[@id='messages']/div[last()]/div/p/strong")   # .alert-info strong
