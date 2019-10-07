from selenium.webdriver.common.by import By


class WomanAndManLocators:

    #WomanCollection
    woman_bookmark = (By.ID, "womanCategoryName")
    man_bookmark = (By.ID, "manCategoryName")
    campaign_bookmark = (By.ID, "campaignCategoryName")
    lookbook_bookmark = (By.ID, "autumn-winter-lookbookCategoryName")
    woman_outerwear_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[1]/a")
    dresses_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[2]/a")
    woman_jeans_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[3]/a")
    woman_tshirt_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[4]/a")
    woman_sweatshirts_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[5]/a")
    woman_sweaters_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[6]/a")
    woman_blouses_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[7]/a")
    woman_shirts_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[8]/a")
    woman_skirts_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[9]/a")
    woman_trousers_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[10]/a")
    woman_shorts_link = (By.XPATH, "//ul[@id='womanCategory']/li[1]/ul/li[11]/a")

    #WomanAccessories

    woman_shoes_link = (By.XPATH, "//*[@id='womanCategory']/li[2]/ul/li[1]/a")
    woman_bags_backpacks_link = (By.XPATH, "//*[@id='womanCategory']/li[2]/ul/li[2]/a")
    woman_lingerie_socks = (By.XPATH, "//*[@id='womanCategory']/li[2]/ul/li[3]/a")
    woman_glasses_link = (By.XPATH, "//*[@id='womanCategory']/li[2]/ul/li[4]/a")
    woman_belts_link = (By.XPATH, "//*[@id='womanCategory']/li[2]/ul/li[5]/a")
    woman_accessories_link = (By.XPATH, "//*[@id='womanCategory']/li[2]/ul/li[6]/a")
    woman_wallets_link = (By.XPATH, "//*[@id='womanCategory']/li[2]/ul/li[7]/a")
    woman_jewellery_link = (By.XPATH, "//*[@id='womanCategory']/li[2]/ul/li[8]/a")
    woman_hats_scarves_gloves_link = (By.XPATH, "//*[@id='womanCategory']/li[2]/ul/li[9]/a")

    #WomanSpecial

    woman_new_link = (By.XPATH, "//*[@id='womanCategory']/li[3]/ul/li[1]/a")
    woman_coming_soon_link = (By.XPATH, "//*[@id='womanCategory']/li[3]/ul/li[2]/a")
    woman_bestsellers_link = (By.XPATH, "//*[@id='womanCategory']/li[3]/ul/li[3]/a")
    woman_friends_link = (By.XPATH, "//*[@id='womanCategory']/li[3]/ul/li[4]/a")
    woman_eco_link = (By.XPATH, "//*[@id='womanCategory']/li[3]/ul/li[5]/a")
    woman_harry_link = (By.XPATH, "//*[@id='womanCategory']/li[3]/ul/li[6]/a")

    #ManCollection
    man_outwear_link = (By.XPATH, "//ul[@id='manCategory']/li[1]/ul/li[1]/a")
    man_sweatshirts_link = (By.XPATH, "//ul[@id='manCategory']/li[1]/ul/li[2]/a")
    man_jeans_link = (By.XPATH, "//ul[@id='manCategory']/li[1]/ul/li[3]/a")
    man_trousers_link = (By.XPATH, "//ul[@id='manCategory']/li[1]/ul/li[4]/a")
    man_tshirts_link = (By.XPATH, "//ul[@id='manCategory']/li[1]/ul/li[5]/a")
    man_polo_link = (By.XPATH, "//ul[@id='manCategory']/li[1]/ul/li[6]/a")
    man_shirts_link = (By.XPATH, "//ul[@id='manCategory']/li[1]/ul/li[7]/a")
    man_sweaters_link = (By.XPATH, "//ul[@id='manCategory']/li[1]/ul/li[8]/a")
    man_shorts_link = (By.XPATH, "//ul[@id='manCategory']/li[1]/ul/li[9]/a")


class NewsletterLocators:
    newsletter_input = (By.ID, "newsletterMailHomePage")
    newsletter_checkbox = (By.XPATH, "//*[@id='homePageNewsletter']/div/div[2]/label/span")
    sign_newsletter_button = (By.XPATH, "//*[@id='homePageNewsletter']/div/div[1]/button")
    error_incorrect_email = (By.ID, "newsletterMailHomePage-error")
    checkbox_unfilled = (By.ID, "newsletterTermsHome-error")


class CampaignLocators:
    campaign_link = (By.ID, "campaignCategoryName")
    campaign_listlink_1 = (By.XPATH, "//*[@id='campaignCategory']/li[1]/a")
    campaign_listlink_2 = (By.XPATH, "//*[@id='campaignCategory']/li[2]/a")
    campaign_listlink_3 = (By.XPATH, "//*[@id='campaignCategory']/li[3]/a")
    campaign_listlink_4 = (By.XPATH, "//*[@id='campaignCategory']/li[4]/a")


class LookbookLocators:
    lookbook_link = (By.ID, "campaignCategory")
    lookbook_listlink_1 = (By.XPATH, "//*[@id='autumn-winter-lookbookCategory']/li[1]/a")
    lookbook_listlink_2 = (By.XPATH, "//*[@id='autumn-winter-lookbookCategory']/li[2]/a")
    lookbook_listlink_3 = (By.XPATH, "//*[@id='autumn-winter-lookbookCategory']/li[3]/a")


class StoreLocator:

    store_locator_link = (By.ID, "storesCategoryName")
    city_input = (By.ID, "searchShopInput")
    search_city_button = (By.XPATH, "//*[@id='geoSearch'']/div/div/button")


