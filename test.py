from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# opening browser
browser = webdriver.Chrome()
# url
browser.get("http://www.saucedemo.com")
# user inputs
username = browser.find_element_by_id("user-name")
password = browser.find_element_by_id("password")
submit   = browser.find_element_by_id("login-button")
username.send_keys("standard_user")
password.send_keys("secret_sauce")
# submit button
submit.click()
wait = WebDriverWait( browser, 5 )
# adding items to cart
cart1=browser.find_element_by_xpath('''//*[@id="inventory_container"]/div/div[1]/div[3]/button''')
cart1.click()

cart2=browser.find_element_by_xpath('''//*[@id="inventory_container"]/div/div[2]/div[3]/button''')
cart2.click()

cart3=browser.find_element_by_xpath('''//*[@id="inventory_container"]/div/div[3]/div[3]/button''')
cart3.click()
# checkout
checkout=browser.find_element_by_xpath('''//*[@id="shopping_cart_container"]''')
checkout.click()
checkoutf=browser.find_element_by_xpath('''//*[@id="cart_contents_container"]/div/div[2]/a[2]''')
checkoutf.click()

