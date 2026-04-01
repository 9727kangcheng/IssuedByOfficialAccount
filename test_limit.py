# -*- coding: utf-8 -*-
import requests, json

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

resp = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
    'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
}, timeout=10)
token = resp.json().get('access_token')

# 用之前的thumb_id
thumb_id = 'KUAn_T9JQN0ReToESVkw9PrwMatC1OKurK_cjJ_bCTIry3O0MBHiUFGfy5p85P7J'

# 测试不同长度的标题
test_cases = [
    ('短标题', 9, 9),
    ('居庸关长城', 15, 15),
    ('居庸关长城之旅', 21, 21),
    ('居庸关长城之旅1234', 27, 27),
    ('居庸关长城：旅行', 33, 33),
    ('居庸关长城：一场说走就走的旅行', 45, 45),
    ('test12345', 10, 10),
]

for name, chars, bytes_len in test_cases:
    title = name if 'test' in name else name
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
    print(f'{title}: {chars}c/{bytes_len}b -> {status}')
