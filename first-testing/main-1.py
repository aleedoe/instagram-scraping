import requests
import json

# URL
url = 'https://www.instagram.com/graphql/query'

# Headers
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'ig_did=EC14FC3F-9357-4441-AEFB-53EB730ABD90; datr=zFgXZdRGC-535k0CAitDybVA; mid=ZRdYzgALAAGBplh9c22viuzLmvvj; ig_nrcb=1; fbm_124024574287414=base_domain=.instagram.com; ps_n=1; ps_l=1; shbid="9690\0549212171449\0541754748943:01f79d462ffcca7292de3256d5704ec6dcd29fa115293d7cb3450fd68b0f792ff85f1a73"; shbts="1723212943\0549212171449\0541754748943:01f7e02340085814677b0c2f8f73aac79aa059b7710382c925febcf75ded6d4cb3263820"; ds_user_id=13205355323; csrftoken=1FOJWuO2uqlLywpIkOwVa3bV1NaNWAv2; sessionid=13205355323%3AXwi6o98sMWXZL3%3A18%3AAYeuyMM5LhbVz3AK7xfIv3tynRwEHEtq12flrMLUpA; wd=1517x712; dpr=0.8999999761581421; fbsr_124024574287414=RMjVuWJLrpJH0PgsLYFZ7taVXnNB7C5c8ZU8otCjoYc.eyJ1c2VyX2lkIjoiMTAwMDM1OTk1MjUwNDMxIiwiY29kZSI6IkFRQWlSLVpPcHVraE8wQVpya0o1alBoWWtGbTdUWmZMNnktVGt0cVh2bm1VWFF0amhPOVFrMEFXUi0yNkFnY212Q2VadVRQZ1dtQ3dwTmF6VEFTSEd6T1BQYzJPQ0JlMi1VcDlZdEVrdEtQekx1cWdmRnc5Zjk4cEUyb28xeUtzMHRPQ3o3MTFib2FOdHhRUnowZy05VFRhSWxWVG1HU1R3Rk5ua1FUVVA1em03V0Y5SDVWOW0yc2RuWmJ1b3B2LU9LMDRsd093YzdRZ2hQZXJKVDRZSUJ1Q2Q1Y3N6anhoR2k5VXY2TGQxbVViMjJiVE9odlZUY2ZDR0ZacWFWOHRXUUZLT2ttT3o4YVNpdnQtUzRYUVdlTjl2X1Q3LVl4TXVYRE5fRjZoNkd4RHpMUEZ5a3JSd3hBbDdGMmo2MENSWjdRWEV2U0xzeDBoUmtuNms4aGU2ZGVUIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCTzdCbzlhYm5pTDBMaTFKS1pBb3Z2enV4dUg2VjA1RlpCVUFWQlpDeWZJNXpDcWlkd0diVnlTNk9sMzUzQ0w0OFM4MExtM2hUaVdycWhOZlYyUkZMYW9jVW1jdWhHdHphNmNFOHBRV3hPVmF4VFcyZFpDc3JhOFJ4S3paQmpsNHNjSEJtdkNOZkQ5aUVaQTlzVFNuZFBpYVduRzJIczJiMkJSZXJxZVl5bVZVNUNqNmJoUlBtaG9pdEVaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNzIzNDMyMDIwfQ; rur="EAG\05413205355323\0541754968118:01f74537928f2a900fc3109fd8bee2ab5fc21b5c269e055a5a7f30ef19e91d59197a5eb1"; fbsr_124024574287414=ExD1_gwNd05S7ULEDSuHHGm9mqTWEXpIWWvG9-EwBTg.eyJ1c2VyX2lkIjoiMTAwMDM1OTk1MjUwNDMxIiwiY29kZSI6IkFRQlpCM0ZfaHBNT1ZXSU85Uk5oM0hnX0pYQmU4MG5lMmVla290WEFzUU5GMXBicnJ4S0V4dXgtdUhYdzB2bmJER2tGR2VoRS1Bbi1UNE9uOU85enJpQ1dxc2xWYVhlVjhnVDhUaXBDRXRURXB2aFU0VG1lT0pEZEUyYUJLa3lwcV81VEJSU25VUFpGaG13QV9PN2R1ZVgyMG9fVHU1cFF0VXJpWjdpNzJrN3V2VXVTTEU0Y01QcjN1T2xOQ3dSWUlOYWtzcFNlT2ZrOG1JYjJmNmYwbk1qaEZpZ1E3SUhFRXI5NVJyeGs4Zl9TM3JZREk5YnBhZ0R4N05BRU1pWTVlUmFsc0x3NjNhNzJ1em94aWZWYmlSazNGYmhjOU8xYTYzNnBEbGVGYkdlZlp1NGZGb1k4ZEZUbkYxNWIwNGpnZUhwbmtvUWRJUFVLcTdjcnA0eFZIVUVFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCT1pCa1pBaEE5dVVDbUtyNVdHVGx3ZzVQa3pFOUJWSTc0V2ZBUzdRUUhSb05PZVpCMTBkdXRLaEtNQWp3bVhSb0tuclpCSnVFU3hHOERveE1VOUZHYlFuOURsbWJVOTVFTlRSQWFzQXZFS0FpYjlGNW1TNUFZUjdYdEJaQzd1UHE2OXZFUmtraHFUeFpDV2Uwc2VIS1huYkxlUVNudk5TemxIY1U1RXZEd3laQ2VGNGhsN3NPR2xLQUswWkQ"',
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
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR2l6MIgA_-1VSVpUmsAg6Si2nNGR-vtqAa8g_yEBX4tAVIM',
    'x-instagram-ajax': '2c0a81d5c45c',
    'x-requested-with': 'XMLHttpRequest'
}

# Parameters
params = {
    'query_hash': 'c6809c9c025875ac6f02619eae97a80e',
    'variables': '{"id":"1541000085","first":12}'
}

# Send the request
response = requests.get(url, headers=headers, params=params)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    
    # Save the data to a JSON file
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data successfully saved to data.json")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
