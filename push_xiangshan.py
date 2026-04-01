# -*- coding: utf-8 -*-
import requests, json

app_id = 'wx668d7edefc166605'
app_secret = '5e34e46f3d5f79a69ffd5978d88eb826'

# 获取 token
token = requests.get('https://api.weixin.qq.com/cgi-bin/token', params={
    'grant_type': 'client_credential', 'appid': app_id, 'secret': app_secret
}, timeout=10).json()['access_token']
print('Token OK')

thumb_media_id = 'KUAn_T9JQN0ReToESVkw9EnknSL2VZtDSvAQqXCUWE2TIK4dBfoZ9j0YiAqgxOTw'
img_url = 'http://mmbiz.qpic.cn/mmbiz_jpg/rBPNqw2AMGXSa5zT4yzg8pZs3ibTgdmXS6Ovuatym6kWn4sLGOzFWYcOQrGzicZjTroouCsQI5cGaaNibhNN4JWOVb0jctyUY3BZgtvOqic6PxI/0?wx_fmt=jpeg'

title = '香山春日踏青'

content = (
    '<p style="text-align:center"><img src="' + img_url + '" style="max-width:100%"/></p>'
    '<p>春风拂过山野，万物渐次复苏，硬石户外的家人们齐聚香山，赴一场春日之约。'
    '这是一场久违的相聚，大家卸下城市的忙碌，在专业领队的带领下，沿着舒缓的小径一路前行。</p>'
    '<p>眼前的香山，不愧是"北京的后花园"。这里山峦叠翠，古木参天，清风徐来，带着山野特有的清新气息。'
    '阳光倾泻而下，林间光影斑驳，与脚下蜿蜒的山路相映成趣，构成了一幅绝美的自然画卷。'
    '大家穿梭在春风里，脚步轻快，彼此照应，那份独属于团队的默契与温暖，在山野间悄然流淌。</p>'
    '<p>群友们一路欢声笑语，有人在香炉峰顶驻足沉思，有人在碧云寺前定格美好瞬间。'
    '春日的生机盎然，配上大家发自内心的笑容，让这片香山更显动人。'
    '感谢每一位靠谱的伙伴，是你们的热情与活力，让这次踏青充满了意义。</p>'
    '<p>这个春天，硬石户外与大家一起，在徒步中拥抱自然，在同行中收获情谊。'
    '期待下一次，我们继续携手，奔赴更多山野之美！</p>'
)

draft_data = {
    'articles': [{
        'title': title,
        'author': '',
        'digest': '春风拂过香山，硬石户外与你共赴山野之约。',
        'content': content,
        'content_source_url': '',
        'thumb_media_id': thumb_media_id,
        'show_cover_pic': 1,
        'need_open_comment': 1,
        'only_fans_can_comment': 0
    }]
}

resp = requests.post(
    'https://api.weixin.qq.com/cgi-bin/draft/add',
    params={'access_token': token},
    data=json.dumps(draft_data, ensure_ascii=False).encode('utf-8'),
    headers={'Content-Type': 'application/json; charset=utf-8'},
    timeout=15
)
result = resp.json()
print('Draft result:', json.dumps(result, ensure_ascii=False))
