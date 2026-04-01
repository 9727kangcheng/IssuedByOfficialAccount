# -*- coding: utf-8 -*-
import requests, json, os

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

resp = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
    'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
}, timeout=10)
token = resp.json().get('access_token')
print(f'Token OK')

# 上传封面
img_dir = r'D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher\downloaded_images'
files = [f for f in os.listdir(img_dir) if f.endswith('.jpg')][:1]
with open(os.path.join(img_dir, files[0]), 'rb') as f:
    resp = requests.post('https://api.weixin.qq.com/cgi-bin/material/add_material',
        params={'access_token': token, 'type': 'thumb'}, files={'media': f}, timeout=30)
thumb_id = resp.json().get('media_id')
print(f'Thumb ID: {thumb_id}')

# 测试不同title长度
test_titles = ['Test', '居庸关长城', '居庸关长城之旅', '居庸关长城之旅11111']
for t in test_titles:
    resp = requests.post('https://api.weixin.qq.com/cgi-bin/draft/add',
        params={'access_token': token},
        json={'articles': [{'title': t, 'author': '硬石', 'content': '<p>test</p>', 'thumb_media_id': thumb_id}]},
        timeout=10)
    data = resp.json()
    if 'media_id' in data:
        print(f'OK: "{t}" ({len(t)} chars, {len(t.encode("utf-8"))} bytes)')
    else:
        print(f'FAIL: "{t}" ({len(t)} chars) - {data.get("errmsg")}')
