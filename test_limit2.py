# -*- coding: utf-8 -*-
import requests, json

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

resp = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
    'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
}, timeout=10)
token = resp.json().get('access_token')

thumb_id = 'KUAn_T9JQN0ReToESVkw9PrwMatC1OKurK_cjJ_bCTIry3O0MBHiUFGfy5p85P7J'

# 测试精确限制
# 之前33字节通过，45字节失败，找临界点
test_titles = [
    ('A' * 40, '40纯ASCII'),
    ('A' * 64, '64纯ASCII'),
    ('A' * 20 + '中' * 10, '20+10混'),
    ('中' * 20, '20纯中文'),
    ('中' * 30, '30纯中文'),
    ('中' * 40, '40纯中文'),
    ('中' * 35, '35纯中文'),
    ('中' * 38, '38纯中文'),
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
