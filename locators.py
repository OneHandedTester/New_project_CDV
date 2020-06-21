from selenium.webdriver.common.by import By

class HomePageLocators():
    LOGO_EL = (By. XPATH, '//*[@class="img-responsive"]')
    OVERLAPS_EL = (By. XPATH, '//*[@class="nav navbar-nav"]')
    CATEGORIES_EL = (By. XPATH, '//*[@id="categories_block_left_content"]')
    HEAD1_EL = (By. XPATH, '//*[@id="center_column"]/div[2]/h1')
    HEAD2_EL = (By. XPATH, '//*[@id="center_column"]/div[2]/h4[2]')
    HEAD3_EL = (By. XPATH, '//*[@id="tabela_flat"]')
    PHOTO_EL = (By. CSS_SELECTOR, '.rte > p:nth-child(8) > a:nth-child(1) > span:nth-child(1) > img:nth-child(1)')


class LoginPageLocators():
    EMAIL_INPUT = (By.XPATH, '//*[@id="email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="passwd"]')
    LOG_ON_TO_USER_BTN = (By.XPATH, '//*[@id="SubmitLogin"]')
    MY_ACCOUNT_LINK = (By. XPATH, "//*[contains(text(), 'Moje Konto')]")
    ERROR_COM = (By. XPATH, '//*[@class="error"]')

class RegisterPageLocators():
    COOKIES_BTN = (By. XPATH, '//*[@id="cookiesClose"]')
    LOG_AND_REGISTER_BTN = (By. XPATH, '//*[@id="header_user_info"]/a')
    NEW_EMAIL_INPUT = (By. XPATH, '//*[@id="email_create"]')
    REGISTER_BTN = (By. XPATH, '//*[@id="SubmitCreate"]')
    ERROR_COM = (By. XPATH, '//*[@id="create_account_error"]')
    ERROR2_COM= (By. XPATH, "//*[contains(text(), 'Nieprawidłowy adres e-mail')]")
    BAD_POPUP_BTN = (By. ID, 'smwpRejectionButton')
    BAD_POPUP2_BTN = (By. XPATH, '// *[ @ id = "bhr-popup-form"] / div / div / div[2] / div[4]')

# VIEW ACCOUNT CREATION - FORM:
    FIRSTNAME_INPUT = (By. ID, "customer_firstname")
    LASTNAME_INPUT = (By. ID, "customer_lastname")
    EMAIL_INPUT = (By. ID, "email")
    PASSWORD_INPUT = (By. ID, "passwd")
    NEWSLETTER_CHECKBOX = (By. ID, "newsletter")
    COMPANY_NAME_INPUT = (By. ID, "company")
    NIP_INPUT = (By. NAME, "vat_number")
    ADDRESS1_INPUT = (By. ID, "address1")
    ADDRESS2_INPUT = (By. ID, "address2")
    POSTCODE_INPUT = (By. ID, "postcode")
    CITY_INPUT = (By. ID, "city")
    COUNTRY_ID_SELECTLIST = (By. ID, "id_country")
    OTHERS_INFORMATIONS_INPUT = (By. ID, "other")
    PHONE_NUMBER_INPUT = (By. ID, "phone")
    MY_ADRESS_NAME_INPUT = (By. ID, "alias")

class ResultsPageLocators():
    COOKIES_BTN = (By. XPATH, '//*[@id="cookiesClose"]')
    SEARCHER_INPUT = (By. XPATH, '//*[@id="search_query_top"]')
    SEARCH_RESULTS_LIST = (By. XPATH, '//*[@id="index"]/div[3]/ul')
    RANDOM_PRODUCT1_EL = (By. XPATH, "//*[text()= 'Dodaj']")
    PRODUCTS_LIST = (By. XPATH, '//*[@id="product_list"]')
    RANDOM_PRODUCT2_EL = (By. XPATH, '//*[@id="product_list"]/li[2]/div[2]/div/a[1]')
    RANDOM_PRODUCT3_EL = (By. XPATH, '//*[@id="product_list"]/li[3]/div[2]/div/a[1]')
    RANDOM_PRODUCT4_EL = (By. XPATH, '//*[@id="product_list"]/li[4]/div[2]/div/a[1]')
    SELECT_LIST_EL = (By. XPATH, '//*[@id="selectPrductSort"]/option[6]')
    ORDER_BTN = (By. XPATH, '//*[@id="button_order_cart"]')
    ORDER_PRODUCT_LIST = (By. XPATH, '//*[@class="product_counter"]')
    SUM_BRUTTO_EL = (By. XPATH, '//*[@id="total_product"]')
    SUM_SHIPPING_EL = (By. XPATH, '//*[@id="total_shipping"]')
    SUM_TOTAL_PRICE = (By. XPATH, '//html/body/div[1]/div[2]/div/div[2]/form/fieldset/div/div[1]/div[1]/div[1]/div[1]/table/tbody/tr[5]/td[2]/span')
    CLEAR_BASKET_BTN = (By. XPATH, '//*[@id="myBtn"]')
    CLEAR_BASKET_ACCEPT_BTN = (By. XPATH, '//*[@id="modal-confirm"]')







