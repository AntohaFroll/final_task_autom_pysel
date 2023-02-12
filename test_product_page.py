from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.find_product_name()
    product_page.find_product_price()
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    basket_page = BasketPage(browser, url=browser.current_url)
    product_page.should_be_product_in_basket()
    basket_page.find_product_name_in_basket()
    basket_page.find_product_price_in_basket()
    assert product_page.find_product_name().text == basket_page.find_product_name_in_basket().text, \
        "Wrong product added to basket"
    assert product_page.find_product_price().text == basket_page.find_product_price_in_basket().text, \
        "Wrong product price"
