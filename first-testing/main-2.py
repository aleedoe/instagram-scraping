import json
import requests

url = 'https://www.instagram.com/graphql/query'

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=EC14FC3F-9357-4441-AEFB-53EB730ABD90; datr=zFgXZdRGC-535k0CAitDybVA; mid=ZRdYzgALAAGBplh9c22viuzLmvvj; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; ps_n=1; ps_l=1; shbid="9690\\0549212171449\\0541754748943:01f79d462ffcca7292de3256d5704ec6dcd29fa115293d7cb3450fd68b0f792ff85f1a73"; shbts="1723212943\\0549212171449\\0541754748943:01f7e02340085814677b0c2f8f73aac79aa059b7710382c925febcf75ded6d4cb3263820"; ds_user_id=13205355323; csrftoken=1FOJWuO2uqlLywpIkOwVa3bV1NaNWAv2; wd=1517x712; dpr=0.8999999761581421; fbsr_124024574287414=2oSw20YFFMPLjCtzxCCwalh8SBfn9HJCPM_9Tq8p5Js.eyJ1c2VyX2lkIjoiMTAwMDM1OTk1MjUwNDMxIiwiY29kZSI6IkFRQlBweUYwcHM1blBSLWVCbDhTYUdFeWxtN0lGU3Y5akpOWVpydHQ1UmhEblZrT2l5bFI0YU44czJJMTRTcEtEUXdzTHJtRU8tUkRfbmFUdXMydUdJYlJ2YTYtRzFRR3Y5WkZ1N0xUMVRNR1pNb3NHM0l4aTUtd0F4S1QtbGExaTZfTHNqMW1fQ0hsc1NRWDZ1eHZfazB4U0dEVnB0bG1kZENIOUh6LXlQMDdlM0RJZC01Yjc2Z1k2RVhLTXJ4VW5iSV9HWG1YdkpBWVl2dkcwZUcydGhTaEhCazFZQlI2MF9USDRobUt5alA4SEQ0b09GcHgxcEpRYW5nUVBGMlZZRmh5b3AtektEM1lxNnJKYzk2Y2w5Y25UMnpmRjctb0dzc21abDhMbkpTSE51LWtyWVFGMXlIWlRfeWFiVjB5N0Fsakw5SGMyY2draXE3Z2dTX0luNGlxIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzhTaEtrWkJ3YnhwZ0dKN2JnQlhkNVM4WDA5ZDJqYkNlSlFpWkJKeUhoQ1JiM0pBWkFIc2lFdFFkMk5lRjVGZmw5dVByamttZ3E2OVpDYmIwaVIxWXdjWDRzdjdVQXNySndoMENTOXBFYnllRmx2NTBzQ0JBVHU0UndnOU5jTmJ5Mko5Y2tkUTBGTUVvTWtiYzFHbXM5Q2dudDY0T0ZvMUdQYXFKSEhaQ25YWkE4WWdaRFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE3MjM0MzYwOTR9; sessionid=13205355323%3AXwi6o98sMWXZL3%3A18%3AAYcMhaimlX90Bd2xsjDJfQvllGY3RLwn-1W1yvLsdA; rur="EAG\\05413205355323\\0541754972522:01f72aaf6350683eeb8537be1766aff58cf0a1cdc2b227d68a55d00ebc597900d6563116"',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/agablackjack/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.100", "Chromium";v="127.0.6533.100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-asbd-id': '129477',
    'x-bloks-version-id': 'd48864a035b1835e7d6839f3f4f6eccef248b3d94fbc4ded47b31025a6d691c3',
    'x-csrftoken': '1FOJWuO2uqlLywpIkOwVa3bV1NaNWAv2',
    'x-fb-friendly-name': 'PolarisProfilePostsTabContentDirectQuery_connection',
    'x-fb-lsd': 'l-9up_mPTWVtCwao7NuC6K',
    'x-ig-app-id': '936619743392459'
}

data = {
    'av': '17841413299690669',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': 'w',
    '__hs': '19947.HYP:instagram_web_pkg.2.1..0.1',
    'dpr': '1',
    '__ccg': 'UNKNOWN',
    '__rev': '1015584519',
    '__s': '5lzhhx:ieo156:1mlmuh',
    '__hsi': '7402103409766805159',
    '__dyn': '7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awgo9oO0n24oaEnxO1ywOwv89k2C1Fwc60D87u3ifK0EUjwGzEaE2iwNwmE2eUlwhEe87q7U1mVEbUGdwtUd-2u2J0bS1LwTwKG1pg2fwxyo6O1FwlEcUed6goK2OubxKi2qi7E5yqcxK2K1ew',
    '__csr': 'gevd6gmNp2n94N58hb6lEBsyF99cyH-p5JXlGV9CJ9uCp2dFjBJ5muytbBCKmFUWuLVBFkuAiEHCBKEDGKB-Qhat2VVECUnBBAVV9RgWm4GK4uFqDHCgix5vFXAy6FrBghVFQmazokCxm00iw-fxe2e2mdgjwbR02KE2kx-1go2-whEbpk0kUMy0G4EG02nZwGahACgCAE6i0w89FAFEb8d8lz9h4E1k9lcJCAoh42m2p0wwaW1Vp9wAE8A2kje222W10w-UG0ghDBwyg9o7C0eSwLAsE0brE05sO',
    '__comet_req': '7',
    'fb_dtsg': 'NAcMGKxZHtcQfEqL5Ivm1bKl7bksqliJT9NAnqIefMiqNXogztmjTtw:17853828322093762:1723293317',
    'jazoest': '26617',
    'lsd': 'l-9up_mPTWVtCwao7NuC6K',
    '__spin_r': '1015584519',
    '__spin_b': 'trunk',
    '__spin_t': '1723436501',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisProfilePostsTabContentDirectQuery_connection',
    'variables': '{"after":"3413329042532123727_1024760936","before":null,"data":{"count":100,"include_relationship_info":true,"latest_besties_reel_media":true,"latest_reel_media":true},"first":100,"last":null,"username":"agablackjack","__relay_internal__pv__PolarisFeedShareMenurelayprovider":false}',
    'server_timestamps': 'true',
    'doc_id': '7935114066569227'
}

response = requests.post(url, headers=headers, data=data)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    
    # Save the data to a JSON file
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data successfully saved to data.json")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
