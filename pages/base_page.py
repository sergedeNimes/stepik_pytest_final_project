class BasePage():
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url

	def open(self):
		self.browser.get(self.url)

	'''
	def test_add_to_cart(browser):
	    page = ProductPage(url="", browser)   # инициализируем объект Page Object
	    page.open()                           # открываем страницу в браузере
	    page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
	    page.add_product_to_cart()            # жмем кнопку добавить в корзину 
	    page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом
    '''