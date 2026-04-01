# -*- coding: utf-8 -*-
import requests, json

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

resp = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
    'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
}, timeout=10)
token = resp.json().get('access_token')

thumb_id = 'KUAn_T9JQN0ReToESVkw9PrwMatC1OKurK_cjJ_bCTIry3O0MBHiUFGfy5p85P7J'

# 测试字符数限制
test_titles = [
    ('A' * 10, '10A'),
    ('A' * 11, '11A'),
    ('A' * 20, '20A'),
    ('中' * 10, '10中'),
    ('中' * 11, '11中'),
    ('a中' * 5, '5a+5中'),  # 10字符
    ('a中' * 6, '6a+6中'),  # 12字符
    ('test中' * 2, '4test+2中'),  # 6字符
    ('test中' * 3, '4test+3中'),  # 7字符
    ('test中' * 4, '4test+4中'),  # 8字符
    ('test中' * 5, '4test+5中'),  # 9字符
    ('test中' * 6, '4test+6中'),  # 10字符
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
    print(f'{desc} ({len(title)}字符): {status}')
