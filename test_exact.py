# -*- coding: utf-8 -*-
import requests, json, os

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

# 获取token
resp = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
    'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
}, timeout=10)
token = resp.json().get('access_token')
print(f'Token OK: {token[:20]}...')

# 上传封面
img_dir = r'D:\Program Files\QClaw\resources\openclaw\config\skills\wechat-publisher\downloaded_images'
files = [f for f in os.listdir(img_dir) if f.endswith('.jpg')][:1]
print(f'Uploading: {files[0]}')

with open(os.path.join(img_dir, files[0]), 'rb') as f:
    resp = requests.post('https://api.weixin.qq.com/cgi-bin/material/add_material',
        params={'access_token': token, 'type': 'thumb'}, files={'media': f}, timeout=30)
result = resp.json()
thumb_id = result.get('media_id')
cover_url = result.get('url', '')
print(f'Thumb ID: {thumb_id}')
print(f'Cover URL: {cover_url[:50]}...')

# 准备数据（完全模拟程序中的逻辑）
title = '居庸关长城：一场说走就走的旅行'
content = '在这个居庸关长城，我们找到了久违的宁静。'
html_content = f'<p><img src="{cover_url}" /></p><p>{content}</p>'
safe_title = title[:15] if len(title) > 15 else title
safe_author = "硬石"
safe_digest = content[:20] if len(content) > 20 else content

articles = [{
    "title": safe_title,
    "author": safe_author,
    "digest": safe_digest,
    "show_cover_pic": 1,
    "content": html_content,
    "content_source_url": "",
    "thumb_media_id": thumb_id
}]

payload = {"articles": articles}
json_str = json.dumps(payload, ensure_ascii=False)
print(f'JSON length: {len(json_str)}')
print(f'Title: {safe_title}')
print(f'Title bytes: {len(safe_title.encode("utf-8"))}')

# 发送请求
resp = requests.post('https://api.weixin.qq.com/cgi-bin/draft/add',
    params={'access_token': token}, json=payload, timeout=10)
data = resp.json()
print(f'Result: {json.dumps(data, indent=2, ensure_ascii=False)}')
