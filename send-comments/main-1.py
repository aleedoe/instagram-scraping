from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
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
        keyword = "@webzet.dev"
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
        time.sleep(8)
        
        # Get the initial page height
        initial_height = driver.execute_script("return document.body.scrollHeight")
        
        # Create a list to store htmls
        soups = []

        while True:
            # Scroll down to the bottom of the page
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for a moment to allow new content to load (adjust as needed)
            time.sleep(5)
            
            # Parse the HTML
            html = driver.page_source

            # Create a BeautifulSoup object from the scraped HTML
            soups.append(BeautifulSoup(html, 'html.parser'))

            # Get the current page height
            current_height = driver.execute_script("return document.body.scrollHeight")

            if current_height == initial_height:
                break  # Exit the loop when you can't scroll further

            initial_height = current_height  # Update the initial height for the next iteration
        
        # List to store the post image URLs
        post_urls = []

        for soup in soups:
            # Find all anchor elements with href attributes
            anchors = soup.find_all('a', href=True)
            
            # Filter URLs that start with "/p/" or "/reel/"
            post_urls.extend([anchor['href'] for anchor in anchors if anchor['href'].startswith(("/p/", "/reel/"))])

        # Convert the list to a set to remove duplicates
        unique_post_urls = list(set(post_urls))
        print(unique_post_urls)

        print(f"before: {len(post_urls)}, after: {len(unique_post_urls)}")
        

    finally:
        driver.quit()

chrome_driver_path = "D:\\Programs\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
user_name = "aleedoe_"
password_user = "kasurrusak"

startScraping(chrome_driver_path, user_name, password_user)
