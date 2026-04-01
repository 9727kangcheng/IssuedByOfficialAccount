# -*- coding: utf-8 -*-
import requests, json

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

resp = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
    'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
}, timeout=10)
token = resp.json().get('access_token')

thumb_id = 'KUAn_T9JQN0ReToESVkw9PrwMatC1OKurK_cjJ_bCTIry3O0MBHiUFGfy5p85P7J'

# 测试字符数限制（而不是字节数）
test_titles = [
    ('中' * 10, '10中文'),
    ('中' * 15, '15中文'),
    ('中' * 20, '20中文'),
    ('中' * 25, '25中文'),
    ('中' * 30, '30中文'),
    ('中' * 35, '35中文'),
    ('test中' * 5, '5test+5中'),
    ('test中' * 8, '8test+8中'),
]

for title, desc in test_titles:
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
    status = 'OK' if 'media_id' in data else f'FAIL({data.get("errcode")})'
    print(f'{desc} ({len(title)}c/{len(title.encode("utf-8"))}b): {status}')
