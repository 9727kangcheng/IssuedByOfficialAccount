# -*- coding: utf-8 -*-
import requests, json

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

# 每次都重新获取token
def get_token():
    resp = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
        'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
    }, timeout=10)
    return resp.json().get('access_token')

# 先上传一个thumb
import os
img_dir = r'D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher\downloaded_images'
files = [f for f in os.listdir(img_dir) if f.endswith('.jpg')][:1]
token = get_token()
with open(os.path.join(img_dir, files[0]), 'rb') as f:
    resp = requests.post('https://api.weixin.qq.com/cgi-bin/material/add_material',
        params={'access_token': token, 'type': 'thumb'}, files={'media': f}, timeout=30)
result = resp.json()
thumb_id = result.get('media_id')
print(f'Thumb ID: {thumb_id[:20]}...')

# 测试标题限制
def test_title(title):
    token = get_token()  # 每次新token
    payload = {
        'articles': [{
            'title': title,
            'author': '硬石',
            'content': '<p>test</p>',
            'thumb_media_id': thumb_id
        }]
    }
    resp = requests.post('https://api.weixin.qq.com/cgi-bin/draft/add',
        params={'access_token': token}, json=payload, timeout=10)
    data = resp.json()
    return 'OK' if 'media_id' in data else f'FAIL({data.get("errcode")})'

# 找出限制
print('Testing title limits...')
print(f'10中文: {test_title("中" * 10)}')
print(f'11中文: {test_title("中" * 11)}')
print(f'12中文: {test_title("中" * 12)}')
print(f'13中文: {test_title("中" * 13)}')
print(f'14中文: {test_title("中" * 14)}')
print(f'15中文: {test_title("中" * 15)}')
print(f'14ASCII: {test_title("A" * 14)}')
print(f'15ASCII: {test_title("A" * 15)}')
print(f'16ASCII: {test_title("A" * 16)}')
print(f'17ASCII: {test_title("A" * 17)}')
print(f'18ASCII: {test_title("A" * 18)}')
print(f'19ASCII: {test_title("A" * 19)}')
print(f'20ASCII: {test_title("A" * 20)}')
