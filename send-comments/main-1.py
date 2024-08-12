from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

def extractUrlToApi(url):
    # Parsing URL
    parsed_url = urlparse(url)
    
    # Mengambil path dan memecahnya berdasarkan '/'
    path_parts = parsed_url.path.split('/')
    
    # Mendapatkan shop_domain dan product_key
    if len(path_parts) > 2:
        shop_domain = path_parts[1]
        product_key = path_parts[2]
    else:
        shop_domain = ''
        product_key = ''
    
    return {
        'shop_domain': shop_domain,
        'product_key': product_key
    }

def startScraping(chrome_driver_path, keyword_search):
    chrome_options = Options()
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    try:
        driver.get("https://www.tokopedia.com")
        wait = WebDriverWait(driver, 20)
        search_box = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'exxxdg63')))
        search_box.send_keys(keyword_search)
        search_box.send_keys(Keys.ENTER)
        search_toko = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="btnSRPShopTab"]')))
        search_toko.click()

    finally:
        driver.quit()


chrome_driver_path = "D:\\Programs\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
keyword_search = "Lenovo Official"

startScraping(chrome_driver_path, keyword_search)