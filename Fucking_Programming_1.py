import os
import requests

if (os.name == "nt"):
    _ = os.system("cls")

try:
    # توکن دسترسی و شناسه کاربری اینستاگرام خود را وارد کنید
    # توکن دسترسی که از Facebook Developer Console دریافت کرده‌اید
    access_token = "EAAH62rWeZAb4BO5ZCLHZBrZCTBX3iMHNgn3fe3trcfSv8RsM0vP318qrwDehhyq7Pfzu5cOTH0ZC2NVLpeA75H89eZCcINXbN6Hin3ZAb8HpaVQn5Rd2GjTAWXlxyEAWxeoIrBrsZCBZAKtoEOrpmjhd1vvNDpGrZAQxCbkUbUJHIBt6Ko3HGBi7DnxvqE3V5xK2T3QrvNMXpQf0UD1v4DfdsTGCeI1GLsmWeJBZAZAjTZAmRY13TltocCfoW5lzwZCUIZD"
    user_id = 'behdad_p'  # شناسه کاربری اینستاگرام خود

    # URL برای دریافت اطلاعات پروفایل
    url = f'https://graph.instagram.com/{user_id}?fields=id,username,media_count,account_type&access_token={access_token}'
    #url = "https://graph.instagram.com/behdad_p?fields=id,username,media_count,account_type&access_token=EAAH62rWeZAb4BO5ZCLHZBrZCTBX3iMHNgn3fe3trcfSv8RsM0vP318qrwDehhyq7Pfzu5cOTH0ZC2NVLpeA75H89eZCcINXbN6Hin3ZAb8HpaVQn5Rd2GjTAWXlxyEAWxeoIrBrsZCBZAKtoEOrpmjhd1vvNDpGrZAQxCbkUbUJHIBt6Ko3HGBi7DnxvqE3V5xK2T3QrvNMXpQf0UD1v4DfdsTGCeI1GLsmWeJBZAZAjTZAmRY13TltocCfoW5lzwZCUIZD"

    # ارسال درخواست به API
    response = requests.get(url)

    # نمایش اطلاعات پاسخ
    if response.status_code == 200:
        profile_data = response.json()
        print("ID:", profile_data['id'])
        print("Username:", profile_data['username'])
        print("Media Count:", profile_data['media_count'])
        print("Account Type:", profile_data['account_type'])
    else:
        print("Error:", response.status_code)
except Exception as e:
    print(f"Error: {e}")
