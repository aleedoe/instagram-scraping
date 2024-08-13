from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def startScraping(chrome_driver_path, user_name, password_user):
    chrome_options = Options()
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(20)
    try:
        driver.get("https://www.instagram.com/")
        wait = WebDriverWait(driver, 30)  # Perpanjang waktu tunggu hingga 30 detik

        # Menunggu hingga form login terlihat
        wait.until(EC.visibility_of_element_located((By.ID, "loginForm")))

        # Menginputkan username
        username_input = driver.find_element(By.NAME, "username")
        username_input.send_keys(user_name)

        # Menginputkan password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password_user)

        # Menekan tombol "Log in"
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        time.sleep(5)

        # Tunggu hingga elemen pencarian terlihat dan klik
        search_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Search"]')))
        search_item.click()
        # time.sleep(5)

        #target the search input field
        searchbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
        searchbox.clear()

        #search for the @handle or keyword
        keyword = "@dr.richard_lee"
        searchbox.send_keys(keyword)
        
        # Check if the keyword starts with "@"
        if keyword.startswith("@"):
            # Remove the "@" symbol
            keyword = keyword[1:]
            
        # Wait until the first result appears in the search dropdown
        first_result = wait.until(EC.presence_of_element_located((By.XPATH, f'//span[text()="{keyword}"]')))

        # Re-locate the element before clicking to avoid StaleElementReferenceException
        first_result = driver.find_element(By.XPATH, f'//span[text()="{keyword}"]')
        first_result.click()
        time.sleep(5)
        
        # Get the initial page height
        initial_height = driver.execute_script("return document.body.scrollHeight")

        while True:

            # Cari semua div dengan class tertentu
            div_containers = driver.find_elements(By.CSS_SELECTOR, 'div._ac7v.xras4av.xgc1b0m.xat24cr.xzboxd6')

            # Loop melalui setiap div dan cari <a> di dalamnya
            for div_container in div_containers:
                a_tags = div_container.find_elements(By.TAG_NAME, "a")

                # Loop melalui setiap <a> dan klik satu per satu
                for a_tag in a_tags:
                    try:
                        # Scroll ke elemen <a> untuk memastikan terlihat
                        driver.execute_script("arguments[0].scrollIntoView();", a_tag)

                        # Tunggu elemen <a> dapat di-klik
                        wait.until(EC.element_to_be_clickable(a_tag))

                        # Klik elemen <a>
                        a_tag.click()

                        ###### comment section #######
                        comment_value = "@klinik_kecantikan_athena ULTAH! @dr.richard_lee mau live tgl 19 Agustus jualan produk baru!"

                        # Menginputkan comment
                        comment_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[aria-label="Add a comment…"]')))
                        comment_input.send_keys(comment_value)
                        comment_input.send_keys(Keys.ENTER)

                        close_item = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'svg[aria-label="Close"]')))
                        close_item.click()
                        ###### /.comment section #######

                        # Tunggu hingga kembali ke halaman sebelumnya
                        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div._ac7v.xras4av.xgc1b0m.xat24cr.xzboxd6')))

                    except Exception as e:
                        print(f"Gagal klik <a> dengan href {a_tag.get_attribute('href')}: {e}")
                        continue


            
            # Scroll down to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for a moment to allow new content to load (adjust as needed)
            time.sleep(3)

            # Get the current page height
            current_height = driver.execute_script("return document.body.scrollHeight")

            if current_height == initial_height:
                break  # Exit the loop when you can't scroll further

            initial_height = current_height  # Update the initial height for the next iteration
        

    finally:
        driver.quit()

chrome_driver_path = "D:\\Programs\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
user_name = "aleedoe_"
password_user = "kasurrusak"

startScraping(chrome_driver_path, user_name, password_user)
