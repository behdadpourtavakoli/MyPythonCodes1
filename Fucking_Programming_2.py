import os, requests, getpass
from datetime import datetime

if (os.name == "nt"):
    _ = os.system("cls")

time = int(datetime.now().timestamp())
def IsExists(user, password):
    url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
    password=password

    payload = { 'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
                'optIntoOneTap': 'false',
                'queryParams': {},
                'username': user }
    files = [
    ]

    headers = {
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        csrf=response.cookies["csrftoken"]
        mid=response.cookies["mid"]
        ig_did=response.cookies["ig_did"]
        ig_nrcb=response.cookies["ig_nrcb"]
        headers = { 'X-Csrftoken': f'{csrf}', 'Cookie': f"csrftoken={csrf}; mid={mid}; ig_did={ig_did}; ig_nrcb={ig_nrcb};" }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        return(response.json())
    except Exception as e:
        print(f"OP Error: {e}")
        return(None)

try:
    print("Connect/Login to Instagram by Python.\r\n")

    user = input("Enter Username: ")
    password = input("Enter Password: ")
    # password = getpass.getpass("Enter Password: ")
    print()
    
    x = IsExists(user, password)
    if (x["status"] == "ok" and x["authenticated"] != None and x["authenticated"] == True):
        print("user and password matching ")
    else:
        print("no password or user are correct")
        print(x)
except Exception as e:
    print(f"OP Error: {e}")
