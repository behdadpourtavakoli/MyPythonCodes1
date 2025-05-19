# Connect to the Facebook account by Access Token on 1403/09/04
# 
# Verbinden Sie sich mit dem Facebook-Konto per Access Token am 1403/09/04

import os
import requests

if (os.name == "nt"):
    _ = os.system("cls")

ACCESS_TOKEN = "EAAbZBMSxMjNEBO0Wze6RMdgjpQcMsnv8FCPkVJ3r30oYJLeDdgqCWP8T2ihPtJplwxEZBPAWqrTYeJWuxnRJMvd71r4lmxAiRH7rsGDdsFJmYtbGFfEzuNFxO39Does2qZAyzhlAfhTntifbsEvBLLTW6wKAZCAjzd2zJlgpQmuSnNgLK5d9cHXsokZBbQIADtG6TP8pfIwpIac29vV1U755flsuiZA3C9ws5ubJzXFEC2dA6Es2IG2oCcwIDF"

try:
    # URL برای دریافت اطلاعات پروفایل
    url = f"https://graph.facebook.com/me?fields=id,name,email&access_token={ACCESS_TOKEN}"

    # ارسال درخواست
    response = requests.get(url)

    # بررسی پاسخ
    if response.status_code == 200:
        print("Profile data:", response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")
except Exception as e:
    print(f"OP Error: {e}")
