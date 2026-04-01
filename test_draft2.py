# -*- coding: utf-8 -*-
import requests, json, os

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

resp = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
    'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
}, timeout=10)
token = resp.json().get('access_token')

# 上传封面
img_dir = r'D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher\downloaded_images'
files = [f for f in os.listdir(img_dir) if f.endswith('.jpg')][:1]
with open(os.path.join(img_dir, files[0]), 'rb') as f:
    resp = requests.post('https://api.weixin.qq.com/cgi-bin/material/add_material',
        params={'access_token': token, 'type': 'thumb'}, files={'media': f}, timeout=30)
thumb_id = resp.json().get('media_id')
print(f'Thumb ID: {thumb_id[:30]}...')

# 测试1：短content
content1 = '<p>test</p>'
resp = requests.post('https://api.weixin.qq.com/cgi-bin/draft/add',
    params={'access_token': token},
    json={'articles': [{'title': 'Test1', 'author': '硬石', 'content': content1, 'thumb_media_id': thumb_id}]},
    timeout=10)
data = resp.json()
print(f'Short content: {"OK" if "media_id" in data else data.get("errmsg")}')

# 测试2：长URL content
long_url = 'http://mmbiz.qpic.cn/sz_mmbiz_jpg/rBPNqw2AMGVJr0iajzByoY7RLFET7IvlgHCRmiaPFupuRqCTL0yFEDXKkDaJ7cNeFTEDtiaOErauwQtPFSEnuAIolu0uJbMRVPOicLIYT7yMEVM/0?wx_fmt=jpeg'
content2 = f'<p><img src="{long_url}" /></p><p>test content</p>'
resp = requests.post('https://api.weixin.qq.com/cgi-bin/draft/add',
    params={'access_token': token},
    json={'articles': [{'title': 'Test2', 'author': '硬石', 'content': content2, 'thumb_media_id': thumb_id}]},
    timeout=10)
data = resp.json()
print(f'Long URL content: {"OK" if "media_id" in data else data.get("errmsg")}')
print(f'  Content length: {len(content2)} chars')
