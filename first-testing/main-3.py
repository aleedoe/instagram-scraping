from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json

# Set up Chrome options and enable logging
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

# Set up the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://www.tokopedia.com/lbagstore/masker-3-ply-putih-white-orlee-medis-3ply-earloop-kemenkes-3ply-50-putih?extParam=src%3Dmultiloc%26whid%3D7108&source=homepage.left_carousel.0.303847')

# Capture and print network requests
logs = driver.get_log('performance')

for log in logs:
    message = json.loads(log['message'])
    message_content = message['message']
    
    # Check if the message contains a response from the specific endpoint
    if message_content['method'] == 'Network.responseReceived':
        response_url = message_content['params']['response']['url']
        if response_url == 'https://gql.tokopedia.com/graphql/PDPGetLayoutQuery':
            request_id = message_content['params']['requestId']
            
            # Immediately try to get the response body using the request ID
            try:
                response_body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': request_id})
                print(f"ini adalah data response --> {response_body['body']}")
            except Exception as e:
                print(f"Error capturing response body: {e}")

driver.quit()
