import requests
from uuid import uuid4
you = input("input your user : ")
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.146 Mobile Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'package': 'ins.bradychrist.com',
    'apptype': 'android',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'idfa': str(uuid4),
    'version': '1.0',
    'Origin': 'http://www.bradychrist.top',
    'X-Requested-With': 'ins.bradychrist.com',
    'Referer': 'http://www.bradychrist.top/h5_v12/',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    
}

data = {
    'username': you,
}

response = requests.post('http://www.bradychrist.top/api/v7/user', cookies=None, headers=headers, data=data).json()
try:
 u = response["data"]["userPk"]
 v = response["data"]["username"]
 vz = response["data"]["avatar"]
 vx = response["data"]["followerNum"]
 xz = response["data"]["followingNum"]
 xxx = response["data"]["postsNum"]
 xnx = response["data"]["isNewUser"]
 
 print(f"\nuser id : {u}\nuser name : {v}\n\nphoto avatar : {vz}\n\nfollow num : {vx}\nfollowing num : {xz}\npost num : {xxx}\n is new user ? : {xnx}")
except:
 print(None)
